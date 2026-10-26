# PatchedOrganizationUser

Read roles out of a mapping preloaded by the list serializer.  ``preloaded_roles`` holds the roles of every object being serialized while a list is serialized, and stays None when a single object is serialized, in which case every role is looked up on its own.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] [readonly]
**email** | **str** |  | [optional] [readonly]
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional]
**has_mfa_device** | **bool** |  | [optional] [readonly]
**name** | **str** |  | [optional]
**roles** | [**Dict[str, UserRoleObject]**](UserRoleObject.md) | Roles in the organization. | [optional] [readonly]
**is_support** | **bool** | Designates whether this user should be treated as a support. | [optional] [readonly]

## Example

```python
from gencove_client.models.patched_organization_user import PatchedOrganizationUser

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedOrganizationUser from a JSON string
patched_organization_user_instance = PatchedOrganizationUser.from_json(json)
# print the JSON string representation of the object
print(PatchedOrganizationUser.to_json())

# convert the object into a dict
patched_organization_user_dict = patched_organization_user_instance.to_dict()
# create an instance of PatchedOrganizationUser from a dict
patched_organization_user_from_dict = PatchedOrganizationUser.from_dict(patched_organization_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
