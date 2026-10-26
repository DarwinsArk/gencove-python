# PaginatedSampleSheetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[SampleSheet]**](SampleSheet.md) |  |

## Example

```python
from gencove_client.models.paginated_sample_sheet_list import PaginatedSampleSheetList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSampleSheetList from a JSON string
paginated_sample_sheet_list_instance = PaginatedSampleSheetList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSampleSheetList.to_json())

# convert the object into a dict
paginated_sample_sheet_list_dict = paginated_sample_sheet_list_instance.to_dict()
# create an instance of PaginatedSampleSheetList from a dict
paginated_sample_sheet_list_from_dict = PaginatedSampleSheetList.from_dict(paginated_sample_sheet_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
