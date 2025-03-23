# UploadURLCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_path** | **str** |  |
**source_url** | **str** |  |

## Example

```python
from gencove_client.models.upload_url_create import UploadURLCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UploadURLCreate from a JSON string
upload_url_create_instance = UploadURLCreate.from_json(json)
# print the JSON string representation of the object
print(UploadURLCreate.to_json())

# convert the object into a dict
upload_url_create_dict = upload_url_create_instance.to_dict()
# create an instance of UploadURLCreate from a dict
upload_url_create_from_dict = UploadURLCreate.from_dict(upload_url_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
