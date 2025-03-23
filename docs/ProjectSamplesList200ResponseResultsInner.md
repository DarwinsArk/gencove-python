# ProjectSamplesList200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional]
**created** | **datetime** |  | [optional]
**hidden** | **bool** |  | [optional]
**modified** | **datetime** |  | [optional]
**client_id** | **str** |  | [optional]
**physical_id** | **str** |  | [optional]
**legacy_id** | **str** |  | [optional]
**last_status** | [**ProjectSamplesList200ResponseResultsInnerLastStatus**](ProjectSamplesList200ResponseResultsInnerLastStatus.md) |  | [optional]
**failed_qc** | **List[str]** |  | [optional]

## Example

```python
from gencove_client.models.project_samples_list200_response_results_inner import ProjectSamplesList200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSamplesList200ResponseResultsInner from a JSON string
project_samples_list200_response_results_inner_instance = ProjectSamplesList200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ProjectSamplesList200ResponseResultsInner.to_json())

# convert the object into a dict
project_samples_list200_response_results_inner_dict = project_samples_list200_response_results_inner_instance.to_dict()
# create an instance of ProjectSamplesList200ResponseResultsInner from a dict
project_samples_list200_response_results_inner_from_dict = ProjectSamplesList200ResponseResultsInner.from_dict(project_samples_list200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
