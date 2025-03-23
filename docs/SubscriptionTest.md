# SubscriptionTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** |  | [optional]
**retry** | **bool** |  | [optional] [default to False]

## Example

```python
from gencove_client.models.subscription_test import SubscriptionTest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionTest from a JSON string
subscription_test_instance = SubscriptionTest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionTest.to_json())

# convert the object into a dict
subscription_test_dict = subscription_test_instance.to_dict()
# create an instance of SubscriptionTest from a dict
subscription_test_from_dict = SubscriptionTest.from_dict(subscription_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
