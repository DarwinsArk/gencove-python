# PaginatedProjectUsersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[ProjectUsers]**](ProjectUsers.md) |  |

## Example

```python
from gencove_client.models.paginated_project_users_list import PaginatedProjectUsersList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProjectUsersList from a JSON string
paginated_project_users_list_instance = PaginatedProjectUsersList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProjectUsersList.to_json())

# convert the object into a dict
paginated_project_users_list_dict = paginated_project_users_list_instance.to_dict()
# create an instance of PaginatedProjectUsersList from a dict
paginated_project_users_list_from_dict = PaginatedProjectUsersList.from_dict(paginated_project_users_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
