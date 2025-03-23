# OrganizationUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**email** | **str** |  | [optional] [readonly]
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional]
**has_mfa_device** | **bool** |  | [optional] [readonly]
**name** | **str** |  | [optional]
**roles** | [**Dict[str, UserRoleObject]**](UserRoleObject.md) | Roles in the organization. | [optional] [readonly]
**is_support** | **bool** | Designates whether this user should be treated as a support. | [optional] [readonly]

## Example

```python
from gencove_client.models.organization_user import OrganizationUser

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUser from a JSON string
organization_user_instance = OrganizationUser.from_json(json)
# print the JSON string representation of the object
print(OrganizationUser.to_json())

# convert the object into a dict
organization_user_dict = organization_user_instance.to_dict()
# create an instance of OrganizationUser from a dict
organization_user_from_dict = OrganizationUser.from_dict(organization_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
