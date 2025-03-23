# coding: utf-8

"""
    Gencove Back API

    API for Gencove REST service. Visit <a href='https://gencove.com/'>gencove.com</a> and <a href='https://docs.gencove.com/'>docs.gencove.com</a> for more information. <br><hr><p>To work with Insomnia, you can generate a Gencove API key by <a target='_blank' href='https://web.gencove.com/account?filter=api-keys'>clicking here</a>. Once you have the API key and have imported the project in Insomnia as a <i>Request Collection</i>, enter the key in Insomnia under <i>Manage Environment</i>.</p><a href='https://insomnia.rest/run/?label=back_api2&uri=https%3A%2F%2Fv2-api-files-prod.s3.amazonaws.com%2Fpublic%2Finsomnia%2Finsomnia_gencove_prod.json' target='_blank'>Run in Insomnia</a><hr>

    The version of the OpenAPI document: v2
    Contact: info@gencove.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gencove_client.models.file_nested import FileNested
from gencove_client.models.upload_status_nested import UploadStatusNested
from typing import Optional, Set
from typing_extensions import Self


class Upload(BaseModel):
    """
    Upload
    """  # noqa: E501

    id: Optional[StrictStr] = None
    last_status: Optional[UploadStatusNested] = None
    file: FileNested
    created: Optional[datetime] = None
    destination_path: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(
        default=None, description="Destination path given by the user as an optional argument"
    )
    source: StrictStr
    user: StrictStr
    organization: StrictStr
    __properties: ClassVar[List[str]] = [
        "id",
        "last_status",
        "file",
        "created",
        "destination_path",
        "source",
        "user",
        "organization",
    ]

    @field_validator("source")
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["cli", "cli url", "basespace", "s3"]):
            raise ValueError("must be one of enum values ('cli', 'cli url', 'basespace', 's3')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Upload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "id",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of last_status
        if self.last_status:
            _dict["last_status"] = self.last_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict["file"] = self.file.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Upload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "last_status": (
                    UploadStatusNested.from_dict(obj["last_status"]) if obj.get("last_status") is not None else None
                ),
                "file": FileNested.from_dict(obj["file"]) if obj.get("file") is not None else None,
                "created": obj.get("created"),
                "destination_path": obj.get("destination_path"),
                "source": obj.get("source"),
                "user": obj.get("user"),
                "organization": obj.get("organization"),
            }
        )
        return _obj
