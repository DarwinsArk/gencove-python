# SampleStatusList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  |
**note** | **str** |  | [optional]
**created** | **datetime** |  | [optional]

## Example

```python
from gencove_client.models.sample_status_list import SampleStatusList

# TODO update the JSON string below
json = "{}"
# create an instance of SampleStatusList from a JSON string
sample_status_list_instance = SampleStatusList.from_json(json)
# print the JSON string representation of the object
print(SampleStatusList.to_json())

# convert the object into a dict
sample_status_list_dict = sample_status_list_instance.to_dict()
# create an instance of SampleStatusList from a dict
sample_status_list_from_dict = SampleStatusList.from_dict(sample_status_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
