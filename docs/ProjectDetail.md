# ProjectDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**name** | **str** |  |
**description** | **str** |  | [optional]
**created** | **datetime** |  | [optional]
**modified** | **str** | Sample&#39;s last non-internal status that was added. | [optional] [readonly]
**hidden** | **bool** | Flag to hide the project. | [optional]
**organization** | **str** |  |
**organization_name** | **str** | Organization name | [optional] [readonly]
**sample_count** | **str** |  | [optional] [readonly]
**hidden_sample_count** | **str** |  | [optional] [readonly]
**pipeline_capabilities** | **str** | Versioned pipeline capabilities |
**project_modifications** | **object** | Allows for pipeline modifications e.g. disabling QC | [optional]
**roles** | **str** | Roles for the project in the organization. | [optional] [readonly]
**webhook_url** | **str** | Legacy: this field is not used anymore, it is present in the response for the sake of backwards compatility with clients. | [optional] [readonly]
**is_shared** | **str** |  | [optional] [readonly]
**locked** | **bool** | Flag to set the project to locked mode. | [optional]
**files** | [**List[ProjectFileNested]**](ProjectFileNested.md) | Project files | [optional] [readonly]

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
