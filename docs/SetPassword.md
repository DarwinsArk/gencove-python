# SetPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** |  |
**current_password** | **str** |  |

## Example

```python
from gencove_client.models.set_password import SetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of SetPassword from a JSON string
set_password_instance = SetPassword.from_json(json)
# print the JSON string representation of the object
print(SetPassword.to_json())

# convert the object into a dict
set_password_dict = set_password_instance.to_dict()
# create an instance of SetPassword from a dict
set_password_from_dict = SetPassword.from_dict(set_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
