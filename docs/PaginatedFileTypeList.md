# PaginatedFileTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[FileType]**](FileType.md) |  |

## Example

```python
from gencove_client.models.paginated_file_type_list import PaginatedFileTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFileTypeList from a JSON string
paginated_file_type_list_instance = PaginatedFileTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFileTypeList.to_json())

# convert the object into a dict
paginated_file_type_list_dict = paginated_file_type_list_instance.to_dict()
# create an instance of PaginatedFileTypeList from a dict
paginated_file_type_list_from_dict = PaginatedFileTypeList.from_dict(paginated_file_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
