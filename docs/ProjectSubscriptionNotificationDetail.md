# ProjectSubscriptionNotificationDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**created** | **datetime** |  | [optional]
**response_status** | **int** |  | [optional]
**notification_event_type** | **str** | notification event type | [optional] [readonly]
**response_message** | **str** |  | [optional]
**payload_url** | **str** | presigned s3 url for the payload content | [optional] [readonly]

## Example

```python
from gencove_client.models.project_subscription_notification_detail import ProjectSubscriptionNotificationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSubscriptionNotificationDetail from a JSON string
project_subscription_notification_detail_instance = ProjectSubscriptionNotificationDetail.from_json(json)
# print the JSON string representation of the object
print(ProjectSubscriptionNotificationDetail.to_json())

# convert the object into a dict
project_subscription_notification_detail_dict = project_subscription_notification_detail_instance.to_dict()
# create an instance of ProjectSubscriptionNotificationDetail from a dict
project_subscription_notification_detail_from_dict = ProjectSubscriptionNotificationDetail.from_dict(project_subscription_notification_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
