# ArrayDataUploadCreate

Request body for ``POST /api/v2/array-data-upload``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** | Optional UUID of the project the uploaded sample should land in. When omitted, the sample falls back to the organization&#39;s consumer array-data project. | [optional]
**metadata** | **object** | Free-form JSON object. | [optional]

## Example

```python
from gencove_client.models.array_data_upload_create import ArrayDataUploadCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayDataUploadCreate from a JSON string
array_data_upload_create_instance = ArrayDataUploadCreate.from_json(json)
# print the JSON string representation of the object
print(ArrayDataUploadCreate.to_json())

# convert the object into a dict
array_data_upload_create_dict = array_data_upload_create_instance.to_dict()
# create an instance of ArrayDataUploadCreate from a dict
array_data_upload_create_from_dict = ArrayDataUploadCreate.from_dict(array_data_upload_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
