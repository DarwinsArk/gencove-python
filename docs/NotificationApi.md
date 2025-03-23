# gencove_client.NotificationApi

All URIs are relative to *https://api.gencove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_read**](NotificationApi.md#notifications_read) | **GET** /notifications/{notification_id} |


# **notifications_read**
> ProjectSubscriptionNotificationDetail notifications_read(notification_id)



List all available subscriptions for given project or create a new subscription.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_subscription_notification_detail import ProjectSubscriptionNotificationDetail
from gencove_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gencove.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = gencove_client.Configuration(
    host = "https://api.gencove.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API key
configuration.api_key['API key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API key'] = 'Bearer'

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with gencove_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gencove_client.NotificationApi(api_client)
    notification_id = 'notification_id_example' # str |

    try:
        api_response = api_instance.notifications_read(notification_id)
        print("The response of NotificationApi->notifications_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationApi->notifications_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  |

### Return type

[**ProjectSubscriptionNotificationDetail**](ProjectSubscriptionNotificationDetail.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
