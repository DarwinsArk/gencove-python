# APIKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revoked** | **bool** | If the API key is revoked, clients cannot use it anymore. (This cannot be undone.) | [optional]
**id** | **str** |  |
**name** | **str** | A free-form name for the API key. Need not be unique. 50 characters max. |
**prefix** | **str** |  | [optional] [readonly]
**expiry_date** | **date** | Last day (UTC) to use the API key, once API key expires clients cannot use it anymore. | [optional] [readonly]
**has_expired** | **str** |  | [optional] [readonly]
**ip_range** | **object** | List of trusted subnets in CIDR notation | [optional]

## Example

```python
from gencove_client.models.api_key import APIKey

# TODO update the JSON string below
json = "{}"
# create an instance of APIKey from a JSON string
api_key_instance = APIKey.from_json(json)
# print the JSON string representation of the object
print(APIKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of APIKey from a dict
api_key_from_dict = APIKey.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
