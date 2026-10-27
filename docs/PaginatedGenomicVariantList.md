# PaginatedGenomicVariantList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[GenomicVariant]**](GenomicVariant.md) |  |

## Example

```python
from gencove_client.models.paginated_genomic_variant_list import PaginatedGenomicVariantList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGenomicVariantList from a JSON string
paginated_genomic_variant_list_instance = PaginatedGenomicVariantList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGenomicVariantList.to_json())

# convert the object into a dict
paginated_genomic_variant_list_dict = paginated_genomic_variant_list_instance.to_dict()
# create an instance of PaginatedGenomicVariantList from a dict
paginated_genomic_variant_list_from_dict = PaginatedGenomicVariantList.from_dict(paginated_genomic_variant_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
