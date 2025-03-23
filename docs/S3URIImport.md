# S3URIImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_uri** | **str** |  |
**project_id** | **str** |  |
**metadata** | **object** |  | [optional]

## Example

```python
from gencove_client.models.s3_uri_import import S3URIImport

# TODO update the JSON string below
json = "{}"
# create an instance of S3URIImport from a JSON string
s3_uri_import_instance = S3URIImport.from_json(json)
# print the JSON string representation of the object
print(S3URIImport.to_json())

# convert the object into a dict
s3_uri_import_dict = s3_uri_import_instance.to_dict()
# create an instance of S3URIImport from a dict
s3_uri_import_from_dict = S3URIImport.from_dict(s3_uri_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
