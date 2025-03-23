# ExtendedSampleSheetCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uploads** | [**List[SampleSheetCreate]**](SampleSheetCreate.md) |  |
**metadata** | **object** |  | [optional]

## Example

```python
from gencove_client.models.extended_sample_sheet_create import ExtendedSampleSheetCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedSampleSheetCreate from a JSON string
extended_sample_sheet_create_instance = ExtendedSampleSheetCreate.from_json(json)
# print the JSON string representation of the object
print(ExtendedSampleSheetCreate.to_json())

# convert the object into a dict
extended_sample_sheet_create_dict = extended_sample_sheet_create_instance.to_dict()
# create an instance of ExtendedSampleSheetCreate from a dict
extended_sample_sheet_create_from_dict = ExtendedSampleSheetCreate.from_dict(extended_sample_sheet_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
