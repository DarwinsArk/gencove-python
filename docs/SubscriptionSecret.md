# SubscriptionSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** |  |

## Example

```python
from gencove_client.models.subscription_secret import SubscriptionSecret

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionSecret from a JSON string
subscription_secret_instance = SubscriptionSecret.from_json(json)
# print the JSON string representation of the object
print(SubscriptionSecret.to_json())

# convert the object into a dict
subscription_secret_dict = subscription_secret_instance.to_dict()
# create an instance of SubscriptionSecret from a dict
subscription_secret_from_dict = SubscriptionSecret.from_dict(subscription_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
