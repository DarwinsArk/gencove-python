# SampleKitFormCreateRedirectOnSuccess

URL the end-user is redirected to after a successful order. Omit to send them to a generic Gencove-hosted confirmation page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from gencove_client.models.sample_kit_form_create_redirect_on_success import SampleKitFormCreateRedirectOnSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of SampleKitFormCreateRedirectOnSuccess from a JSON string
sample_kit_form_create_redirect_on_success_instance = SampleKitFormCreateRedirectOnSuccess.from_json(json)
# print the JSON string representation of the object
print(SampleKitFormCreateRedirectOnSuccess.to_json())

# convert the object into a dict
sample_kit_form_create_redirect_on_success_dict = sample_kit_form_create_redirect_on_success_instance.to_dict()
# create an instance of SampleKitFormCreateRedirectOnSuccess from a dict
sample_kit_form_create_redirect_on_success_from_dict = SampleKitFormCreateRedirectOnSuccess.from_dict(sample_kit_form_create_redirect_on_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
