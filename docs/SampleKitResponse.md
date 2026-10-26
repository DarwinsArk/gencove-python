# SampleKitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_id** | **UUID** |  | [readonly]

## Example

```python
from gencove_client.models.sample_kit_response import SampleKitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SampleKitResponse from a JSON string
sample_kit_response_instance = SampleKitResponse.from_json(json)
# print the JSON string representation of the object
print(SampleKitResponse.to_json())

# convert the object into a dict
sample_kit_response_dict = sample_kit_response_instance.to_dict()
# create an instance of SampleKitResponse from a dict
sample_kit_response_from_dict = SampleKitResponse.from_dict(sample_kit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
