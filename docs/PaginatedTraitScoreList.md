# PaginatedTraitScoreList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[TraitScore]**](TraitScore.md) |  |

## Example

```python
from gencove_client.models.paginated_trait_score_list import PaginatedTraitScoreList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTraitScoreList from a JSON string
paginated_trait_score_list_instance = PaginatedTraitScoreList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTraitScoreList.to_json())

# convert the object into a dict
paginated_trait_score_list_dict = paginated_trait_score_list_instance.to_dict()
# create an instance of PaginatedTraitScoreList from a dict
paginated_trait_score_list_from_dict = PaginatedTraitScoreList.from_dict(paginated_trait_score_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
