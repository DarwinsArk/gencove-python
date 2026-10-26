# PaginatedS3URIAutoimportList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[S3URIAutoimport]**](S3URIAutoimport.md) |  |

## Example

```python
from gencove_client.models.paginated_s3_uri_autoimport_list import PaginatedS3URIAutoimportList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedS3URIAutoimportList from a JSON string
paginated_s3_uri_autoimport_list_instance = PaginatedS3URIAutoimportList.from_json(json)
# print the JSON string representation of the object
print(PaginatedS3URIAutoimportList.to_json())

# convert the object into a dict
paginated_s3_uri_autoimport_list_dict = paginated_s3_uri_autoimport_list_instance.to_dict()
# create an instance of PaginatedS3URIAutoimportList from a dict
paginated_s3_uri_autoimport_list_from_dict = PaginatedS3URIAutoimportList.from_dict(paginated_s3_uri_autoimport_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
