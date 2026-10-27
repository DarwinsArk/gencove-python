# ProjectSubscription

Subscription serializer where the scope is a project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**name** | **str** | User identifiable name, if left empty default name with a timestamp is used | [optional]
**project** | **UUID** |  | [readonly]
**target** | **str** | URL if webhook, e-mail address if email |
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) | How is the notification delivered  * &#x60;webhook&#x60; - webhook * &#x60;email&#x60; - email | [readonly]
**event_types** | **List[object]** | event types which will be delivered for current subscription | [readonly]
**has_secret** | **bool** | Is webhook secret set |

## Example

```python
from gencove_client.models.project_subscription import ProjectSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSubscription from a JSON string
project_subscription_instance = ProjectSubscription.from_json(json)
# print the JSON string representation of the object
print(ProjectSubscription.to_json())

# convert the object into a dict
project_subscription_dict = project_subscription_instance.to_dict()
# create an instance of ProjectSubscription from a dict
project_subscription_from_dict = ProjectSubscription.from_dict(project_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
