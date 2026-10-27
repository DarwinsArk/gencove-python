# PaginatedBatchTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[BatchType]**](BatchType.md) |  |

## Example

```python
from gencove_client.models.paginated_batch_type_list import PaginatedBatchTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBatchTypeList from a JSON string
paginated_batch_type_list_instance = PaginatedBatchTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBatchTypeList.to_json())

# convert the object into a dict
paginated_batch_type_list_dict = paginated_batch_type_list_instance.to_dict()
# create an instance of PaginatedBatchTypeList from a dict
paginated_batch_type_list_from_dict = PaginatedBatchTypeList.from_dict(paginated_batch_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
