# ProjectMergeVCFsJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**created** | **datetime** |  | [optional]
**user** | **str** |  |
**last_status** | [**JobStatusNested**](JobStatusNested.md) |  | [optional]
**up_to_date** | **bool** |  | [optional] [readonly] [default to False]

## Example

```python
from gencove_client.models.project_merge_vcfs_job import ProjectMergeVCFsJob

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMergeVCFsJob from a JSON string
project_merge_vcfs_job_instance = ProjectMergeVCFsJob.from_json(json)
# print the JSON string representation of the object
print(ProjectMergeVCFsJob.to_json())

# convert the object into a dict
project_merge_vcfs_job_dict = project_merge_vcfs_job_instance.to_dict()
# create an instance of ProjectMergeVCFsJob from a dict
project_merge_vcfs_job_from_dict = ProjectMergeVCFsJob.from_dict(project_merge_vcfs_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
