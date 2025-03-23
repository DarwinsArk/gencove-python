# BatchFileNested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**s3_path** | **str** | S3 object key | [optional]
**size** | **int** | Size as reported by AWS in bytes | [optional]
**download_url** | **str** | Download url | [optional] [readonly]
**file_type** | **str** |  | [optional] [readonly]
**checksum_sha256** | **str** | Object&#39;s sha256 Checksum | [optional]
**shadow_mode** | **bool** | If true, file is only accessible by organizations with shadow mode access enabled. | [optional]

## Example

```python
from gencove_client.models.batch_file_nested import BatchFileNested

# TODO update the JSON string below
json = "{}"
# create an instance of BatchFileNested from a JSON string
batch_file_nested_instance = BatchFileNested.from_json(json)
# print the JSON string representation of the object
print(BatchFileNested.to_json())

# convert the object into a dict
batch_file_nested_dict = batch_file_nested_instance.to_dict()
# create an instance of BatchFileNested from a dict
batch_file_nested_from_dict = BatchFileNested.from_dict(batch_file_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
