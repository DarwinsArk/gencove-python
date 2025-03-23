# SampleSheetList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[SampleSheet]**](SampleSheet.md) |  |

## Example

```python
from gencove_client.models.sample_sheet_list200_response import SampleSheetList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SampleSheetList200Response from a JSON string
sample_sheet_list200_response_instance = SampleSheetList200Response.from_json(json)
# print the JSON string representation of the object
print(SampleSheetList200Response.to_json())

# convert the object into a dict
sample_sheet_list200_response_dict = sample_sheet_list200_response_instance.to_dict()
# create an instance of SampleSheetList200Response from a dict
sample_sheet_list200_response_from_dict = SampleSheetList200Response.from_dict(sample_sheet_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
