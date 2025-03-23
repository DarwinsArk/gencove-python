# SampleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**run** | **str** |  | [optional]
**created** | **datetime** |  | [optional]
**hidden** | **bool** | Flag to hide the sample. | [optional]
**modified** | **datetime** |  |
**client_id** | **str** | Legacy: external_id |
**physical_id** | **str** | Legacy: external_id, external_barcode and sample_barcode |
**legacy_id** | **str** | Legacy: sample_id/member_id. Matching sample_ids from back_api app. |
**last_status** | [**SampleStatusNested**](SampleStatusNested.md) |  | [optional]
**archive_last_status** | [**ArchiveSampleStatus**](ArchiveSampleStatus.md) |  | [optional]
**failed_qc** | **str** | Description of failed_qc status if present | [optional] [readonly]

## Example

```python
from gencove_client.models.sample_list import SampleList

# TODO update the JSON string below
json = "{}"
# create an instance of SampleList from a JSON string
sample_list_instance = SampleList.from_json(json)
# print the JSON string representation of the object
print(SampleList.to_json())

# convert the object into a dict
sample_list_dict = sample_list_instance.to_dict()
# create an instance of SampleList from a dict
sample_list_from_dict = SampleList.from_dict(sample_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
