# ProjectQualityControlHistogram


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_edges** | **List[float]** |  |
**hist** | **List[float]** |  |

## Example

```python
from gencove_client.models.project_quality_control_histogram import ProjectQualityControlHistogram

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectQualityControlHistogram from a JSON string
project_quality_control_histogram_instance = ProjectQualityControlHistogram.from_json(json)
# print the JSON string representation of the object
print(ProjectQualityControlHistogram.to_json())

# convert the object into a dict
project_quality_control_histogram_dict = project_quality_control_histogram_instance.to_dict()
# create an instance of ProjectQualityControlHistogram from a dict
project_quality_control_histogram_from_dict = ProjectQualityControlHistogram.from_dict(project_quality_control_histogram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
