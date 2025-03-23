# SampleManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**file_name** | **str** |  |
**file** | **str** |  | [optional] [readonly]
**project** | **str** |  | [optional] [readonly]
**created** | **datetime** |  | [optional]

## Example

```python
from gencove_client.models.sample_manifest import SampleManifest

# TODO update the JSON string below
json = "{}"
# create an instance of SampleManifest from a JSON string
sample_manifest_instance = SampleManifest.from_json(json)
# print the JSON string representation of the object
print(SampleManifest.to_json())

# convert the object into a dict
sample_manifest_dict = sample_manifest_instance.to_dict()
# create an instance of SampleManifest from a dict
sample_manifest_from_dict = SampleManifest.from_dict(sample_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
