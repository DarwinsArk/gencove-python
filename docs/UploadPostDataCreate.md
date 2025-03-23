# UploadPostDataCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_path** | **str** |  |

## Example

```python
from gencove_client.models.upload_post_data_create import UploadPostDataCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPostDataCreate from a JSON string
upload_post_data_create_instance = UploadPostDataCreate.from_json(json)
# print the JSON string representation of the object
print(UploadPostDataCreate.to_json())

# convert the object into a dict
upload_post_data_create_dict = upload_post_data_create_instance.to_dict()
# create an instance of UploadPostDataCreate from a dict
upload_post_data_create_from_dict = UploadPostDataCreate.from_dict(upload_post_data_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
