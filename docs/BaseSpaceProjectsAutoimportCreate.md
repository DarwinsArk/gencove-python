# BaseSpaceProjectsAutoimportCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**metadata** | **object** | Additional information to be attached to the Sample instances. | [optional]
**action** | **str** |  | [optional] [readonly]

## Example

```python
from gencove_client.models.base_space_projects_autoimport_create import BaseSpaceProjectsAutoimportCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSpaceProjectsAutoimportCreate from a JSON string
base_space_projects_autoimport_create_instance = BaseSpaceProjectsAutoimportCreate.from_json(json)
# print the JSON string representation of the object
print(BaseSpaceProjectsAutoimportCreate.to_json())

# convert the object into a dict
base_space_projects_autoimport_create_dict = base_space_projects_autoimport_create_instance.to_dict()
# create an instance of BaseSpaceProjectsAutoimportCreate from a dict
base_space_projects_autoimport_create_from_dict = BaseSpaceProjectsAutoimportCreate.from_dict(base_space_projects_autoimport_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
