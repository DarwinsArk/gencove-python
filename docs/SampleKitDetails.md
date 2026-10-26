# SampleKitDetails

Kit details exposed for a sample's kit order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_id** | **UUID** | UUID of the sample the kit belongs to. | [readonly]
**provider_kit_id** | **str** | Kit ID printed on the kit; null until assigned by the provider. | [readonly]
**test_mode** | **bool** | True for test orders that will not be shipped. | [readonly]
**recipient_address_name** | **str** | Full name of the person the kit ships to. | [readonly]
**recipient_address_line1** | **str** | First line of the shipping address. | [readonly]
**recipient_address_line2** | **str** | Second line of the shipping address; empty if not given. | [readonly]
**recipient_address_line3** | **str** | Third line of the shipping address; empty if not given. | [readonly]
**recipient_address_city** | **str** | City of the shipping address. | [readonly]
**recipient_address_state_region** | **str** | State or region of the shipping address. US states are stored as their 2-letter code. | [readonly]
**recipient_address_postal_code** | **str** | Postal or ZIP code of the shipping address. | [readonly]
**recipient_address_country_code** | **str** | 2-letter ISO country code, e.g. US. | [readonly]
**recipient_phone** | **str** | Recipient phone number, e.g. +14155551234. | [readonly]
**recipient_instructions** | **str** | Delivery instructions for the carrier; empty if not given. | [readonly]
**tracking_number** | **str** | Shipping tracking number; null until the kit is shipped. | [readonly]
**tracking_carrier** | **str** | Shipping carrier name; null until the kit is shipped. | [readonly]
**tracking_url** | **str** | Carrier tracking URL; null when the carrier is not recognized. | [readonly]
**provider_destruction_requested** | **datetime** | When the physical swab was added to a destruction list sent to the lab. Null unless swab destruction is arranged for your organization, and null forever otherwise. Destruction affects only the physical swab: no data, files or results are removed. | [readonly]
**provider_destruction_completed** | **datetime** | When the lab confirmed the physical swab was destroyed. Null while a requested destruction is still awaiting confirmation. | [readonly]
**created** | **datetime** |  | [optional]

## Example

```python
from gencove_client.models.sample_kit_details import SampleKitDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SampleKitDetails from a JSON string
sample_kit_details_instance = SampleKitDetails.from_json(json)
# print the JSON string representation of the object
print(SampleKitDetails.to_json())

# convert the object into a dict
sample_kit_details_dict = sample_kit_details_instance.to_dict()
# create an instance of SampleKitDetails from a dict
sample_kit_details_from_dict = SampleKitDetails.from_dict(sample_kit_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
