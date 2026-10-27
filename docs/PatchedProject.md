# PatchedProject

Read roles out of a mapping preloaded by the list serializer.  ``preloaded_roles`` holds the roles of every object being serialized while a list is serialized, and stays None when a single object is serialized, in which case every role is looked up on its own.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] [readonly]
**name** | **str** |  | [optional]
**description** | **str** |  | [optional]
**created** | **datetime** |  | [optional] [readonly]
**modified** | **str** | Sample&#39;s last non-internal status that was added. | [optional] [readonly]
**hidden** | **bool** | Flag to hide the project. | [optional] [readonly]
**organization** | **UUID** |  | [optional] [readonly]
**organization_name** | **str** | Organization name | [optional] [readonly]
**sample_count** | **str** |  | [optional] [readonly]
**hidden_sample_count** | **str** |  | [optional] [readonly]
**pipeline_capabilities** | **UUID** | Versioned pipeline capabilities | [optional]
**project_modifications** | **object** | Allows for pipeline modifications e.g. disabling QC | [optional]
**roles** | **str** | Roles for the project in the organization. | [optional] [readonly]
**webhook_url** | **str** | Legacy: this field is not used anymore, it is present in the response for the sake of backwards compatility with clients. | [optional] [readonly]
**is_shared** | **bool** | Return whether the project is shared with other organizations | [optional] [readonly]
**locked** | **bool** | Flag to set the project to locked mode. | [optional] [readonly]

## Example

```python
from gencove_client.models.patched_project import PatchedProject

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProject from a JSON string
patched_project_instance = PatchedProject.from_json(json)
# print the JSON string representation of the object
print(PatchedProject.to_json())

# convert the object into a dict
patched_project_dict = patched_project_instance.to_dict()
# create an instance of PatchedProject from a dict
patched_project_from_dict = PatchedProject.from_dict(patched_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
