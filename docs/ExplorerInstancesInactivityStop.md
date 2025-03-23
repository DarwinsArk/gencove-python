# ExplorerInstancesInactivityStop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_ids** | **List[str]** |  |
**stop_after_inactivity_hours** | **int** | After how many hours of inactivity should an explorer instance be stopped. None -&gt; adhere to org setting. 0 -&gt; do not stop instance. Any number -&gt; amount of hours to wait before stopping instance. If org.explorer_override_stop_after_inactivity_hours is True, this attribute doesn&#39;t have any effects. |

## Example

```python
from gencove_client.models.explorer_instances_inactivity_stop import ExplorerInstancesInactivityStop

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerInstancesInactivityStop from a JSON string
explorer_instances_inactivity_stop_instance = ExplorerInstancesInactivityStop.from_json(json)
# print the JSON string representation of the object
print(ExplorerInstancesInactivityStop.to_json())

# convert the object into a dict
explorer_instances_inactivity_stop_dict = explorer_instances_inactivity_stop_instance.to_dict()
# create an instance of ExplorerInstancesInactivityStop from a dict
explorer_instances_inactivity_stop_from_dict = ExplorerInstancesInactivityStop.from_dict(explorer_instances_inactivity_stop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
