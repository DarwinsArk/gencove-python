# ArrayDataUploadFormCreate

Request body for ``POST /api/v2/array-data-upload-form``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** | Optional UUID of the project the uploaded sample should land in. When omitted, the sample falls back to the organization&#39;s consumer array-data project. | [optional]
**metadata** | **object** | Free-form JSON object. | [optional]
**redirect_on_success** | [**ArrayDataUploadFormCreateRedirectOnSuccess**](ArrayDataUploadFormCreateRedirectOnSuccess.md) |  | [optional]
**redirect_on_failure** | [**ArrayDataUploadFormCreateRedirectOnFailure**](ArrayDataUploadFormCreateRedirectOnFailure.md) |  | [optional]
**expires_in** | **int** | JWT lifetime in seconds (default 600, max 3600). Once the URL is opened, a 15-minute session is created that may outlive this token. | [optional] [default to 600]

## Example

```python
from gencove_client.models.array_data_upload_form_create import ArrayDataUploadFormCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayDataUploadFormCreate from a JSON string
array_data_upload_form_create_instance = ArrayDataUploadFormCreate.from_json(json)
# print the JSON string representation of the object
print(ArrayDataUploadFormCreate.to_json())

# convert the object into a dict
array_data_upload_form_create_dict = array_data_upload_form_create_instance.to_dict()
# create an instance of ArrayDataUploadFormCreate from a dict
array_data_upload_form_create_from_dict = ArrayDataUploadFormCreate.from_dict(array_data_upload_form_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
