# PasswordResetConfirm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  |
**token** | **str** |  |
**new_password** | **str** |  |

## Example

```python
from gencove_client.models.password_reset_confirm import PasswordResetConfirm

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordResetConfirm from a JSON string
password_reset_confirm_instance = PasswordResetConfirm.from_json(json)
# print the JSON string representation of the object
print(PasswordResetConfirm.to_json())

# convert the object into a dict
password_reset_confirm_dict = password_reset_confirm_instance.to_dict()
# create an instance of PasswordResetConfirm from a dict
password_reset_confirm_from_dict = PasswordResetConfirm.from_dict(password_reset_confirm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
