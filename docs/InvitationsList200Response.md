# InvitationsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[Invitation]**](Invitation.md) |  |

## Example

```python
from gencove_client.models.invitations_list200_response import InvitationsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationsList200Response from a JSON string
invitations_list200_response_instance = InvitationsList200Response.from_json(json)
# print the JSON string representation of the object
print(InvitationsList200Response.to_json())

# convert the object into a dict
invitations_list200_response_dict = invitations_list200_response_instance.to_dict()
# create an instance of InvitationsList200Response from a dict
invitations_list200_response_from_dict = InvitationsList200Response.from_dict(invitations_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
