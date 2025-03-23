# UploadStatusNested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**status** | **str** |  |
**note** | **str** |  | [optional]
**created** | **datetime** |  | [optional]

## Example

```python
from gencove_client.models.upload_status_nested import UploadStatusNested

# TODO update the JSON string below
json = "{}"
# create an instance of UploadStatusNested from a JSON string
upload_status_nested_instance = UploadStatusNested.from_json(json)
# print the JSON string representation of the object
print(UploadStatusNested.to_json())

# convert the object into a dict
upload_status_nested_dict = upload_status_nested_instance.to_dict()
# create an instance of UploadStatusNested from a dict
upload_status_nested_from_dict = UploadStatusNested.from_dict(upload_status_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
