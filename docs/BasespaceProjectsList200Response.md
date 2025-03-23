# BasespaceProjectsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[BaseSpaceProject]**](BaseSpaceProject.md) |  |

## Example

```python
from gencove_client.models.basespace_projects_list200_response import BasespaceProjectsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BasespaceProjectsList200Response from a JSON string
basespace_projects_list200_response_instance = BasespaceProjectsList200Response.from_json(json)
# print the JSON string representation of the object
print(BasespaceProjectsList200Response.to_json())

# convert the object into a dict
basespace_projects_list200_response_dict = basespace_projects_list200_response_instance.to_dict()
# create an instance of BasespaceProjectsList200Response from a dict
basespace_projects_list200_response_from_dict = BasespaceProjectsList200Response.from_dict(basespace_projects_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
