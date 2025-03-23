# UploadsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[Upload]**](Upload.md) |  |

## Example

```python
from gencove_client.models.uploads_list200_response import UploadsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UploadsList200Response from a JSON string
uploads_list200_response_instance = UploadsList200Response.from_json(json)
# print the JSON string representation of the object
print(UploadsList200Response.to_json())

# convert the object into a dict
uploads_list200_response_dict = uploads_list200_response_instance.to_dict()
# create an instance of UploadsList200Response from a dict
uploads_list200_response_from_dict = UploadsList200Response.from_dict(uploads_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
