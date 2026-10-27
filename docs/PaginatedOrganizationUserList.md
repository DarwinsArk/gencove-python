# PaginatedOrganizationUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[OrganizationUser]**](OrganizationUser.md) |  |

## Example

```python
from gencove_client.models.paginated_organization_user_list import PaginatedOrganizationUserList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOrganizationUserList from a JSON string
paginated_organization_user_list_instance = PaginatedOrganizationUserList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOrganizationUserList.to_json())

# convert the object into a dict
paginated_organization_user_list_dict = paginated_organization_user_list_instance.to_dict()
# create an instance of PaginatedOrganizationUserList from a dict
paginated_organization_user_list_from_dict = PaginatedOrganizationUserList.from_dict(paginated_organization_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
