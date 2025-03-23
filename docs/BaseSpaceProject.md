# BaseSpaceProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basespace_id** | **str** |  |
**basespace_name** | **str** |  |
**basespace_description** | **str** |  |
**basespace_date_created** | **datetime** |  |
**basespace_date_modified** | **datetime** |  |

## Example

```python
from gencove_client.models.base_space_project import BaseSpaceProject

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSpaceProject from a JSON string
base_space_project_instance = BaseSpaceProject.from_json(json)
# print the JSON string representation of the object
print(BaseSpaceProject.to_json())

# convert the object into a dict
base_space_project_dict = base_space_project_instance.to_dict()
# create an instance of BaseSpaceProject from a dict
base_space_project_from_dict = BaseSpaceProject.from_dict(base_space_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
