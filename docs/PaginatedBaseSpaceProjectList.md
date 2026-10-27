# PaginatedBaseSpaceProjectList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[BaseSpaceProject]**](BaseSpaceProject.md) |  |

## Example

```python
from gencove_client.models.paginated_base_space_project_list import PaginatedBaseSpaceProjectList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBaseSpaceProjectList from a JSON string
paginated_base_space_project_list_instance = PaginatedBaseSpaceProjectList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBaseSpaceProjectList.to_json())

# convert the object into a dict
paginated_base_space_project_list_dict = paginated_base_space_project_list_instance.to_dict()
# create an instance of PaginatedBaseSpaceProjectList from a dict
paginated_base_space_project_list_from_dict = PaginatedBaseSpaceProjectList.from_dict(paginated_base_space_project_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
