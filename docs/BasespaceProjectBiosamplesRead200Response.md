# BasespaceProjectBiosamplesRead200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[BaseSpaceBioSample]**](BaseSpaceBioSample.md) |  |

## Example

```python
from gencove_client.models.basespace_project_biosamples_read200_response import BasespaceProjectBiosamplesRead200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BasespaceProjectBiosamplesRead200Response from a JSON string
basespace_project_biosamples_read200_response_instance = BasespaceProjectBiosamplesRead200Response.from_json(json)
# print the JSON string representation of the object
print(BasespaceProjectBiosamplesRead200Response.to_json())

# convert the object into a dict
basespace_project_biosamples_read200_response_dict = basespace_project_biosamples_read200_response_instance.to_dict()
# create an instance of BasespaceProjectBiosamplesRead200Response from a dict
basespace_project_biosamples_read200_response_from_dict = BasespaceProjectBiosamplesRead200Response.from_dict(basespace_project_biosamples_read200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
