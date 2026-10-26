# PaginatedCostReportPeriodList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[CostReportPeriod]**](CostReportPeriod.md) |  |

## Example

```python
from gencove_client.models.paginated_cost_report_period_list import PaginatedCostReportPeriodList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCostReportPeriodList from a JSON string
paginated_cost_report_period_list_instance = PaginatedCostReportPeriodList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCostReportPeriodList.to_json())

# convert the object into a dict
paginated_cost_report_period_list_dict = paginated_cost_report_period_list_instance.to_dict()
# create an instance of PaginatedCostReportPeriodList from a dict
paginated_cost_report_period_list_from_dict = PaginatedCostReportPeriodList.from_dict(paginated_cost_report_period_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
