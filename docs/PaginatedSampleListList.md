# PaginatedSampleListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[SampleList]**](SampleList.md) |  |

## Example

```python
from gencove_client.models.paginated_sample_list_list import PaginatedSampleListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSampleListList from a JSON string
paginated_sample_list_list_instance = PaginatedSampleListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSampleListList.to_json())

# convert the object into a dict
paginated_sample_list_list_dict = paginated_sample_list_list_instance.to_dict()
# create an instance of PaginatedSampleListList from a dict
paginated_sample_list_list_from_dict = PaginatedSampleListList.from_dict(paginated_sample_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
