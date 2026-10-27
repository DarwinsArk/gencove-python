# PatchedAPIKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revoked** | **bool** | If the API key is revoked, clients cannot use it anymore. (This cannot be undone.) | [optional]
**id** | **str** |  | [optional]
**name** | **str** | A free-form name for the API key. Need not be unique. 50 characters max. | [optional]
**prefix** | **str** |  | [optional] [readonly]
**expiry_date** | **date** | Last day (UTC) to use the API key, once API key expires clients cannot use it anymore. | [optional] [readonly]
**has_expired** | **str** |  | [optional] [readonly]
**ip_range** | **object** | List of trusted subnets in CIDR notation | [optional]

## Example

```python
from gencove_client.models.patched_api_key import PatchedAPIKey

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAPIKey from a JSON string
patched_api_key_instance = PatchedAPIKey.from_json(json)
# print the JSON string representation of the object
print(PatchedAPIKey.to_json())

# convert the object into a dict
patched_api_key_dict = patched_api_key_instance.to_dict()
# create an instance of PatchedAPIKey from a dict
patched_api_key_from_dict = PatchedAPIKey.from_dict(patched_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
