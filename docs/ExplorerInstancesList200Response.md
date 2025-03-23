# ExplorerInstancesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[ExplorerInstance]**](ExplorerInstance.md) |  |

## Example

```python
from gencove_client.models.explorer_instances_list200_response import ExplorerInstancesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerInstancesList200Response from a JSON string
explorer_instances_list200_response_instance = ExplorerInstancesList200Response.from_json(json)
# print the JSON string representation of the object
print(ExplorerInstancesList200Response.to_json())

# convert the object into a dict
explorer_instances_list200_response_dict = explorer_instances_list200_response_instance.to_dict()
# create an instance of ExplorerInstancesList200Response from a dict
explorer_instances_list200_response_from_dict = ExplorerInstancesList200Response.from_dict(explorer_instances_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
