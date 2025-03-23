# ProjectBatchTypesRead200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[BatchType]**](BatchType.md) |  |

## Example

```python
from gencove_client.models.project_batch_types_read200_response import ProjectBatchTypesRead200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBatchTypesRead200Response from a JSON string
project_batch_types_read200_response_instance = ProjectBatchTypesRead200Response.from_json(json)
# print the JSON string representation of the object
print(ProjectBatchTypesRead200Response.to_json())

# convert the object into a dict
project_batch_types_read200_response_dict = project_batch_types_read200_response_instance.to_dict()
# create an instance of ProjectBatchTypesRead200Response from a dict
project_batch_types_read200_response_from_dict = ProjectBatchTypesRead200Response.from_dict(project_batch_types_read200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
