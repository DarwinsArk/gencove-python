# UploadNestedList

Uploaded fastq

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload** | **str** |  |
**destination_path** | **str** | Destination path given by the user as an optional argument | [optional]
**last_status** | [**UploadStatusNested**](UploadStatusNested.md) |  | [optional]
**source_url** | **str** |  | [optional] [readonly]

## Example

```python
from gencove_client.models.upload_nested_list import UploadNestedList

# TODO update the JSON string below
json = "{}"
# create an instance of UploadNestedList from a JSON string
upload_nested_list_instance = UploadNestedList.from_json(json)
# print the JSON string representation of the object
print(UploadNestedList.to_json())

# convert the object into a dict
upload_nested_list_dict = upload_nested_list_instance.to_dict()
# create an instance of UploadNestedList from a dict
upload_nested_list_from_dict = UploadNestedList.from_dict(upload_nested_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
