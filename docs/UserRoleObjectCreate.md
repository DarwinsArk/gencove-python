# UserRoleObjectCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  |
**role** | **str** |  |

## Example

```python
from gencove_client.models.user_role_object_create import UserRoleObjectCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleObjectCreate from a JSON string
user_role_object_create_instance = UserRoleObjectCreate.from_json(json)
# print the JSON string representation of the object
print(UserRoleObjectCreate.to_json())

# convert the object into a dict
user_role_object_create_dict = user_role_object_create_instance.to_dict()
# create an instance of UserRoleObjectCreate from a dict
user_role_object_create_from_dict = UserRoleObjectCreate.from_dict(user_role_object_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
