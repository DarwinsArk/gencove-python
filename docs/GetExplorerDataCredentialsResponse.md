# GetExplorerDataCredentialsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  |
**access_key** | **str** |  |
**secret_key** | **str** |  |
**token** | **str** |  |
**expiry_time** | **datetime** |  |
**region_name** | **str** |  |

## Example

```python
from gencove_client.models.get_explorer_data_credentials_response import GetExplorerDataCredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExplorerDataCredentialsResponse from a JSON string
get_explorer_data_credentials_response_instance = GetExplorerDataCredentialsResponse.from_json(json)
# print the JSON string representation of the object
print(GetExplorerDataCredentialsResponse.to_json())

# convert the object into a dict
get_explorer_data_credentials_response_dict = get_explorer_data_credentials_response_instance.to_dict()
# create an instance of GetExplorerDataCredentialsResponse from a dict
get_explorer_data_credentials_response_from_dict = GetExplorerDataCredentialsResponse.from_dict(get_explorer_data_credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
