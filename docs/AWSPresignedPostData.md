# AWSPresignedPostData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  |
**aws_access_key_id** | **str** |  |
**policy** | **str** |  |
**signature** | **str** |  |

## Example

```python
from gencove_client.models.aws_presigned_post_data import AWSPresignedPostData

# TODO update the JSON string below
json = "{}"
# create an instance of AWSPresignedPostData from a JSON string
aws_presigned_post_data_instance = AWSPresignedPostData.from_json(json)
# print the JSON string representation of the object
print(AWSPresignedPostData.to_json())

# convert the object into a dict
aws_presigned_post_data_dict = aws_presigned_post_data_instance.to_dict()
# create an instance of AWSPresignedPostData from a dict
aws_presigned_post_data_from_dict = AWSPresignedPostData.from_dict(aws_presigned_post_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
