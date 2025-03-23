# ProjectShareStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**status** | **str** |  | [optional]
**note** | **str** |  | [optional]
**created** | **datetime** |  | [optional]

## Example

```python
from gencove_client.models.project_share_status import ProjectShareStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectShareStatus from a JSON string
project_share_status_instance = ProjectShareStatus.from_json(json)
# print the JSON string representation of the object
print(ProjectShareStatus.to_json())

# convert the object into a dict
project_share_status_dict = project_share_status_instance.to_dict()
# create an instance of ProjectShareStatus from a dict
project_share_status_from_dict = ProjectShareStatus.from_dict(project_share_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
