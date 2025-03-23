# SampleQualityControlsRead200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[QualityControl]**](QualityControl.md) |  |

## Example

```python
from gencove_client.models.sample_quality_controls_read200_response import SampleQualityControlsRead200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SampleQualityControlsRead200Response from a JSON string
sample_quality_controls_read200_response_instance = SampleQualityControlsRead200Response.from_json(json)
# print the JSON string representation of the object
print(SampleQualityControlsRead200Response.to_json())

# convert the object into a dict
sample_quality_controls_read200_response_dict = sample_quality_controls_read200_response_instance.to_dict()
# create an instance of SampleQualityControlsRead200Response from a dict
sample_quality_controls_read200_response_from_dict = SampleQualityControlsRead200Response.from_dict(sample_quality_controls_read200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
