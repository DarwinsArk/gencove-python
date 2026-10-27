# SampleKitFormResponse

Response body for ``POST /api/v2/sample-kit-form/``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_id** | **UUID** | UUID of the placeholder &#x60;&#x60;samples.Sample&#x60;&#x60; created for the order. |
**url** | **str** | Tokenized kit-order form URL for the end-user. |
**expires_at** | **datetime** | When the embedded JWT expires (ISO-8601). |

## Example

```python
from gencove_client.models.sample_kit_form_response import SampleKitFormResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SampleKitFormResponse from a JSON string
sample_kit_form_response_instance = SampleKitFormResponse.from_json(json)
# print the JSON string representation of the object
print(SampleKitFormResponse.to_json())

# convert the object into a dict
sample_kit_form_response_dict = sample_kit_form_response_instance.to_dict()
# create an instance of SampleKitFormResponse from a dict
sample_kit_form_response_from_dict = SampleKitFormResponse.from_dict(sample_kit_form_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
