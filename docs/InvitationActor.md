# InvitationActor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**name** | **str** |  | [optional]

## Example

```python
from gencove_client.models.invitation_actor import InvitationActor

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationActor from a JSON string
invitation_actor_instance = InvitationActor.from_json(json)
# print the JSON string representation of the object
print(InvitationActor.to_json())

# convert the object into a dict
invitation_actor_dict = invitation_actor_instance.to_dict()
# create an instance of InvitationActor from a dict
invitation_actor_from_dict = InvitationActor.from_dict(invitation_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
