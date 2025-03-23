# BaseSpaceBioSampleNested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basespace_id** | **str** |  |
**client_id** | **str** |  |
**sample** | **str** |  | [optional] [readonly]

## Example

```python
from gencove_client.models.base_space_bio_sample_nested import BaseSpaceBioSampleNested

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSpaceBioSampleNested from a JSON string
base_space_bio_sample_nested_instance = BaseSpaceBioSampleNested.from_json(json)
# print the JSON string representation of the object
print(BaseSpaceBioSampleNested.to_json())

# convert the object into a dict
base_space_bio_sample_nested_dict = base_space_bio_sample_nested_instance.to_dict()
# create an instance of BaseSpaceBioSampleNested from a dict
base_space_bio_sample_nested_from_dict = BaseSpaceBioSampleNested.from_dict(base_space_bio_sample_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
