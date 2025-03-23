# BaseSpaceProjectsImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  |
**basespace_project_ids** | **List[str]** |  |
**metadata** | **object** |  | [optional]

## Example

```python
from gencove_client.models.base_space_projects_import import BaseSpaceProjectsImport

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSpaceProjectsImport from a JSON string
base_space_projects_import_instance = BaseSpaceProjectsImport.from_json(json)
# print the JSON string representation of the object
print(BaseSpaceProjectsImport.to_json())

# convert the object into a dict
base_space_projects_import_dict = base_space_projects_import_instance.to_dict()
# create an instance of BaseSpaceProjectsImport from a dict
base_space_projects_import_from_dict = BaseSpaceProjectsImport.from_dict(base_space_projects_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
