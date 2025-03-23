# OTPTokenObtainPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp_token** | **str** |  | [optional]
**backup_token** | **str** |  | [optional]
**email** | **str** |  |
**password** | **str** |  |

## Example

```python
from gencove_client.models.otp_token_obtain_pair import OTPTokenObtainPair

# TODO update the JSON string below
json = "{}"
# create an instance of OTPTokenObtainPair from a JSON string
otp_token_obtain_pair_instance = OTPTokenObtainPair.from_json(json)
# print the JSON string representation of the object
print(OTPTokenObtainPair.to_json())

# convert the object into a dict
otp_token_obtain_pair_dict = otp_token_obtain_pair_instance.to_dict()
# create an instance of OTPTokenObtainPair from a dict
otp_token_obtain_pair_from_dict = OTPTokenObtainPair.from_dict(otp_token_obtain_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
