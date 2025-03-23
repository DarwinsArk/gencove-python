# S3URIAutoimport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**project_id** | **str** |  |
**s3_uri** | **str** |  |
**metadata** | **object** |  | [optional]

## Example

```python
from gencove_client.models.s3_uri_autoimport import S3URIAutoimport

# TODO update the JSON string below
json = "{}"
# create an instance of S3URIAutoimport from a JSON string
s3_uri_autoimport_instance = S3URIAutoimport.from_json(json)
# print the JSON string representation of the object
print(S3URIAutoimport.to_json())

# convert the object into a dict
s3_uri_autoimport_dict = s3_uri_autoimport_instance.to_dict()
# create an instance of S3URIAutoimport from a dict
s3_uri_autoimport_from_dict = S3URIAutoimport.from_dict(s3_uri_autoimport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
