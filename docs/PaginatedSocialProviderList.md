# PaginatedSocialProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[SocialProvider]**](SocialProvider.md) |  |

## Example

```python
from gencove_client.models.paginated_social_provider_list import PaginatedSocialProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSocialProviderList from a JSON string
paginated_social_provider_list_instance = PaginatedSocialProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSocialProviderList.to_json())

# convert the object into a dict
paginated_social_provider_list_dict = paginated_social_provider_list_instance.to_dict()
# create an instance of PaginatedSocialProviderList from a dict
paginated_social_provider_list_from_dict = PaginatedSocialProviderList.from_dict(paginated_social_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
