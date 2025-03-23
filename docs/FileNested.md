# FileNested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**s3_path** | **str** | S3 object key | [optional]
**size** | **int** | Size as reported by AWS in bytes | [optional]
**download_url** | **str** |  | [optional] [readonly]
**file_type** | **str** |  | [optional] [readonly]
**checksum_sha256** | **str** | Object&#39;s sha256 Checksum | [optional]
**shadow_mode** | **bool** | If true, file is only accessible by organizations with shadow mode access enabled. | [optional]

## Example

```python
from gencove_client.models.file_nested import FileNested

# TODO update the JSON string below
json = "{}"
# create an instance of FileNested from a JSON string
file_nested_instance = FileNested.from_json(json)
# print the JSON string representation of the object
print(FileNested.to_json())

# convert the object into a dict
file_nested_dict = file_nested_instance.to_dict()
# create an instance of FileNested from a dict
file_nested_from_dict = FileNested.from_dict(file_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
