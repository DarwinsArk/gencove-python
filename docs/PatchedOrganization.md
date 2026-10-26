# PatchedOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] [readonly]
**name** | **str** |  | [optional]
**expire_uploads_period_days** | **int** |  | [optional] [readonly]
**archive_period_days** | **int** |  | [optional] [readonly]
**archive_restore_period_days** | **int** |  | [optional] [readonly]
**roles** | [**Dict[str, UserRoleObject]**](UserRoleObject.md) | Roles in the organization. | [optional] [readonly]
**uploads_enabled** | **bool** | Designates whether the organization can access upload functionality. | [optional] [readonly]
**delete_samples_enabled** | **bool** | Designates whether the organization can delete samples. | [optional] [readonly]
**project_sharing_enabled** | **bool** | When enabled, allows organization to share projects with other organizations. | [optional] [readonly]
**account_on_hold** | **bool** | When enabled, limits ability of organization to manage data and displays UI warning to organization users that invoice is past due. | [optional] [readonly]
**organization_type** | [**OrganizationTypeEnum**](OrganizationTypeEnum.md) | Type of organization  * &#x60;enterprise&#x60; - enterprise * &#x60;consumer&#x60; - consumer * &#x60;consumer_provider&#x60; - consumer provider | [optional] [readonly]
**cross_org_cost_reports_enabled** | **bool** | The organization has cost reports covering organizations it funds. | [optional] [readonly]

## Example

```python
from gencove_client.models.patched_organization import PatchedOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedOrganization from a JSON string
patched_organization_instance = PatchedOrganization.from_json(json)
# print the JSON string representation of the object
print(PatchedOrganization.to_json())

# convert the object into a dict
patched_organization_dict = patched_organization_instance.to_dict()
# create an instance of PatchedOrganization from a dict
patched_organization_from_dict = PatchedOrganization.from_dict(patched_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
