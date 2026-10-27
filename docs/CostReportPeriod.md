# CostReportPeriod

One month of an organization's cost report. Field names follow the Explorer cost report list this replaces; ``id`` is its record's, null for a month without one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  |
**start_date** | **date** |  |
**end_date** | **date** |  |
**report_amount** | **decimal.Decimal** |  |
**is_current_report** | **bool** |  |
**report_is_finalized** | **bool** |  |
**last_updated** | **datetime** |  |
**covered_through** | **date** |  |
**categories** | [**List[CostReportLine]**](CostReportLine.md) |  |
**files** | [**List[FileNested]**](FileNested.md) |  |

## Example

```python
from gencove_client.models.cost_report_period import CostReportPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of CostReportPeriod from a JSON string
cost_report_period_instance = CostReportPeriod.from_json(json)
# print the JSON string representation of the object
print(CostReportPeriod.to_json())

# convert the object into a dict
cost_report_period_dict = cost_report_period_instance.to_dict()
# create an instance of CostReportPeriod from a dict
cost_report_period_from_dict = CostReportPeriod.from_dict(cost_report_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
