# Project

Read roles out of a mapping preloaded by the list serializer.  ``preloaded_roles`` holds the roles of every object being serialized while a list is serialized, and stays None when a single object is serialized, in which case every role is looked up on its own.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**name** | **str** |  |
**description** | **str** |  | [optional]
**created** | **datetime** |  | [readonly]
**modified** | **str** | Sample&#39;s last non-internal status that was added. | [readonly]
**hidden** | **bool** | Flag to hide the project. | [readonly]
**organization** | **UUID** |  | [readonly]
**organization_name** | **str** | Organization name | [readonly]
**sample_count** | **str** |  | [readonly]
**hidden_sample_count** | **str** |  | [readonly]
**pipeline_capabilities** | **UUID** | Versioned pipeline capabilities |
**project_modifications** | **object** | Allows for pipeline modifications e.g. disabling QC | [optional]
**roles** | **str** | Roles for the project in the organization. | [readonly]
**webhook_url** | **str** | Legacy: this field is not used anymore, it is present in the response for the sake of backwards compatility with clients. | [readonly]
**is_shared** | **bool** | Return whether the project is shared with other organizations | [readonly]
**locked** | **bool** | Flag to set the project to locked mode. | [readonly]

## Example

```python
from gencove_client.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
