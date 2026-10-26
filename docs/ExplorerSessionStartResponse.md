# ExplorerSessionStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explorer_url** | **str** | Clean Explorer URL to open after the session cookie is set. |
**expires_in** | **int** | Explorer session duration in seconds. |

## Example

```python
from gencove_client.models.explorer_session_start_response import ExplorerSessionStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerSessionStartResponse from a JSON string
explorer_session_start_response_instance = ExplorerSessionStartResponse.from_json(json)
# print the JSON string representation of the object
print(ExplorerSessionStartResponse.to_json())

# convert the object into a dict
explorer_session_start_response_dict = explorer_session_start_response_instance.to_dict()
# create an instance of ExplorerSessionStartResponse from a dict
explorer_session_start_response_from_dict = ExplorerSessionStartResponse.from_dict(explorer_session_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
