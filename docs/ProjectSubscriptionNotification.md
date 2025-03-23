# ProjectSubscriptionNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**created** | **datetime** |  | [optional]
**response_status** | **int** |  | [optional]
**notification_event_type** | **str** | notification event type | [optional] [readonly]

## Example

```python
from gencove_client.models.project_subscription_notification import ProjectSubscriptionNotification

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSubscriptionNotification from a JSON string
project_subscription_notification_instance = ProjectSubscriptionNotification.from_json(json)
# print the JSON string representation of the object
print(ProjectSubscriptionNotification.to_json())

# convert the object into a dict
project_subscription_notification_dict = project_subscription_notification_instance.to_dict()
# create an instance of ProjectSubscriptionNotification from a dict
project_subscription_notification_from_dict = ProjectSubscriptionNotification.from_dict(project_subscription_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
