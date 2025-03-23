# FileTypesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[FileType]**](FileType.md) |  |

## Example

```python
from gencove_client.models.file_types_list200_response import FileTypesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FileTypesList200Response from a JSON string
file_types_list200_response_instance = FileTypesList200Response.from_json(json)
# print the JSON string representation of the object
print(FileTypesList200Response.to_json())

# convert the object into a dict
file_types_list200_response_dict = file_types_list200_response_instance.to_dict()
# create an instance of FileTypesList200Response from a dict
file_types_list200_response_from_dict = FileTypesList200Response.from_dict(file_types_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
