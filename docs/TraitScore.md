# TraitScore

Serializer trait score and associated trait metadata models.  This is not really optimal, since it pulls data from multiple parent tables for objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trait_score** | [**TraitScoreSelfNested**](TraitScoreSelfNested.md) |  |
**trait_distribution** | [**TraitDistribution**](TraitDistribution.md) |  |
**trait** | [**Trait**](Trait.md) |  |
**trait_unit** | [**TraitUnit**](TraitUnit.md) |  |
**risk** | **str** | Return risk level for the trait score.  Returns:     Optional[str]: \&quot;high_risk\&quot; if the value is greater than or equal to the risk threshold,     \&quot;not_high_risk\&quot; otherwise. If the risk threshold or percentile is None, return None. | [readonly]

## Example

```python
from gencove_client.models.trait_score import TraitScore

# TODO update the JSON string below
json = "{}"
# create an instance of TraitScore from a JSON string
trait_score_instance = TraitScore.from_json(json)
# print the JSON string representation of the object
print(TraitScore.to_json())

# convert the object into a dict
trait_score_dict = trait_score_instance.to_dict()
# create an instance of TraitScore from a dict
trait_score_from_dict = TraitScore.from_dict(trait_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
