# ExplorerInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**status** | **str** |  | [optional] [readonly]
**stop_after_inactivity_hours** | **int** | After how many hours of inactivity should an explorer instance be stopped. None -&gt; adhere to org setting. 0 -&gt; do not stop instance. Any number -&gt; amount of hours to wait before stopping instance. If org.explorer_override_stop_after_inactivity_hours is True, this attribute doesn&#39;t have any effects. | [optional]

## Example

```python
from gencove_client.models.explorer_instance import ExplorerInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerInstance from a JSON string
explorer_instance_instance = ExplorerInstance.from_json(json)
# print the JSON string representation of the object
print(ExplorerInstance.to_json())

# convert the object into a dict
explorer_instance_dict = explorer_instance_instance.to_dict()
# create an instance of ExplorerInstance from a dict
explorer_instance_from_dict = ExplorerInstance.from_dict(explorer_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
