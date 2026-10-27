# PaginatedBaseSpaceBioSampleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[BaseSpaceBioSample]**](BaseSpaceBioSample.md) |  |

## Example

```python
from gencove_client.models.paginated_base_space_bio_sample_list import PaginatedBaseSpaceBioSampleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBaseSpaceBioSampleList from a JSON string
paginated_base_space_bio_sample_list_instance = PaginatedBaseSpaceBioSampleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBaseSpaceBioSampleList.to_json())

# convert the object into a dict
paginated_base_space_bio_sample_list_dict = paginated_base_space_bio_sample_list_instance.to_dict()
# create an instance of PaginatedBaseSpaceBioSampleList from a dict
paginated_base_space_bio_sample_list_from_dict = PaginatedBaseSpaceBioSampleList.from_dict(paginated_base_space_bio_sample_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
