# ProjectSubscriptionEventTypesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[EventType]**](EventType.md) |  |

## Example

```python
from gencove_client.models.project_subscription_event_types_list200_response import ProjectSubscriptionEventTypesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSubscriptionEventTypesList200Response from a JSON string
project_subscription_event_types_list200_response_instance = ProjectSubscriptionEventTypesList200Response.from_json(json)
# print the JSON string representation of the object
print(ProjectSubscriptionEventTypesList200Response.to_json())

# convert the object into a dict
project_subscription_event_types_list200_response_dict = project_subscription_event_types_list200_response_instance.to_dict()
# create an instance of ProjectSubscriptionEventTypesList200Response from a dict
project_subscription_event_types_list200_response_from_dict = ProjectSubscriptionEventTypesList200Response.from_dict(project_subscription_event_types_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
