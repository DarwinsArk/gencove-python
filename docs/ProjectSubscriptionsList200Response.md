# ProjectSubscriptionsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[ProjectSubscription]**](ProjectSubscription.md) |  |

## Example

```python
from gencove_client.models.project_subscriptions_list200_response import ProjectSubscriptionsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSubscriptionsList200Response from a JSON string
project_subscriptions_list200_response_instance = ProjectSubscriptionsList200Response.from_json(json)
# print the JSON string representation of the object
print(ProjectSubscriptionsList200Response.to_json())

# convert the object into a dict
project_subscriptions_list200_response_dict = project_subscriptions_list200_response_instance.to_dict()
# create an instance of ProjectSubscriptionsList200Response from a dict
project_subscriptions_list200_response_from_dict = ProjectSubscriptionsList200Response.from_dict(project_subscriptions_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
