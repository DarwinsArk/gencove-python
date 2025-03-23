# ProjectSamplesImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  |
**samples** | [**List[ExistingSample]**](ExistingSample.md) |  |
**metadata** | **object** |  | [optional]

## Example

```python
from gencove_client.models.project_samples_import import ProjectSamplesImport

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSamplesImport from a JSON string
project_samples_import_instance = ProjectSamplesImport.from_json(json)
# print the JSON string representation of the object
print(ProjectSamplesImport.to_json())

# convert the object into a dict
project_samples_import_dict = project_samples_import_instance.to_dict()
# create an instance of ProjectSamplesImport from a dict
project_samples_import_from_dict = ProjectSamplesImport.from_dict(project_samples_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
