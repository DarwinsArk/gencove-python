# ProjectSharesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[ProjectShare]**](ProjectShare.md) |  |

## Example

```python
from gencove_client.models.project_shares_list200_response import ProjectSharesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSharesList200Response from a JSON string
project_shares_list200_response_instance = ProjectSharesList200Response.from_json(json)
# print the JSON string representation of the object
print(ProjectSharesList200Response.to_json())

# convert the object into a dict
project_shares_list200_response_dict = project_shares_list200_response_instance.to_dict()
# create an instance of ProjectSharesList200Response from a dict
project_shares_list200_response_from_dict = ProjectSharesList200Response.from_dict(project_shares_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
