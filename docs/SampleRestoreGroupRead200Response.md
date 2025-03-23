# SampleRestoreGroupRead200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[SampleList]**](SampleList.md) |  |

## Example

```python
from gencove_client.models.sample_restore_group_read200_response import SampleRestoreGroupRead200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SampleRestoreGroupRead200Response from a JSON string
sample_restore_group_read200_response_instance = SampleRestoreGroupRead200Response.from_json(json)
# print the JSON string representation of the object
print(SampleRestoreGroupRead200Response.to_json())

# convert the object into a dict
sample_restore_group_read200_response_dict = sample_restore_group_read200_response_instance.to_dict()
# create an instance of SampleRestoreGroupRead200Response from a dict
sample_restore_group_read200_response_from_dict = SampleRestoreGroupRead200Response.from_dict(sample_restore_group_read200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
