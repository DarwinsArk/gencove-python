# PaginatedAPIKeyListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  |
**next** | **str** |  | [optional]
**previous** | **str** |  | [optional]

## Example

```python
from gencove_client.models.paginated_api_key_list_meta import PaginatedAPIKeyListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAPIKeyListMeta from a JSON string
paginated_api_key_list_meta_instance = PaginatedAPIKeyListMeta.from_json(json)
# print the JSON string representation of the object
print(PaginatedAPIKeyListMeta.to_json())

# convert the object into a dict
paginated_api_key_list_meta_dict = paginated_api_key_list_meta_instance.to_dict()
# create an instance of PaginatedAPIKeyListMeta from a dict
paginated_api_key_list_meta_from_dict = PaginatedAPIKeyListMeta.from_dict(paginated_api_key_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
