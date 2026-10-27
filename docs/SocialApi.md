# gencove_client.SocialApi

All URIs are relative to *https://api.gencove.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**social_disconnect_create**](SocialApi.md#social_disconnect_create) | **POST** /api/v2/social-disconnect/ |
[**social_providers_list**](SocialApi.md#social_providers_list) | **GET** /api/v2/social-providers/ |
[**social_signup_create**](SocialApi.md#social_signup_create) | **POST** /api/v2/social-signup/ |


# **social_disconnect_create**
> SocialDisconnect social_disconnect_create(social_disconnect)

Disconnect given providers' social account from current user.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.social_disconnect import SocialDisconnect
from gencove_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gencove.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gencove_client.Configuration(
    host = "https://api.gencove.com"
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
    api_instance = gencove_client.SocialApi(api_client)
    social_disconnect = gencove_client.SocialDisconnect() # SocialDisconnect |

    try:
        api_response = api_instance.social_disconnect_create(social_disconnect)
        print("The response of SocialApi->social_disconnect_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->social_disconnect_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_disconnect** | [**SocialDisconnect**](SocialDisconnect.md)|  |

### Return type

[**SocialDisconnect**](SocialDisconnect.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **social_providers_list**
> PaginatedSocialProviderList social_providers_list(limit=limit, name=name, offset=offset)

Return all available social providers, their autorization urls and user
connected accounts.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_social_provider_list import PaginatedSocialProviderList
from gencove_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gencove.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gencove_client.Configuration(
    host = "https://api.gencove.com"
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
    api_instance = gencove_client.SocialApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str | Filter social providers by name (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.social_providers_list(limit=limit, name=name, offset=offset)
        print("The response of SocialApi->social_providers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->social_providers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **name** | **str**| Filter social providers by name | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedSocialProviderList**](PaginatedSocialProviderList.md)

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

# **social_signup_create**
> SocialSignUp social_signup_create(social_sign_up)

Associate Social user with logged in Django user.

In social provider's config, `redirect_uri` or a similar setting should
be pointed to a url managed by the frontend app.
Frontend app should pass on the info from social provider ie.
```
    {
        "provider": "basespace",
        "code": "foobar"
    }
```

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.social_sign_up import SocialSignUp
from gencove_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gencove.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gencove_client.Configuration(
    host = "https://api.gencove.com"
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
    api_instance = gencove_client.SocialApi(api_client)
    social_sign_up = gencove_client.SocialSignUp() # SocialSignUp |

    try:
        api_response = api_instance.social_signup_create(social_sign_up)
        print("The response of SocialApi->social_signup_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->social_signup_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_sign_up** | [**SocialSignUp**](SocialSignUp.md)|  |

### Return type

[**SocialSignUp**](SocialSignUp.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
