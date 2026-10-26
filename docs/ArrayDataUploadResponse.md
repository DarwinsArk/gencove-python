# ArrayDataUploadResponse

Response body for ``POST /api/v2/array-data-upload``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_id** | **UUID** | UUID of the &#x60;&#x60;samples.Sample&#x60;&#x60; created for this upload. Use it to track status and retrieve results. |
**upload_url** | **str** | POST the file here as multipart/form-data. |
**upload_fields** | **Dict[str, str]** | Send every key/value in this object as a form field, then the file itself as a field named &#x60;file&#x60; — which MUST be the last field in the multipart body. Send these back exactly as received; do not add, rename, drop or reorder them. |
**file_field_name** | **str** | Name of the multipart field carrying the file. Always &#x60;file&#x60;. |
**expires_at** | **datetime** | When this upload stops being accepted (ISO-8601, UTC). After this, request a new upload. |
**max_file_size_bytes** | **int** | Maximum accepted file size. Larger uploads are rejected outright. |
**content_type** | **str** | The only accepted content type. Already prefilled in &#x60;upload_fields&#x60;. |

## Example

```python
from gencove_client.models.array_data_upload_response import ArrayDataUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayDataUploadResponse from a JSON string
array_data_upload_response_instance = ArrayDataUploadResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayDataUploadResponse.to_json())

# convert the object into a dict
array_data_upload_response_dict = array_data_upload_response_instance.to_dict()
# create an instance of ArrayDataUploadResponse from a dict
array_data_upload_response_from_dict = ArrayDataUploadResponse.from_dict(array_data_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
