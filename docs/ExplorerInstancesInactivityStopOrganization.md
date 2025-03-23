# ExplorerInstancesInactivityStopOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explorer_override_stop_after_inactivity_hours** | **bool** |  |
**explorer_stop_after_inactivity_hours** | **int** | After how many hours of inactivity should an explorer instance be stopped. If org.explorer_override_stop_after_inactivity_hours or instance.stop_after_inactivity_hours is None, then: 0 -&gt; do not stop instances; Any number -&gt; amount of hours to wait before stopping instances. Otherwise, use instance.stop_after_inactivity_hours. |

## Example

```python
from gencove_client.models.explorer_instances_inactivity_stop_organization import ExplorerInstancesInactivityStopOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerInstancesInactivityStopOrganization from a JSON string
explorer_instances_inactivity_stop_organization_instance = ExplorerInstancesInactivityStopOrganization.from_json(json)
# print the JSON string representation of the object
print(ExplorerInstancesInactivityStopOrganization.to_json())

# convert the object into a dict
explorer_instances_inactivity_stop_organization_dict = explorer_instances_inactivity_stop_organization_instance.to_dict()
# create an instance of ExplorerInstancesInactivityStopOrganization from a dict
explorer_instances_inactivity_stop_organization_from_dict = ExplorerInstancesInactivityStopOrganization.from_dict(explorer_instances_inactivity_stop_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
