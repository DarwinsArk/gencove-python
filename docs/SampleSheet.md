# SampleSheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  |
**fastq** | [**UploadNestedList**](UploadNestedList.md) |  | [optional]

## Example

```python
from gencove_client.models.sample_sheet import SampleSheet

# TODO update the JSON string below
json = "{}"
# create an instance of SampleSheet from a JSON string
sample_sheet_instance = SampleSheet.from_json(json)
# print the JSON string representation of the object
print(SampleSheet.to_json())

# convert the object into a dict
sample_sheet_dict = sample_sheet_instance.to_dict()
# create an instance of SampleSheet from a dict
sample_sheet_from_dict = SampleSheet.from_dict(sample_sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
