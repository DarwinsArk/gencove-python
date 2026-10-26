# PaginatedAPIKeyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[APIKey]**](APIKey.md) |  |

## Example

```python
from gencove_client.models.paginated_api_key_list import PaginatedAPIKeyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAPIKeyList from a JSON string
paginated_api_key_list_instance = PaginatedAPIKeyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAPIKeyList.to_json())

# convert the object into a dict
paginated_api_key_list_dict = paginated_api_key_list_instance.to_dict()
# create an instance of PaginatedAPIKeyList from a dict
paginated_api_key_list_from_dict = PaginatedAPIKeyList.from_dict(paginated_api_key_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
