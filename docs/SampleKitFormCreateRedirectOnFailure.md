# SampleKitFormCreateRedirectOnFailure

URL the end-user is redirected to when an order they opened a link for cannot be placed, with a ``reason`` query parameter appended (link_replaced, already_ordered, project_locked or ordering_not_configured). Omit to send them to a generic Gencove-hosted error page. Failures Gencove cannot attribute to an order link, such as an unreadable or expired link, always use the hosted page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from gencove_client.models.sample_kit_form_create_redirect_on_failure import SampleKitFormCreateRedirectOnFailure

# TODO update the JSON string below
json = "{}"
# create an instance of SampleKitFormCreateRedirectOnFailure from a JSON string
sample_kit_form_create_redirect_on_failure_instance = SampleKitFormCreateRedirectOnFailure.from_json(json)
# print the JSON string representation of the object
print(SampleKitFormCreateRedirectOnFailure.to_json())

# convert the object into a dict
sample_kit_form_create_redirect_on_failure_dict = sample_kit_form_create_redirect_on_failure_instance.to_dict()
# create an instance of SampleKitFormCreateRedirectOnFailure from a dict
sample_kit_form_create_redirect_on_failure_from_dict = SampleKitFormCreateRedirectOnFailure.from_dict(sample_kit_form_create_redirect_on_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
