# BaseSpaceProjectsAutoimport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**project_id** | **str** |  |
**identifier** | **str** |  |
**metadata** | **object** |  | [optional]

## Example

```python
from gencove_client.models.base_space_projects_autoimport import BaseSpaceProjectsAutoimport

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSpaceProjectsAutoimport from a JSON string
base_space_projects_autoimport_instance = BaseSpaceProjectsAutoimport.from_json(json)
# print the JSON string representation of the object
print(BaseSpaceProjectsAutoimport.to_json())

# convert the object into a dict
base_space_projects_autoimport_dict = base_space_projects_autoimport_instance.to_dict()
# create an instance of BaseSpaceProjectsAutoimport from a dict
base_space_projects_autoimport_from_dict = BaseSpaceProjectsAutoimport.from_dict(base_space_projects_autoimport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
