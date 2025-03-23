# ProjectSamplesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[ProjectSamplesList200ResponseResultsInner]**](ProjectSamplesList200ResponseResultsInner.md) |  | [optional]

## Example

```python
from gencove_client.models.project_samples_list200_response import ProjectSamplesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSamplesList200Response from a JSON string
project_samples_list200_response_instance = ProjectSamplesList200Response.from_json(json)
# print the JSON string representation of the object
print(ProjectSamplesList200Response.to_json())

# convert the object into a dict
project_samples_list200_response_dict = project_samples_list200_response_instance.to_dict()
# create an instance of ProjectSamplesList200Response from a dict
project_samples_list200_response_from_dict = ProjectSamplesList200Response.from_dict(project_samples_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
