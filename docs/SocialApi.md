# gencove_client.SocialApi

All URIs are relative to *https://api.gencove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**social_disconnect_create**](SocialApi.md#social_disconnect_create) | **POST** /social-disconnect/ |
[**social_providers_list**](SocialApi.md#social_providers_list) | **GET** /social-providers/ |
[**social_signup_create**](SocialApi.md#social_signup_create) | **POST** /social-signup/ | Associate Social user with logged in Django user.


# **social_disconnect_create**
> SocialDisconnect social_disconnect_create(data)



Disconnect given providers' social account from current user.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.social_disconnect import SocialDisconnect
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
    api_instance = gencove_client.SocialApi(api_client)
    data = gencove_client.SocialDisconnect() # SocialDisconnect |

    try:
        api_response = api_instance.social_disconnect_create(data)
        print("The response of SocialApi->social_disconnect_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->social_disconnect_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SocialDisconnect**](SocialDisconnect.md)|  |

### Return type

[**SocialDisconnect**](SocialDisconnect.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **social_providers_list**
> SocialProvidersList200Response social_providers_list(name=name)



Return all available social providers, their autorization urls and user connected accounts.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.social_providers_list200_response import SocialProvidersList200Response
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
    api_instance = gencove_client.SocialApi(api_client)
    name = 'name_example' # str | Filter social providers by name (optional)

    try:
        api_response = api_instance.social_providers_list(name=name)
        print("The response of SocialApi->social_providers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->social_providers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter social providers by name | [optional]

### Return type

[**SocialProvidersList200Response**](SocialProvidersList200Response.md)

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
> SocialSignUp social_signup_create(data)

Associate Social user with logged in Django user.

In social provider's config, `redirect_uri` or a similar setting should be pointed to a url managed by the frontend app. Frontend app should pass on the info from social provider ie. ```     {         \"provider\": \"basespace\",         \"code\": \"foobar\"     } ```

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.social_sign_up import SocialSignUp
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
    api_instance = gencove_client.SocialApi(api_client)
    data = gencove_client.SocialSignUp() # SocialSignUp |

    try:
        # Associate Social user with logged in Django user.
        api_response = api_instance.social_signup_create(data)
        print("The response of SocialApi->social_signup_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->social_signup_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SocialSignUp**](SocialSignUp.md)|  |

### Return type

[**SocialSignUp**](SocialSignUp.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
