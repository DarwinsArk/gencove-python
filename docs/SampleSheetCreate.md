# SampleSheetCreate

Adds samples with their uploads to the project.  Samples are being created in `create` method of this serializer. They don't exist as objects in db before that.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  |
**fastq** | [**FastqsNestedCreate**](FastqsNestedCreate.md) |  |
**sample** | **UUID** |  | [readonly]

## Example

```python
from gencove_client.models.sample_sheet_create import SampleSheetCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SampleSheetCreate from a JSON string
sample_sheet_create_instance = SampleSheetCreate.from_json(json)
# print the JSON string representation of the object
print(SampleSheetCreate.to_json())

# convert the object into a dict
sample_sheet_create_dict = sample_sheet_create_instance.to_dict()
# create an instance of SampleSheetCreate from a dict
sample_sheet_create_from_dict = SampleSheetCreate.from_dict(sample_sheet_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
