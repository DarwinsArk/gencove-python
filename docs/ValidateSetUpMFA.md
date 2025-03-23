# ValidateSetUpMFA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  |
**backup_tokens** | **List[Optional[str]]** |  | [optional] [readonly]

## Example

```python
from gencove_client.models.validate_set_up_mfa import ValidateSetUpMFA

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateSetUpMFA from a JSON string
validate_set_up_mfa_instance = ValidateSetUpMFA.from_json(json)
# print the JSON string representation of the object
print(ValidateSetUpMFA.to_json())

# convert the object into a dict
validate_set_up_mfa_dict = validate_set_up_mfa_instance.to_dict()
# create an instance of ValidateSetUpMFA from a dict
validate_set_up_mfa_from_dict = ValidateSetUpMFA.from_dict(validate_set_up_mfa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
