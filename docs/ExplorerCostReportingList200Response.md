# ExplorerCostReportingList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[ExplorerCostReportRecord]**](ExplorerCostReportRecord.md) |  |

## Example

```python
from gencove_client.models.explorer_cost_reporting_list200_response import ExplorerCostReportingList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerCostReportingList200Response from a JSON string
explorer_cost_reporting_list200_response_instance = ExplorerCostReportingList200Response.from_json(json)
# print the JSON string representation of the object
print(ExplorerCostReportingList200Response.to_json())

# convert the object into a dict
explorer_cost_reporting_list200_response_dict = explorer_cost_reporting_list200_response_instance.to_dict()
# create an instance of ExplorerCostReportingList200Response from a dict
explorer_cost_reporting_list200_response_from_dict = ExplorerCostReportingList200Response.from_dict(explorer_cost_reporting_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
