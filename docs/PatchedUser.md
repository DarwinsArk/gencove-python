# PatchedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] [readonly]
**email** | **str** |  | [optional] [readonly]
**name** | **str** |  | [optional]
**uploads_enabled** | **str** |  | [optional] [readonly]
**explorer_enabled** | **str** |  | [optional] [readonly]
**created** | **datetime** |  | [optional] [readonly]
**is_support** | **bool** | Designates whether this user should be treated as a support. | [optional] [readonly]

## Example

```python
from gencove_client.models.patched_user import PatchedUser

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUser from a JSON string
patched_user_instance = PatchedUser.from_json(json)
# print the JSON string representation of the object
print(PatchedUser.to_json())

# convert the object into a dict
patched_user_dict = patched_user_instance.to_dict()
# create an instance of PatchedUser from a dict
patched_user_from_dict = PatchedUser.from_dict(patched_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
