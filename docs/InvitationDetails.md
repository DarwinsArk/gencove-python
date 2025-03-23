# InvitationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] [readonly]
**last_status** | [**InvitationStatus**](InvitationStatus.md) |  | [optional]
**expires** | **datetime** |  | [optional] [readonly]
**organization** | [**InviteOrganization**](InviteOrganization.md) |  |
**role** | **str** |  |

## Example

```python
from gencove_client.models.invitation_details import InvitationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationDetails from a JSON string
invitation_details_instance = InvitationDetails.from_json(json)
# print the JSON string representation of the object
print(InvitationDetails.to_json())

# convert the object into a dict
invitation_details_dict = invitation_details_instance.to_dict()
# create an instance of InvitationDetails from a dict
invitation_details_from_dict = InvitationDetails.from_dict(invitation_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
