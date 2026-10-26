# PaginatedCostReportRecordList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[CostReportRecord]**](CostReportRecord.md) |  |

## Example

```python
from gencove_client.models.paginated_cost_report_record_list import PaginatedCostReportRecordList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCostReportRecordList from a JSON string
paginated_cost_report_record_list_instance = PaginatedCostReportRecordList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCostReportRecordList.to_json())

# convert the object into a dict
paginated_cost_report_record_list_dict = paginated_cost_report_record_list_instance.to_dict()
# create an instance of PaginatedCostReportRecordList from a dict
paginated_cost_report_record_list_from_dict = PaginatedCostReportRecordList.from_dict(paginated_cost_report_record_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
