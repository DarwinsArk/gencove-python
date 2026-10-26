# PaginatedProjectShareList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[ProjectShare]**](ProjectShare.md) |  |

## Example

```python
from gencove_client.models.paginated_project_share_list import PaginatedProjectShareList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProjectShareList from a JSON string
paginated_project_share_list_instance = PaginatedProjectShareList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProjectShareList.to_json())

# convert the object into a dict
paginated_project_share_list_dict = paginated_project_share_list_instance.to_dict()
# create an instance of PaginatedProjectShareList from a dict
paginated_project_share_list_from_dict = PaginatedProjectShareList.from_dict(paginated_project_share_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
