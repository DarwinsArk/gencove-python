# SampleTraitScoresRead200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[TraitScore]**](TraitScore.md) |  |

## Example

```python
from gencove_client.models.sample_trait_scores_read200_response import SampleTraitScoresRead200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SampleTraitScoresRead200Response from a JSON string
sample_trait_scores_read200_response_instance = SampleTraitScoresRead200Response.from_json(json)
# print the JSON string representation of the object
print(SampleTraitScoresRead200Response.to_json())

# convert the object into a dict
sample_trait_scores_read200_response_dict = sample_trait_scores_read200_response_instance.to_dict()
# create an instance of SampleTraitScoresRead200Response from a dict
sample_trait_scores_read200_response_from_dict = SampleTraitScoresRead200Response.from_dict(sample_trait_scores_read200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
