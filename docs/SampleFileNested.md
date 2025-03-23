# SampleFileNested


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
from gencove_client.models.sample_file_nested import SampleFileNested

# TODO update the JSON string below
json = "{}"
# create an instance of SampleFileNested from a JSON string
sample_file_nested_instance = SampleFileNested.from_json(json)
# print the JSON string representation of the object
print(SampleFileNested.to_json())

# convert the object into a dict
sample_file_nested_dict = sample_file_nested_instance.to_dict()
# create an instance of SampleFileNested from a dict
sample_file_nested_from_dict = SampleFileNested.from_dict(sample_file_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
