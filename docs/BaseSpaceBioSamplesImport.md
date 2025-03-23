# BaseSpaceBioSamplesImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  |
**basespace_bio_samples** | [**List[BaseSpaceBioSampleNested]**](BaseSpaceBioSampleNested.md) |  |
**metadata** | **object** |  | [optional]

## Example

```python
from gencove_client.models.base_space_bio_samples_import import BaseSpaceBioSamplesImport

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSpaceBioSamplesImport from a JSON string
base_space_bio_samples_import_instance = BaseSpaceBioSamplesImport.from_json(json)
# print the JSON string representation of the object
print(BaseSpaceBioSamplesImport.to_json())

# convert the object into a dict
base_space_bio_samples_import_dict = base_space_bio_samples_import_instance.to_dict()
# create an instance of BaseSpaceBioSamplesImport from a dict
base_space_bio_samples_import_from_dict = BaseSpaceBioSamplesImport.from_dict(base_space_bio_samples_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
