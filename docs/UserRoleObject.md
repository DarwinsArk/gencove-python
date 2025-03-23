# UserRoleObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**name** | **str** |  |

## Example

```python
from gencove_client.models.user_role_object import UserRoleObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleObject from a JSON string
user_role_object_instance = UserRoleObject.from_json(json)
# print the JSON string representation of the object
print(UserRoleObject.to_json())

# convert the object into a dict
user_role_object_dict = user_role_object_instance.to_dict()
# create an instance of UserRoleObject from a dict
user_role_object_from_dict = UserRoleObject.from_dict(user_role_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
