# SocialSignUp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  |
**code** | **str** | Authorization code |

## Example

```python
from gencove_client.models.social_sign_up import SocialSignUp

# TODO update the JSON string below
json = "{}"
# create an instance of SocialSignUp from a JSON string
social_sign_up_instance = SocialSignUp.from_json(json)
# print the JSON string representation of the object
print(SocialSignUp.to_json())

# convert the object into a dict
social_sign_up_dict = social_sign_up_instance.to_dict()
# create an instance of SocialSignUp from a dict
social_sign_up_from_dict = SocialSignUp.from_dict(social_sign_up_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
