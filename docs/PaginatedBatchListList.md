# PaginatedBatchListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[BatchList]**](BatchList.md) |  |

## Example

```python
from gencove_client.models.paginated_batch_list_list import PaginatedBatchListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBatchListList from a JSON string
paginated_batch_list_list_instance = PaginatedBatchListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBatchListList.to_json())

# convert the object into a dict
paginated_batch_list_list_dict = paginated_batch_list_list_instance.to_dict()
# create an instance of PaginatedBatchListList from a dict
paginated_batch_list_list_from_dict = PaginatedBatchListList.from_dict(paginated_batch_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
