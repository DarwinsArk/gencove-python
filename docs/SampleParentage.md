# SampleParentage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parentage_tested** | **str** |  | [readonly]
**parentage** | **str** |  | [readonly]

## Example

```python
from gencove_client.models.sample_parentage import SampleParentage

# TODO update the JSON string below
json = "{}"
# create an instance of SampleParentage from a JSON string
sample_parentage_instance = SampleParentage.from_json(json)
# print the JSON string representation of the object
print(SampleParentage.to_json())

# convert the object into a dict
sample_parentage_dict = sample_parentage_instance.to_dict()
# create an instance of SampleParentage from a dict
sample_parentage_from_dict = SampleParentage.from_dict(sample_parentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
