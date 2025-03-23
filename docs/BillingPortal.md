# BillingPortal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_portal_url** | **str** | Billing portal URL to go to. | [optional] [readonly]

## Example

```python
from gencove_client.models.billing_portal import BillingPortal

# TODO update the JSON string below
json = "{}"
# create an instance of BillingPortal from a JSON string
billing_portal_instance = BillingPortal.from_json(json)
# print the JSON string representation of the object
print(BillingPortal.to_json())

# convert the object into a dict
billing_portal_dict = billing_portal_instance.to_dict()
# create an instance of BillingPortal from a dict
billing_portal_from_dict = BillingPortal.from_dict(billing_portal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
