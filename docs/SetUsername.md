# SetUsername


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** |  |
**new_email** | **str** |  |

## Example

```python
from gencove_client.models.set_username import SetUsername

# TODO update the JSON string below
json = "{}"
# create an instance of SetUsername from a JSON string
set_username_instance = SetUsername.from_json(json)
# print the JSON string representation of the object
print(SetUsername.to_json())

# convert the object into a dict
set_username_dict = set_username_instance.to_dict()
# create an instance of SetUsername from a dict
set_username_from_dict = SetUsername.from_dict(set_username_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
