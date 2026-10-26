# SubscriptionCreate

Generic Subscription serializer without scope object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**name** | **str** |  | [optional]
**target** | **str** | URL if webhook, e-mail address if email |
**event_types** | [**List[EventTypesEnum]**](EventTypesEnum.md) |  |

## Example

```python
from gencove_client.models.subscription_create import SubscriptionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCreate from a JSON string
subscription_create_instance = SubscriptionCreate.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCreate.to_json())

# convert the object into a dict
subscription_create_dict = subscription_create_instance.to_dict()
# create an instance of SubscriptionCreate from a dict
subscription_create_from_dict = SubscriptionCreate.from_dict(subscription_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
