# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**name** | **str** |  |
**expire_uploads_period_days** | **int** |  | [optional] [readonly]
**archive_period_days** | **int** |  | [optional] [readonly]
**archive_restore_period_days** | **int** |  | [optional] [readonly]
**roles** | [**Dict[str, UserRoleObject]**](UserRoleObject.md) | Roles in the organization. | [optional] [readonly]
**uploads_enabled** | **bool** | Designates whether the organization can access upload functionality. | [optional] [readonly]
**delete_samples_enabled** | **bool** | Designates whether the organization can delete samples. | [optional] [readonly]
**project_sharing_enabled** | **bool** | When enabled, allows organization to share projects with other organizations. | [optional] [readonly]
**account_on_hold** | **bool** | When enabled, limits ability of organization to manage data and displays UI warning to organization users that invoice is past due. | [optional] [readonly]

## Example

```python
from gencove_client.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
