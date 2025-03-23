# UploadPresignedPostDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  |
**fields** | [**AWSPresignedPostData**](AWSPresignedPostData.md) |  |

## Example

```python
from gencove_client.models.upload_presigned_post_data_response import UploadPresignedPostDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPresignedPostDataResponse from a JSON string
upload_presigned_post_data_response_instance = UploadPresignedPostDataResponse.from_json(json)
# print the JSON string representation of the object
print(UploadPresignedPostDataResponse.to_json())

# convert the object into a dict
upload_presigned_post_data_response_dict = upload_presigned_post_data_response_instance.to_dict()
# create an instance of UploadPresignedPostDataResponse from a dict
upload_presigned_post_data_response_from_dict = UploadPresignedPostDataResponse.from_dict(upload_presigned_post_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
