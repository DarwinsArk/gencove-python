#!/usr/bin/env bash

docker run --rm \
    -v "$(pwd):/local" \
    openapitools/openapi-generator-cli \
    generate -i "https://api.gencove.com/api/v2/docs/?format=openapi" -g python -o /local --package-name gencove_client
