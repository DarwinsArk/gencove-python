# SampleRestore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_ids** | **List[str]** | List of sample IDs or if empty all archived samples will be used |
**restore_group_id** | **str** |  | [optional] [readonly]
**created** | **datetime** |  | [optional] [readonly]

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
