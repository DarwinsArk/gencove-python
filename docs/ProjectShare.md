# ProjectShare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**project** | **str** |  |
**shared_with_org** | **str** |  | [optional] [readonly]
**shared_with_org_name** | **str** |  | [optional] [readonly]
**shared_with_user_emails** | **List[str]** |  |
**shared_with_user_email** | **str** |  | [optional] [readonly]
**shared_by_user_email** | **str** |  | [optional] [readonly]
**share_level** | **str** |  |
**last_status** | [**ProjectShareStatus**](ProjectShareStatus.md) |  | [optional]

## Example

```python
from gencove_client.models.project_share import ProjectShare

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectShare from a JSON string
project_share_instance = ProjectShare.from_json(json)
# print the JSON string representation of the object
print(ProjectShare.to_json())

# convert the object into a dict
project_share_dict = project_share_instance.to_dict()
# create an instance of ProjectShare from a dict
project_share_from_dict = ProjectShare.from_dict(project_share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
