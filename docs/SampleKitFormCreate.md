# SampleKitFormCreate

Request body for ``POST /api/v2/sample-kit-form/``.  Mirrors ``ArrayDataUploadFormCreateSerializer`` but is project-scoped: the partner names the consumer project the kit's sample lands in. The end user supplies the shipping address later, in the form itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** | UUID of the consumer project to create the kit order in. |
**metadata** | **object** | Free-form JSON object stored on the created sample. | [optional]
**test_mode** | **bool** | Set to true to create a test order that will not be shipped. Defaults to false. | [optional] [default to False]
**redirect_on_success** | [**SampleKitFormCreateRedirectOnSuccess**](SampleKitFormCreateRedirectOnSuccess.md) |  | [optional]
**redirect_on_failure** | [**SampleKitFormCreateRedirectOnFailure**](SampleKitFormCreateRedirectOnFailure.md) |  | [optional]
**expires_in** | **int** | JWT lifetime in seconds (default 600, max 3600). Once the URL is opened, a 15-minute session is created that may outlive this token. | [optional] [default to 600]

## Example

```python
from gencove_client.models.sample_kit_form_create import SampleKitFormCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SampleKitFormCreate from a JSON string
sample_kit_form_create_instance = SampleKitFormCreate.from_json(json)
# print the JSON string representation of the object
print(SampleKitFormCreate.to_json())

# convert the object into a dict
sample_kit_form_create_dict = sample_kit_form_create_instance.to_dict()
# create an instance of SampleKitFormCreate from a dict
sample_kit_form_create_from_dict = SampleKitFormCreate.from_dict(sample_kit_form_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
