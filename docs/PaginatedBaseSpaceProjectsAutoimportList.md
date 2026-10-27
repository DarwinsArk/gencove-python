# PaginatedBaseSpaceProjectsAutoimportList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[BaseSpaceProjectsAutoimport]**](BaseSpaceProjectsAutoimport.md) |  |

## Example

```python
from gencove_client.models.paginated_base_space_projects_autoimport_list import PaginatedBaseSpaceProjectsAutoimportList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBaseSpaceProjectsAutoimportList from a JSON string
paginated_base_space_projects_autoimport_list_instance = PaginatedBaseSpaceProjectsAutoimportList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBaseSpaceProjectsAutoimportList.to_json())

# convert the object into a dict
paginated_base_space_projects_autoimport_list_dict = paginated_base_space_projects_autoimport_list_instance.to_dict()
# create an instance of PaginatedBaseSpaceProjectsAutoimportList from a dict
paginated_base_space_projects_autoimport_list_from_dict = PaginatedBaseSpaceProjectsAutoimportList.from_dict(paginated_base_space_projects_autoimport_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
