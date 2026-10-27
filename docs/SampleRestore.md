# SampleRestore

Serializer for restoring samples from archived state.  Initially samples are set as `restore_requested` and a celery task is kicked off that starts restore process by kicking off an S3 batch job and marking samples as `restore_accepted`. `restore_started` is set when S3 notification is sent on `s3:ObjectRestore:Post` event. Samples are marked as `restored` in a separate celery task once the info gets passed down by an `s3:ObjectRestore:Completed` S3 event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_ids** | **List[UUID]** | List of sample IDs or if empty all archived samples will be used |
**restore_group_id** | **UUID** |  | [readonly]
**created** | **datetime** |  | [readonly]

## Example

```python
from gencove_client.models.sample_restore import SampleRestore

# TODO update the JSON string below
json = "{}"
# create an instance of SampleRestore from a JSON string
sample_restore_instance = SampleRestore.from_json(json)
# print the JSON string representation of the object
print(SampleRestore.to_json())

# convert the object into a dict
sample_restore_dict = sample_restore_instance.to_dict()
# create an instance of SampleRestore from a dict
sample_restore_from_dict = SampleRestore.from_dict(sample_restore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
