# PaginatedExplorerInstanceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[ExplorerInstance]**](ExplorerInstance.md) |  |

## Example

```python
from gencove_client.models.paginated_explorer_instance_list import PaginatedExplorerInstanceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedExplorerInstanceList from a JSON string
paginated_explorer_instance_list_instance = PaginatedExplorerInstanceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedExplorerInstanceList.to_json())

# convert the object into a dict
paginated_explorer_instance_list_dict = paginated_explorer_instance_list_instance.to_dict()
# create an instance of PaginatedExplorerInstanceList from a dict
paginated_explorer_instance_list_from_dict = PaginatedExplorerInstanceList.from_dict(paginated_explorer_instance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
