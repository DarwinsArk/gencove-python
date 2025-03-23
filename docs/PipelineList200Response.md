# PipelineList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[PipelineList]**](PipelineList.md) |  |

## Example

```python
from gencove_client.models.pipeline_list200_response import PipelineList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineList200Response from a JSON string
pipeline_list200_response_instance = PipelineList200Response.from_json(json)
# print the JSON string representation of the object
print(PipelineList200Response.to_json())

# convert the object into a dict
pipeline_list200_response_dict = pipeline_list200_response_instance.to_dict()
# create an instance of PipelineList200Response from a dict
pipeline_list200_response_from_dict = PipelineList200Response.from_dict(pipeline_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
