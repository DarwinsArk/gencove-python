# SampleStatusNested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**status** | **str** |  |
**note** | **str** |  | [optional]
**created** | **datetime** |  | [optional]

## Example

```python
from gencove_client.models.sample_status_nested import SampleStatusNested

# TODO update the JSON string below
json = "{}"
# create an instance of SampleStatusNested from a JSON string
sample_status_nested_instance = SampleStatusNested.from_json(json)
# print the JSON string representation of the object
print(SampleStatusNested.to_json())

# convert the object into a dict
sample_status_nested_dict = sample_status_nested_instance.to_dict()
# create an instance of SampleStatusNested from a dict
sample_status_nested_from_dict = SampleStatusNested.from_dict(sample_status_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
