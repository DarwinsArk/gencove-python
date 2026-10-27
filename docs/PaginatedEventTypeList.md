# PaginatedEventTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[EventType]**](EventType.md) |  |

## Example

```python
from gencove_client.models.paginated_event_type_list import PaginatedEventTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEventTypeList from a JSON string
paginated_event_type_list_instance = PaginatedEventTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEventTypeList.to_json())

# convert the object into a dict
paginated_event_type_list_dict = paginated_event_type_list_instance.to_dict()
# create an instance of PaginatedEventTypeList from a dict
paginated_event_type_list_from_dict = PaginatedEventTypeList.from_dict(paginated_event_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
