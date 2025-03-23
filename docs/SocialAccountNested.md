# SocialAccountNested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**created** | **datetime** |  | [optional]
**social_account_id** | **str** |  |
**auth_time** | **datetime** |  |

## Example

```python
from gencove_client.models.social_account_nested import SocialAccountNested

# TODO update the JSON string below
json = "{}"
# create an instance of SocialAccountNested from a JSON string
social_account_nested_instance = SocialAccountNested.from_json(json)
# print the JSON string representation of the object
print(SocialAccountNested.to_json())

# convert the object into a dict
social_account_nested_dict = social_account_nested_instance.to_dict()
# create an instance of SocialAccountNested from a dict
social_account_nested_from_dict = SocialAccountNested.from_dict(social_account_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
