# PaginatedUploadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[Upload]**](Upload.md) |  |

## Example

```python
from gencove_client.models.paginated_upload_list import PaginatedUploadList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUploadList from a JSON string
paginated_upload_list_instance = PaginatedUploadList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUploadList.to_json())

# convert the object into a dict
paginated_upload_list_dict = paginated_upload_list_instance.to_dict()
# create an instance of PaginatedUploadList from a dict
paginated_upload_list_from_dict = PaginatedUploadList.from_dict(paginated_upload_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
