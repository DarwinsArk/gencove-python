# UploadPostDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**destination_path** | **str** |  | [optional]
**s3** | [**S3ObjectNested**](S3ObjectNested.md) |  | [optional]
**last_status** | [**UploadStatusNested**](UploadStatusNested.md) |  | [optional]

## Example

```python
from gencove_client.models.upload_post_data_response import UploadPostDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPostDataResponse from a JSON string
upload_post_data_response_instance = UploadPostDataResponse.from_json(json)
# print the JSON string representation of the object
print(UploadPostDataResponse.to_json())

# convert the object into a dict
upload_post_data_response_dict = upload_post_data_response_instance.to_dict()
# create an instance of UploadPostDataResponse from a dict
upload_post_data_response_from_dict = UploadPostDataResponse.from_dict(upload_post_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
