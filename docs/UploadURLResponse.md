# UploadURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**destination_path** | **str** |  | [optional]
**s3** | [**S3ObjectNested**](S3ObjectNested.md) |  | [optional]
**last_status** | [**UploadStatusNested**](UploadStatusNested.md) |  | [optional]
**source** | **str** |  |
**source_url** | **str** |  | [optional] [readonly]

## Example

```python
from gencove_client.models.upload_url_response import UploadURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadURLResponse from a JSON string
upload_url_response_instance = UploadURLResponse.from_json(json)
# print the JSON string representation of the object
print(UploadURLResponse.to_json())

# convert the object into a dict
upload_url_response_dict = upload_url_response_instance.to_dict()
# create an instance of UploadURLResponse from a dict
upload_url_response_from_dict = UploadURLResponse.from_dict(upload_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
