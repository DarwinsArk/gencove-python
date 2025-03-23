# InvitationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**status** | **str** |  |
**created** | **datetime** |  | [optional]
**actor** | [**InvitationActor**](InvitationActor.md) |  | [optional]

## Example

```python
from gencove_client.models.invitation_status import InvitationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationStatus from a JSON string
invitation_status_instance = InvitationStatus.from_json(json)
# print the JSON string representation of the object
print(InvitationStatus.to_json())

# convert the object into a dict
invitation_status_dict = invitation_status_instance.to_dict()
# create an instance of InvitationStatus from a dict
invitation_status_from_dict = InvitationStatus.from_dict(invitation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
