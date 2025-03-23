# InviteOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**name** | **str** |  |

## Example

```python
from gencove_client.models.invite_organization import InviteOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of InviteOrganization from a JSON string
invite_organization_instance = InviteOrganization.from_json(json)
# print the JSON string representation of the object
print(InviteOrganization.to_json())

# convert the object into a dict
invite_organization_dict = invite_organization_instance.to_dict()
# create an instance of InviteOrganization from a dict
invite_organization_from_dict = InviteOrganization.from_dict(invite_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
