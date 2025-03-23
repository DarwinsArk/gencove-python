# OrganizationUsersList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[OrganizationUser]**](OrganizationUser.md) |  |

## Example

```python
from gencove_client.models.organization_users_list200_response import OrganizationUsersList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUsersList200Response from a JSON string
organization_users_list200_response_instance = OrganizationUsersList200Response.from_json(json)
# print the JSON string representation of the object
print(OrganizationUsersList200Response.to_json())

# convert the object into a dict
organization_users_list200_response_dict = organization_users_list200_response_instance.to_dict()
# create an instance of OrganizationUsersList200Response from a dict
organization_users_list200_response_from_dict = OrganizationUsersList200Response.from_dict(organization_users_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
