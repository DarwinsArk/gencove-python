# PipelineDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**version** | **str** |  |
**capabilities** | [**List[PipelineCapabilities]**](PipelineCapabilities.md) |  |

## Example

```python
from gencove_client.models.pipeline_detail import PipelineDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineDetail from a JSON string
pipeline_detail_instance = PipelineDetail.from_json(json)
# print the JSON string representation of the object
print(PipelineDetail.to_json())

# convert the object into a dict
pipeline_detail_dict = pipeline_detail_instance.to_dict()
# create an instance of PipelineDetail from a dict
pipeline_detail_from_dict = PipelineDetail.from_dict(pipeline_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
