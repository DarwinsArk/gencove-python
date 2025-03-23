# ExplorerCostReportRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**start_date** | **date** | First day of the month for this reporting cycle |
**end_date** | **date** | Last day of the month for this reporting cycle |
**report_amount** | **decimal.Decimal** |  | [optional]
**is_current_report** | **str** |  | [optional] [readonly]
**report_is_finalized** | **bool** | If True, this record will no longer be automatically updated | [optional]
**last_updated** | **datetime** |  | [optional] [readonly]
**files** | [**List[FileNested]**](FileNested.md) |  |

## Example

```python
from gencove_client.models.explorer_cost_report_record import ExplorerCostReportRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerCostReportRecord from a JSON string
explorer_cost_report_record_instance = ExplorerCostReportRecord.from_json(json)
# print the JSON string representation of the object
print(ExplorerCostReportRecord.to_json())

# convert the object into a dict
explorer_cost_report_record_dict = explorer_cost_report_record_instance.to_dict()
# create an instance of ExplorerCostReportRecord from a dict
explorer_cost_report_record_from_dict = ExplorerCostReportRecord.from_dict(explorer_cost_report_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
