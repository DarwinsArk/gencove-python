# SocialProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**authorization_uri** | **str** |  |
**accounts** | [**List[SocialAccountNested]**](SocialAccountNested.md) | User connected social account | [optional] [readonly]

## Example

```python
from gencove_client.models.social_provider import SocialProvider

# TODO update the JSON string below
json = "{}"
# create an instance of SocialProvider from a JSON string
social_provider_instance = SocialProvider.from_json(json)
# print the JSON string representation of the object
print(SocialProvider.to_json())

# convert the object into a dict
social_provider_dict = social_provider_instance.to_dict()
# create an instance of SocialProvider from a dict
social_provider_from_dict = SocialProvider.from_dict(social_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
