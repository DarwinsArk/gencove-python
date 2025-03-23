# ExplorerShellSessionCredentialsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  |
**access_key** | **str** |  |
**secret_key** | **str** |  |
**token** | **str** |  |
**expiry_time** | **datetime** |  |
**region_name** | **str** |  |
**ec2_instance_id** | **str** |  |
**shell_session_ssm_document_name** | **str** |  |
**network_activity_ssm_document_name** | **str** |  |

## Example

```python
from gencove_client.models.explorer_shell_session_credentials_response import ExplorerShellSessionCredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerShellSessionCredentialsResponse from a JSON string
explorer_shell_session_credentials_response_instance = ExplorerShellSessionCredentialsResponse.from_json(json)
# print the JSON string representation of the object
print(ExplorerShellSessionCredentialsResponse.to_json())

# convert the object into a dict
explorer_shell_session_credentials_response_dict = explorer_shell_session_credentials_response_instance.to_dict()
# create an instance of ExplorerShellSessionCredentialsResponse from a dict
explorer_shell_session_credentials_response_from_dict = ExplorerShellSessionCredentialsResponse.from_dict(explorer_shell_session_credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
