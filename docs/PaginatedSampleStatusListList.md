# PaginatedSampleStatusListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[SampleStatusList]**](SampleStatusList.md) |  |

## Example

```python
from gencove_client.models.paginated_sample_status_list_list import PaginatedSampleStatusListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSampleStatusListList from a JSON string
paginated_sample_status_list_list_instance = PaginatedSampleStatusListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSampleStatusListList.to_json())

# convert the object into a dict
paginated_sample_status_list_list_dict = paginated_sample_status_list_list_instance.to_dict()
# create an instance of PaginatedSampleStatusListList from a dict
paginated_sample_status_list_list_from_dict = PaginatedSampleStatusListList.from_dict(paginated_sample_status_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
