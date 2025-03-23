# SampleMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional]

## Example

```python
from gencove_client.models.sample_metadata import SampleMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SampleMetadata from a JSON string
sample_metadata_instance = SampleMetadata.from_json(json)
# print the JSON string representation of the object
print(SampleMetadata.to_json())

# convert the object into a dict
sample_metadata_dict = sample_metadata_instance.to_dict()
# create an instance of SampleMetadata from a dict
sample_metadata_from_dict = SampleMetadata.from_dict(sample_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
