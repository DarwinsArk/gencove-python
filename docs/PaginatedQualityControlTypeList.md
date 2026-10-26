# PaginatedQualityControlTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[QualityControlType]**](QualityControlType.md) |  |

## Example

```python
from gencove_client.models.paginated_quality_control_type_list import PaginatedQualityControlTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQualityControlTypeList from a JSON string
paginated_quality_control_type_list_instance = PaginatedQualityControlTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedQualityControlTypeList.to_json())

# convert the object into a dict
paginated_quality_control_type_list_dict = paginated_quality_control_type_list_instance.to_dict()
# create an instance of PaginatedQualityControlTypeList from a dict
paginated_quality_control_type_list_from_dict = PaginatedQualityControlTypeList.from_dict(paginated_quality_control_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
