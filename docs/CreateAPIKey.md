# CreateAPIKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **date** | Last day (UTC) to use the API key, once API key expires clients cannot use it anymore. | [optional]
**id** | **str** |  | [optional] [readonly]
**key** | **str** |  | [optional] [readonly]
**name** | **str** | A free-form name for the API key. Need not be unique. 50 characters max. |
**prefix** | **str** |  | [optional] [readonly]
**ip_range** | **object** | List of trusted subnets in CIDR notation | [optional]

## Example

```python
from gencove_client.models.create_api_key import CreateAPIKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPIKey from a JSON string
create_api_key_instance = CreateAPIKey.from_json(json)
# print the JSON string representation of the object
print(CreateAPIKey.to_json())

# convert the object into a dict
create_api_key_dict = create_api_key_instance.to_dict()
# create an instance of CreateAPIKey from a dict
create_api_key_from_dict = CreateAPIKey.from_dict(create_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
