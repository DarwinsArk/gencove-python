# GetUploadCredentialsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  |
**access_key** | **str** |  |
**secret_key** | **str** |  |
**token** | **str** |  |
**expiry_time** | **datetime** |  |

## Example

```python
from gencove_client.models.get_upload_credentials_response import GetUploadCredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUploadCredentialsResponse from a JSON string
get_upload_credentials_response_instance = GetUploadCredentialsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUploadCredentialsResponse.to_json())

# convert the object into a dict
get_upload_credentials_response_dict = get_upload_credentials_response_instance.to_dict()
# create an instance of GetUploadCredentialsResponse from a dict
get_upload_credentials_response_from_dict = GetUploadCredentialsResponse.from_dict(get_upload_credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
