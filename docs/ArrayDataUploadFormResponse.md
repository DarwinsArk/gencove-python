# ArrayDataUploadFormResponse

Response body for ``POST /api/v2/array-data-upload-form``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_id** | **UUID** | UUID of the &#x60;&#x60;samples.Sample&#x60;&#x60; created for this upload session. |
**url** | **str** | Tokenized upload URL for the end-user. |
**expires_at** | **datetime** | When the embedded JWT expires (ISO-8601). |

## Example

```python
from gencove_client.models.array_data_upload_form_response import ArrayDataUploadFormResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayDataUploadFormResponse from a JSON string
array_data_upload_form_response_instance = ArrayDataUploadFormResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayDataUploadFormResponse.to_json())

# convert the object into a dict
array_data_upload_form_response_dict = array_data_upload_form_response_instance.to_dict()
# create an instance of ArrayDataUploadFormResponse from a dict
array_data_upload_form_response_from_dict = ArrayDataUploadFormResponse.from_dict(array_data_upload_form_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
