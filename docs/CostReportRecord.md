# CostReportRecord

One month's cost report files (``costs.report_records``). Field names follow the cost report list the web reads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**start_date** | **date** | First day of the month | [readonly]
**end_date** | **date** | Last day of the month | [readonly]
**include_cross_org** | **bool** | Covers the organizations a grant of the owner&#39;s covered that month, beside its own costs | [readonly]
**report_amount** | **decimal.Decimal** | What the summary rows sum to, in USD | [readonly]
**is_current_report** | **bool** |  | [readonly]
**report_is_finalized** | **bool** | Every line in the files is finalized; the files are not rebuilt | [readonly]
**last_updated** | **datetime** |  | [readonly]
**covered_through** | **date** | Last day every platform figure in the report accounts for; empty when the report has none | [readonly]
**files** | [**List[CostReportFile]**](CostReportFile.md) |  | [readonly]

## Example

```python
from gencove_client.models.cost_report_record import CostReportRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CostReportRecord from a JSON string
cost_report_record_instance = CostReportRecord.from_json(json)
# print the JSON string representation of the object
print(CostReportRecord.to_json())

# convert the object into a dict
cost_report_record_dict = cost_report_record_instance.to_dict()
# create an instance of CostReportRecord from a dict
cost_report_record_from_dict = CostReportRecord.from_dict(cost_report_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
