# PaginatedProjectSubscriptionNotificationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PaginatedAPIKeyListMeta**](PaginatedAPIKeyListMeta.md) |  | [optional]
**results** | [**List[ProjectSubscriptionNotification]**](ProjectSubscriptionNotification.md) |  |

## Example

```python
from gencove_client.models.paginated_project_subscription_notification_list import PaginatedProjectSubscriptionNotificationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProjectSubscriptionNotificationList from a JSON string
paginated_project_subscription_notification_list_instance = PaginatedProjectSubscriptionNotificationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProjectSubscriptionNotificationList.to_json())

# convert the object into a dict
paginated_project_subscription_notification_list_dict = paginated_project_subscription_notification_list_instance.to_dict()
# create an instance of PaginatedProjectSubscriptionNotificationList from a dict
paginated_project_subscription_notification_list_from_dict = PaginatedProjectSubscriptionNotificationList.from_dict(paginated_project_subscription_notification_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
