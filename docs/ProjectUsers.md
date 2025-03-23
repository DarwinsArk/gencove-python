# ProjectUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**email** | **str** |  | [optional] [readonly]
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional]
**name** | **str** |  | [optional]
**roles** | [**Dict[str, UserRoleObject]**](UserRoleObject.md) | Roles for the project in the organization. | [optional] [readonly]
**is_support** | **bool** | Designates whether this user should be treated as a support. | [optional] [readonly]

## Example

```python
from gencove_client.models.project_users import ProjectUsers

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUsers from a JSON string
project_users_instance = ProjectUsers.from_json(json)
# print the JSON string representation of the object
print(ProjectUsers.to_json())

# convert the object into a dict
project_users_dict = project_users_instance.to_dict()
# create an instance of ProjectUsers from a dict
project_users_from_dict = ProjectUsers.from_dict(project_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
