# CostReportLine

One category of a month: quantity × unit rate × billing factor = amount, where the figures exist (Explorer lines carry an amount and a factor only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  |
**label** | **str** |  |
**quantity** | **decimal.Decimal** |  |
**unit** | **str** |  |
**unit_rate** | **decimal.Decimal** |  |
**billing_factor** | **decimal.Decimal** |  |
**amount** | **decimal.Decimal** |  |
**is_finalized** | **bool** |  |
**as_of** | **datetime** |  |
**covered_through** | **date** |  |

## Example

```python
from gencove_client.models.cost_report_line import CostReportLine

# TODO update the JSON string below
json = "{}"
# create an instance of CostReportLine from a JSON string
cost_report_line_instance = CostReportLine.from_json(json)
# print the JSON string representation of the object
print(CostReportLine.to_json())

# convert the object into a dict
cost_report_line_dict = cost_report_line_instance.to_dict()
# create an instance of CostReportLine from a dict
cost_report_line_from_dict = CostReportLine.from_dict(cost_report_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
