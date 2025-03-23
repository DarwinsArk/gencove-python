# ProjectBatchesRead200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[BatchList]**](BatchList.md) |  |

## Example

```python
from gencove_client.models.project_batches_read200_response import ProjectBatchesRead200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBatchesRead200Response from a JSON string
project_batches_read200_response_instance = ProjectBatchesRead200Response.from_json(json)
# print the JSON string representation of the object
print(ProjectBatchesRead200Response.to_json())

# convert the object into a dict
project_batches_read200_response_dict = project_batches_read200_response_instance.to_dict()
# create an instance of ProjectBatchesRead200Response from a dict
project_batches_read200_response_from_dict = ProjectBatchesRead200Response.from_dict(project_batches_read200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
