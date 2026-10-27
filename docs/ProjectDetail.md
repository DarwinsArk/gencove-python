# ProjectDetail

Only used when retrieving a single Project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**name** | **str** |  |
**description** | **str** |  | [optional]
**created** | **datetime** |  | [optional]
**modified** | **str** | Sample&#39;s last non-internal status that was added. | [readonly]
**hidden** | **bool** | Flag to hide the project. | [optional]
**organization** | **UUID** |  |
**organization_name** | **str** | Organization name | [readonly]
**sample_count** | **str** |  | [readonly]
**hidden_sample_count** | **str** |  | [readonly]
**pipeline_capabilities** | **UUID** | Versioned pipeline capabilities |
**project_modifications** | **object** | Allows for pipeline modifications e.g. disabling QC | [optional]
**roles** | **str** | Roles for the project in the organization. | [readonly]
**webhook_url** | **str** | Legacy: this field is not used anymore, it is present in the response for the sake of backwards compatility with clients. | [readonly]
**is_shared** | **bool** | Return whether the project is shared with other organizations | [readonly]
**locked** | **bool** | Flag to set the project to locked mode. | [optional]
**files** | [**List[ProjectFileNested]**](ProjectFileNested.md) | Project files | [readonly]

## Example

```python
from gencove_client.models.project_detail import ProjectDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDetail from a JSON string
project_detail_instance = ProjectDetail.from_json(json)
# print the JSON string representation of the object
print(ProjectDetail.to_json())

# convert the object into a dict
project_detail_dict = project_detail_instance.to_dict()
# create an instance of ProjectDetail from a dict
project_detail_from_dict = ProjectDetail.from_dict(project_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
