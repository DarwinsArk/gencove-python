# Upload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**last_status** | [**UploadStatusNested**](UploadStatusNested.md) |  | [optional]
**file** | [**FileNested**](FileNested.md) |  |
**created** | **datetime** |  | [optional]
**destination_path** | **str** | Destination path given by the user as an optional argument | [optional]
**source** | **str** |  |
**user** | **str** |  |
**organization** | **str** |  |

## Example

```python
from gencove_client.models.upload import Upload

# TODO update the JSON string below
json = "{}"
# create an instance of Upload from a JSON string
upload_instance = Upload.from_json(json)
# print the JSON string representation of the object
print(Upload.to_json())

# convert the object into a dict
upload_dict = upload_instance.to_dict()
# create an instance of Upload from a dict
upload_from_dict = Upload.from_dict(upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
