# SetUpMFA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_type** | **str** |  |
**secret** | **str** | Authenticator secret, used when device_type is \&quot;generator\&quot; | [optional] [readonly]
**config_url** | **str** | Url to build the QR code image, used when device_type is \&quot;generator\&quot; | [optional] [readonly]

## Example

```python
from gencove_client.models.set_up_mfa import SetUpMFA

# TODO update the JSON string below
json = "{}"
# create an instance of SetUpMFA from a JSON string
set_up_mfa_instance = SetUpMFA.from_json(json)
# print the JSON string representation of the object
print(SetUpMFA.to_json())

# convert the object into a dict
set_up_mfa_dict = set_up_mfa_instance.to_dict()
# create an instance of SetUpMFA from a dict
set_up_mfa_from_dict = SetUpMFA.from_dict(set_up_mfa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
