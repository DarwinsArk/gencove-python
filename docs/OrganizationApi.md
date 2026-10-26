# gencove_client.OrganizationApi

All URIs are relative to *https://api.gencove.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_monthly_usage_report_retrieve**](OrganizationApi.md#organization_monthly_usage_report_retrieve) | **GET** /api/v2/organization-monthly-usage-report/ |
[**organization_partial_update**](OrganizationApi.md#organization_partial_update) | **PATCH** /api/v2/organization/ |
[**organization_retrieve**](OrganizationApi.md#organization_retrieve) | **GET** /api/v2/organization/ |
[**organization_roles_retrieve**](OrganizationApi.md#organization_roles_retrieve) | **GET** /api/v2/organization-roles/{role_id} |
[**organization_users_create**](OrganizationApi.md#organization_users_create) | **POST** /api/v2/organization-users/ |
[**organization_users_list**](OrganizationApi.md#organization_users_list) | **GET** /api/v2/organization-users/ |
[**organization_users_partial_update**](OrganizationApi.md#organization_users_partial_update) | **PATCH** /api/v2/organization-users/{user_id} |


# **organization_monthly_usage_report_retrieve**
> organization_monthly_usage_report_retrieve(var_from=var_from, to=to)

Retrieve CSV monthly usage report. Optionally specify a date range.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
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
    api_instance = gencove_client.OrganizationApi(api_client)
    var_from = 'var_from_example' # str | Start date for report. Format is YYYY-MM, e.g. 2023-01. Must supply both 'from' and 'to' parameters. (optional)
    to = 'to_example' # str | End date for report. Format is YYYY-MM, e.g. 2023-05. Must supply both 'from' and 'to' parameters. (optional)

    try:
        api_instance.organization_monthly_usage_report_retrieve(var_from=var_from, to=to)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_monthly_usage_report_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| Start date for report. Format is YYYY-MM, e.g. 2023-01. Must supply both &#39;from&#39; and &#39;to&#39; parameters. | [optional]
 **to** | **str**| End date for report. Format is YYYY-MM, e.g. 2023-05. Must supply both &#39;from&#39; and &#39;to&#39; parameters. | [optional]

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_partial_update**
> Organization organization_partial_update(patched_organization=patched_organization)

Update organization details

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.organization import Organization
from gencove_client.models.patched_organization import PatchedOrganization
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
    api_instance = gencove_client.OrganizationApi(api_client)
    patched_organization = gencove_client.PatchedOrganization() # PatchedOrganization |  (optional)

    try:
        api_response = api_instance.organization_partial_update(patched_organization=patched_organization)
        print("The response of OrganizationApi->organization_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_organization** | [**PatchedOrganization**](PatchedOrganization.md)|  | [optional]

### Return type

[**Organization**](Organization.md)

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

# **organization_retrieve**
> Organization organization_retrieve()

Fetch organization details

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.organization import Organization
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
    api_instance = gencove_client.OrganizationApi(api_client)

    try:
        api_response = api_instance.organization_retrieve()
        print("The response of OrganizationApi->organization_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Organization**](Organization.md)

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

# **organization_roles_retrieve**
> UserRoleObject organization_roles_retrieve(role_id)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.user_role_object import UserRoleObject
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
    api_instance = gencove_client.OrganizationApi(api_client)
    role_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.organization_roles_retrieve(role_id)
        print("The response of OrganizationApi->organization_roles_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_roles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **UUID**|  |

### Return type

[**UserRoleObject**](UserRoleObject.md)

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

# **organization_users_create**
> UserRoleObject organization_users_create(user_role_object_create)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.user_role_object import UserRoleObject
from gencove_client.models.user_role_object_create import UserRoleObjectCreate
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
    api_instance = gencove_client.OrganizationApi(api_client)
    user_role_object_create = gencove_client.UserRoleObjectCreate() # UserRoleObjectCreate |

    try:
        api_response = api_instance.organization_users_create(user_role_object_create)
        print("The response of OrganizationApi->organization_users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_role_object_create** | [**UserRoleObjectCreate**](UserRoleObjectCreate.md)|  |

### Return type

[**UserRoleObject**](UserRoleObject.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_list**
> PaginatedOrganizationUserList organization_users_list(limit=limit, offset=offset, search=search)

Get organization users.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_organization_user_list import PaginatedOrganizationUserList
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
    api_instance = gencove_client.OrganizationApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    search = 'search_example' # str | Search users by name, email or id (optional)

    try:
        api_response = api_instance.organization_users_list(limit=limit, offset=offset, search=search)
        print("The response of OrganizationApi->organization_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **search** | **str**| Search users by name, email or id | [optional]

### Return type

[**PaginatedOrganizationUserList**](PaginatedOrganizationUserList.md)

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

# **organization_users_partial_update**
> OrganizationUser organization_users_partial_update(user_id, patched_organization_user=patched_organization_user)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.organization_user import OrganizationUser
from gencove_client.models.patched_organization_user import PatchedOrganizationUser
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
    api_instance = gencove_client.OrganizationApi(api_client)
    user_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    patched_organization_user = gencove_client.PatchedOrganizationUser() # PatchedOrganizationUser |  (optional)

    try:
        api_response = api_instance.organization_users_partial_update(user_id, patched_organization_user=patched_organization_user)
        print("The response of OrganizationApi->organization_users_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_users_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**|  |
 **patched_organization_user** | [**PatchedOrganizationUser**](PatchedOrganizationUser.md)|  | [optional]

### Return type

[**OrganizationUser**](OrganizationUser.md)

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
