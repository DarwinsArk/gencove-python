# PatchedInvitationDetails

Represent invitation for invitee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] [readonly]
**last_status** | [**InvitationStatus**](InvitationStatus.md) |  | [optional] [readonly]
**expires** | **datetime** |  | [optional] [readonly]
**organization** | [**InviteOrganization**](InviteOrganization.md) |  | [optional]
**role** | **str** |  | [optional]

## Example

```python
from gencove_client.models.patched_invitation_details import PatchedInvitationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInvitationDetails from a JSON string
patched_invitation_details_instance = PatchedInvitationDetails.from_json(json)
# print the JSON string representation of the object
print(PatchedInvitationDetails.to_json())

# convert the object into a dict
patched_invitation_details_dict = patched_invitation_details_instance.to_dict()
# create an instance of PatchedInvitationDetails from a dict
patched_invitation_details_from_dict = PatchedInvitationDetails.from_dict(patched_invitation_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
