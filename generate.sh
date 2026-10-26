#!/usr/bin/env bash

set -euo pipefail

# Pin the generator so regenerations are reproducible; bump deliberately.
GENERATOR_IMAGE="openapitools/openapi-generator-cli:v7.26.0"

# The spec is committed so regenerations are reproducible. Run with
# --update-spec to download the current spec from Gencove first.
SPEC_URL="https://api.gencove.com/api/v2/openapi.json"
SPEC_FILE="openapi.json"

if [ "${1:-}" = "--update-spec" ]; then
    echo "Downloading $SPEC_URL"
    curl -fsSL "$SPEC_URL" -o "$SPEC_FILE"
fi

# Package version tracks the API version in the spec.
API_VERSION=$(python3 -c 'import json, sys; print(json.load(open(sys.argv[1]))["info"]["version"])' "$SPEC_FILE")

if [ -z "$API_VERSION" ]; then
    echo "❌ Could not extract version from $SPEC_FILE" >&2
    exit 1
fi

# Gencove uses "v2"; expand to semantic versioning (e.g., "v2" -> "2.0.0")
API_VERSION="${API_VERSION#v}"
if [[ "$API_VERSION" =~ ^[0-9]+$ ]]; then
    PACKAGE_VERSION="${API_VERSION}.0.0"
else
    PACKAGE_VERSION="$API_VERSION"
fi

echo "Generating gencove_client $PACKAGE_VERSION (spec version $API_VERSION) with $GENERATOR_IMAGE"

# Patch a temporary copy of the spec for what the generator can't handle, so
# the committed spec stays exactly what Gencove publishes. drf-spectacular
# writes nullable choice fields as oneOf [XEnum, BlankEnum, NullEnum], where
# NullEnum is {"enum": [null]}; the generator turns that into invalid Python
# ("class NullEnum(, Enum)"). Drop null-only enums from oneOf/anyOf and mark
# the field nullable instead, which means the same thing.
PATCHED_DIR=$(mktemp -d)
trap 'rm -rf "$PATCHED_DIR"' EXIT
python3 - "$SPEC_FILE" "$PATCHED_DIR/openapi.json" <<'PY'
import json
import sys

spec = json.load(open(sys.argv[1]))
schemas = spec.get("components", {}).get("schemas", {})
null_refs = {f"#/components/schemas/{name}" for name, s in schemas.items() if s.get("enum") == [None]}


def patch(node):
    if isinstance(node, dict):
        for key in ("oneOf", "anyOf"):
            if key in node and any(item.get("$ref") in null_refs for item in node[key]):
                node[key] = [item for item in node[key] if item.get("$ref") not in null_refs]
                node["nullable"] = True
        for value in node.values():
            patch(value)
    elif isinstance(node, list):
        for value in node:
            patch(value)


patch(spec)
for ref in null_refs:
    del schemas[ref.rsplit("/", 1)[1]]
json.dump(spec, open(sys.argv[2], "w"), indent=2)
PY

# The generator never deletes files, so remove the ones it wrote last time;
# otherwise models and endpoints dropped from the spec would linger. Keep
# .openapi-generator-ignore and the paths it lists (matched exactly, not as
# globs), which hold local changes. If generation then fails, restore the
# removed files from git.
if [ -f .openapi-generator/FILES ]; then
    STALE=$(grep -vxF -e .openapi-generator-ignore -f <(grep -vE '^[[:space:]]*(#|$)' .openapi-generator-ignore) .openapi-generator/FILES || true)
    trap 'echo "❌ Generation failed; restoring the previous files" >&2; git checkout -- $STALE' ERR
    echo "$STALE" | xargs -r rm -f
fi

# --skip-validate-spec: Gencove names a security scheme "API key", which fails
# the generator's name check (no spaces). Renaming it in the spec would change
# the client's configuration.api_key["API key"], so validation is skipped.
#
# disallowAdditionalPropertiesIfNotPresent=false: follow the OpenAPI/JSON Schema
# default (objects are open), so unknown fields from the API are kept in
# additional_properties instead of being silently dropped.
docker run --rm \
    -u "$(id -u):$(id -g)" \
    -v "$(pwd):/local" \
    -v "$PATCHED_DIR:/spec:ro" \
    "$GENERATOR_IMAGE" \
    generate -i /spec/openapi.json -g python -o /local \
    --package-name gencove_client \
    --git-user-id DarwinsArk \
    --git-repo-id gencove-python \
    --skip-validate-spec \
    --additional-properties="packageVersion=${PACKAGE_VERSION},packageUrl=https://github.com/DarwinsArk/gencove-python,buildSystem=hatchling,disallowAdditionalPropertiesIfNotPresent=false"

trap - ERR

# Apply the repo's pre-commit fixes (black, trailing whitespace, end of file)
# so the generated code is committed in its formatted form. Hooks exit
# non-zero when they change files, so run them again to check it's clean.
pre-commit run --all-files > /dev/null || pre-commit run --all-files
