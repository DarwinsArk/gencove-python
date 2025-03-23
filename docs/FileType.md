# FileType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | File extension |
**description** | **str** |  | [optional]

## Example

```python
from gencove_client.models.file_type import FileType

# TODO update the JSON string below
json = "{}"
# create an instance of FileType from a JSON string
file_type_instance = FileType.from_json(json)
# print the JSON string representation of the object
print(FileType.to_json())

# convert the object into a dict
file_type_dict = file_type_instance.to_dict()
# create an instance of FileType from a dict
file_type_from_dict = FileType.from_dict(file_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
