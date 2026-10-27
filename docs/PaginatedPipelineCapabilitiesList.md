# PaginatedPipelineCapabilitiesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[PipelineCapabilities]**](PipelineCapabilities.md) |  |

## Example

```python
from gencove_client.models.paginated_pipeline_capabilities_list import PaginatedPipelineCapabilitiesList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPipelineCapabilitiesList from a JSON string
paginated_pipeline_capabilities_list_instance = PaginatedPipelineCapabilitiesList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPipelineCapabilitiesList.to_json())

# convert the object into a dict
paginated_pipeline_capabilities_list_dict = paginated_pipeline_capabilities_list_instance.to_dict()
# create an instance of PaginatedPipelineCapabilitiesList from a dict
paginated_pipeline_capabilities_list_from_dict = PaginatedPipelineCapabilitiesList.from_dict(paginated_pipeline_capabilities_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
