# SampleDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**project** | **str** |  |
**run** | **str** |  | [optional]
**created** | **datetime** |  | [optional]
**modified** | **datetime** |  |
**hidden** | **bool** | Flag to hide the sample. | [optional]
**client_id** | **str** | Legacy: external_id |
**physical_id** | **str** | Legacy: external_id, external_barcode and sample_barcode |
**legacy_id** | **str** | Legacy: sample_id/member_id. Matching sample_ids from back_api app. |
**last_status** | [**SampleStatusNested**](SampleStatusNested.md) |  | [optional]
**archive_last_status** | [**ArchiveSampleStatus**](ArchiveSampleStatus.md) |  | [optional]
**files** | [**List[SampleFileNested]**](SampleFileNested.md) | Sample files | [optional] [readonly]

## Example

```python
from gencove_client.models.sample_details import SampleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SampleDetails from a JSON string
sample_details_instance = SampleDetails.from_json(json)
# print the JSON string representation of the object
print(SampleDetails.to_json())

# convert the object into a dict
sample_details_dict = sample_details_instance.to_dict()
# create an instance of SampleDetails from a dict
sample_details_from_dict = SampleDetails.from_dict(sample_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
