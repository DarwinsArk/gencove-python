# SampleKit

Serializer for creating kit orders in consumer mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** |  |
**metadata** | **object** |  | [optional]
**sample_id** | **UUID** |  | [readonly]
**recipient_address_name** | **str** |  |
**recipient_address_line1** | **str** |  |
**recipient_address_line2** | **str** |  | [optional]
**recipient_address_line3** | **str** |  | [optional]
**recipient_address_city** | **str** |  |
**recipient_address_postal_code** | **str** |  |
**recipient_address_state_region** | **str** |  |
**recipient_address_country_code** | [**RecipientAddressCountryCodeEnum**](RecipientAddressCountryCodeEnum.md) |  |
**recipient_phone** | **str** |  |
**recipient_email** | **str** |  |
**recipient_instructions** | **str** |  | [optional]
**test_mode** | **bool** | Set to true to create a test order that will not be shipped. Defaults to false. | [optional] [default to False]

## Example

```python
from gencove_client.models.sample_kit import SampleKit

# TODO update the JSON string below
json = "{}"
# create an instance of SampleKit from a JSON string
sample_kit_instance = SampleKit.from_json(json)
# print the JSON string representation of the object
print(SampleKit.to_json())

# convert the object into a dict
sample_kit_dict = sample_kit_instance.to_dict()
# create an instance of SampleKit from a dict
sample_kit_from_dict = SampleKit.from_dict(sample_kit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
