# PaginatedPipelineListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[PipelineList]**](PipelineList.md) |  |

## Example

```python
from gencove_client.models.paginated_pipeline_list_list import PaginatedPipelineListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPipelineListList from a JSON string
paginated_pipeline_list_list_instance = PaginatedPipelineListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPipelineListList.to_json())

# convert the object into a dict
paginated_pipeline_list_list_dict = paginated_pipeline_list_list_instance.to_dict()
# create an instance of PaginatedPipelineListList from a dict
paginated_pipeline_list_list_from_dict = PaginatedPipelineListList.from_dict(paginated_pipeline_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
