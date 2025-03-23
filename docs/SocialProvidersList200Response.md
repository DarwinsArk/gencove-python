# SocialProvidersList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[SocialProvider]**](SocialProvider.md) |  |

## Example

```python
from gencove_client.models.social_providers_list200_response import SocialProvidersList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SocialProvidersList200Response from a JSON string
social_providers_list200_response_instance = SocialProvidersList200Response.from_json(json)
# print the JSON string representation of the object
print(SocialProvidersList200Response.to_json())

# convert the object into a dict
social_providers_list200_response_dict = social_providers_list200_response_instance.to_dict()
# create an instance of SocialProvidersList200Response from a dict
social_providers_list200_response_from_dict = SocialProvidersList200Response.from_dict(social_providers_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
