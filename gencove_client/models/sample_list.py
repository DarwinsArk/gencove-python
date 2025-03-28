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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gencove_client.models.archive_sample_status import ArchiveSampleStatus
from gencove_client.models.sample_status_nested import SampleStatusNested
from typing import Optional, Set
from typing_extensions import Self


class SampleList(BaseModel):
    """
    SampleList
    """  # noqa: E501

    id: Optional[StrictStr] = None
    run: Optional[StrictStr] = None
    created: Optional[datetime] = None
    hidden: Optional[StrictBool] = Field(default=None, description="Flag to hide the sample.")
    modified: datetime
    client_id: Annotated[str, Field(min_length=1, strict=True, max_length=250)] = Field(
        description="Legacy: external_id"
    )
    physical_id: Annotated[str, Field(min_length=1, strict=True, max_length=250)] = Field(
        description="Legacy: external_id, external_barcode and sample_barcode"
    )
    legacy_id: Annotated[str, Field(min_length=1, strict=True, max_length=250)] = Field(
        description="Legacy: sample_id/member_id. Matching sample_ids from back_api app."
    )
    last_status: Optional[SampleStatusNested] = None
    archive_last_status: Optional[ArchiveSampleStatus] = None
    failed_qc: Optional[StrictStr] = Field(default=None, description="Description of failed_qc status if present")
    __properties: ClassVar[List[str]] = [
        "id",
        "run",
        "created",
        "hidden",
        "modified",
        "client_id",
        "physical_id",
        "legacy_id",
        "last_status",
        "archive_last_status",
        "failed_qc",
    ]

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
        """Create an instance of SampleList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "id",
                "failed_qc",
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
        # override the default output from pydantic by calling `to_dict()` of archive_last_status
        if self.archive_last_status:
            _dict["archive_last_status"] = self.archive_last_status.to_dict()
        # set to None if run (nullable) is None
        # and model_fields_set contains the field
        if self.run is None and "run" in self.model_fields_set:
            _dict["run"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SampleList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "run": obj.get("run"),
                "created": obj.get("created"),
                "hidden": obj.get("hidden"),
                "modified": obj.get("modified"),
                "client_id": obj.get("client_id"),
                "physical_id": obj.get("physical_id"),
                "legacy_id": obj.get("legacy_id"),
                "last_status": (
                    SampleStatusNested.from_dict(obj["last_status"]) if obj.get("last_status") is not None else None
                ),
                "archive_last_status": (
                    ArchiveSampleStatus.from_dict(obj["archive_last_status"])
                    if obj.get("archive_last_status") is not None
                    else None
                ),
                "failed_qc": obj.get("failed_qc"),
            }
        )
        return _obj
