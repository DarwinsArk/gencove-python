# ArchiveSampleStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  |
**status** | **str** |  |
**created** | **str** |  |
**transition_cutoff** | **datetime** | Denotes the transition time for calculated states | [optional]

## Example

```python
from gencove_client.models.archive_sample_status import ArchiveSampleStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveSampleStatus from a JSON string
archive_sample_status_instance = ArchiveSampleStatus.from_json(json)
# print the JSON string representation of the object
print(ArchiveSampleStatus.to_json())

# convert the object into a dict
archive_sample_status_dict = archive_sample_status_instance.to_dict()
# create an instance of ArchiveSampleStatus from a dict
archive_sample_status_from_dict = ArchiveSampleStatus.from_dict(archive_sample_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
