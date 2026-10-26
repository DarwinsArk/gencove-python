# gencove_client.ExplorerApi

All URIs are relative to *https://api.gencove.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explorer_access_url_create**](ExplorerApi.md#explorer_access_url_create) | **POST** /api/v2/explorer-access-url/ |
[**explorer_cost_reporting_list**](ExplorerApi.md#explorer_cost_reporting_list) | **GET** /api/v2/explorer-cost-reporting/ |
[**explorer_data_credentials_create**](ExplorerApi.md#explorer_data_credentials_create) | **POST** /api/v2/explorer-data-credentials/ |
[**explorer_instances_inactivity_stop_create**](ExplorerApi.md#explorer_instances_inactivity_stop_create) | **POST** /api/v2/explorer-instances-inactivity-stop/ |
[**explorer_instances_inactivity_stop_organization_create**](ExplorerApi.md#explorer_instances_inactivity_stop_organization_create) | **POST** /api/v2/explorer-instances-inactivity-stop-organization/ |
[**explorer_instances_inactivity_stop_organization_retrieve**](ExplorerApi.md#explorer_instances_inactivity_stop_organization_retrieve) | **GET** /api/v2/explorer-instances-inactivity-stop-organization/ |
[**explorer_instances_list**](ExplorerApi.md#explorer_instances_list) | **GET** /api/v2/explorer-instances/ |
[**explorer_session_start_create**](ExplorerApi.md#explorer_session_start_create) | **POST** /api/v2/explorer-session-start/ |
[**explorer_shell_session_credentials_create**](ExplorerApi.md#explorer_shell_session_credentials_create) | **POST** /api/v2/explorer-shell-session-credentials/ |
[**explorer_start_instances_create**](ExplorerApi.md#explorer_start_instances_create) | **POST** /api/v2/explorer-start-instances/ |
[**explorer_stop_instances_create**](ExplorerApi.md#explorer_stop_instances_create) | **POST** /api/v2/explorer-stop-instances/ |


# **explorer_access_url_create**
> explorer_access_url_create(explorer_instance_access_url)

Retrieves the Access URL for the given instance.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.explorer_instance_access_url import ExplorerInstanceAccessURL
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
    api_instance = gencove_client.ExplorerApi(api_client)
    explorer_instance_access_url = gencove_client.ExplorerInstanceAccessURL() # ExplorerInstanceAccessURL |

    try:
        api_instance.explorer_access_url_create(explorer_instance_access_url)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_access_url_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **explorer_instance_access_url** | [**ExplorerInstanceAccessURL**](ExplorerInstanceAccessURL.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explorer_cost_reporting_list**
> PaginatedCostReportPeriodList explorer_cost_reporting_list(limit=limit, offset=offset)

The caller's organization's cost report: its months, newest first,
each with one line per category (``costs.report``), the month's total,
whether it is finalized, when it was last computed, and the archived
CSV when the month has one, kept in step with the month's lines
(``costs.report_files``).

Served on the Explorer cost reporting route it replaces, with the field
names that list used. What a reader of that list sees change: ``id``
is the Explorer report record's and null for a month without one;
``report_amount`` is the total of every line the organization may see,
platform lines and adjustments included; ``last_updated`` is the
earliest as-of across the month's lines, null when none carries one;
``covered_through`` and ``categories`` are new.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_cost_report_period_list import PaginatedCostReportPeriodList
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
    api_instance = gencove_client.ExplorerApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.explorer_cost_reporting_list(limit=limit, offset=offset)
        print("The response of ExplorerApi->explorer_cost_reporting_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_cost_reporting_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedCostReportPeriodList**](PaginatedCostReportPeriodList.md)

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

# **explorer_data_credentials_create**
> GetExplorerDataCredentialsResponse explorer_data_credentials_create(get_explorer_data_credentials_response)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.get_explorer_data_credentials_response import GetExplorerDataCredentialsResponse
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
    api_instance = gencove_client.ExplorerApi(api_client)
    get_explorer_data_credentials_response = gencove_client.GetExplorerDataCredentialsResponse() # GetExplorerDataCredentialsResponse |

    try:
        api_response = api_instance.explorer_data_credentials_create(get_explorer_data_credentials_response)
        print("The response of ExplorerApi->explorer_data_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_data_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_explorer_data_credentials_response** | [**GetExplorerDataCredentialsResponse**](GetExplorerDataCredentialsResponse.md)|  |

### Return type

[**GetExplorerDataCredentialsResponse**](GetExplorerDataCredentialsResponse.md)

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

# **explorer_instances_inactivity_stop_create**
> explorer_instances_inactivity_stop_create(explorer_instances_inactivity_stop)

Sets the inactivity threshold for the given instances.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.explorer_instances_inactivity_stop import ExplorerInstancesInactivityStop
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
    api_instance = gencove_client.ExplorerApi(api_client)
    explorer_instances_inactivity_stop = gencove_client.ExplorerInstancesInactivityStop() # ExplorerInstancesInactivityStop |

    try:
        api_instance.explorer_instances_inactivity_stop_create(explorer_instances_inactivity_stop)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_instances_inactivity_stop_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **explorer_instances_inactivity_stop** | [**ExplorerInstancesInactivityStop**](ExplorerInstancesInactivityStop.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explorer_instances_inactivity_stop_organization_create**
> explorer_instances_inactivity_stop_organization_create(explorer_instances_inactivity_stop_organization)

Sets the inactivity treshold for the user's organization.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.explorer_instances_inactivity_stop_organization import ExplorerInstancesInactivityStopOrganization
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
    api_instance = gencove_client.ExplorerApi(api_client)
    explorer_instances_inactivity_stop_organization = gencove_client.ExplorerInstancesInactivityStopOrganization() # ExplorerInstancesInactivityStopOrganization |

    try:
        api_instance.explorer_instances_inactivity_stop_organization_create(explorer_instances_inactivity_stop_organization)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_instances_inactivity_stop_organization_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **explorer_instances_inactivity_stop_organization** | [**ExplorerInstancesInactivityStopOrganization**](ExplorerInstancesInactivityStopOrganization.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explorer_instances_inactivity_stop_organization_retrieve**
> ExplorerInstancesInactivityStopOrganization explorer_instances_inactivity_stop_organization_retrieve()

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.explorer_instances_inactivity_stop_organization import ExplorerInstancesInactivityStopOrganization
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
    api_instance = gencove_client.ExplorerApi(api_client)

    try:
        api_response = api_instance.explorer_instances_inactivity_stop_organization_retrieve()
        print("The response of ExplorerApi->explorer_instances_inactivity_stop_organization_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_instances_inactivity_stop_organization_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ExplorerInstancesInactivityStopOrganization**](ExplorerInstancesInactivityStopOrganization.md)

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

# **explorer_instances_list**
> PaginatedExplorerInstanceList explorer_instances_list(limit=limit, offset=offset)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_explorer_instance_list import PaginatedExplorerInstanceList
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
    api_instance = gencove_client.ExplorerApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.explorer_instances_list(limit=limit, offset=offset)
        print("The response of ExplorerApi->explorer_instances_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_instances_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedExplorerInstanceList**](PaginatedExplorerInstanceList.md)

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

# **explorer_session_start_create**
> ExplorerSessionStartResponse explorer_session_start_create(explorer_session_start)

Start an Explorer session by setting the user_session cookie and returning a clean Explorer URL.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.explorer_session_start import ExplorerSessionStart
from gencove_client.models.explorer_session_start_response import ExplorerSessionStartResponse
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
    api_instance = gencove_client.ExplorerApi(api_client)
    explorer_session_start = gencove_client.ExplorerSessionStart() # ExplorerSessionStart |

    try:
        api_response = api_instance.explorer_session_start_create(explorer_session_start)
        print("The response of ExplorerApi->explorer_session_start_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_session_start_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **explorer_session_start** | [**ExplorerSessionStart**](ExplorerSessionStart.md)|  |

### Return type

[**ExplorerSessionStartResponse**](ExplorerSessionStartResponse.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explorer_shell_session_credentials_create**
> ExplorerShellSessionCredentialsResponse explorer_shell_session_credentials_create(explorer_shell_session_credentials)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.explorer_shell_session_credentials import ExplorerShellSessionCredentials
from gencove_client.models.explorer_shell_session_credentials_response import ExplorerShellSessionCredentialsResponse
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
    api_instance = gencove_client.ExplorerApi(api_client)
    explorer_shell_session_credentials = gencove_client.ExplorerShellSessionCredentials() # ExplorerShellSessionCredentials |

    try:
        api_response = api_instance.explorer_shell_session_credentials_create(explorer_shell_session_credentials)
        print("The response of ExplorerApi->explorer_shell_session_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_shell_session_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **explorer_shell_session_credentials** | [**ExplorerShellSessionCredentials**](ExplorerShellSessionCredentials.md)|  |

### Return type

[**ExplorerShellSessionCredentialsResponse**](ExplorerShellSessionCredentialsResponse.md)

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

# **explorer_start_instances_create**
> explorer_start_instances_create(explorer_instances_start)

Starts the given instances.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.explorer_instances_start import ExplorerInstancesStart
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
    api_instance = gencove_client.ExplorerApi(api_client)
    explorer_instances_start = gencove_client.ExplorerInstancesStart() # ExplorerInstancesStart |

    try:
        api_instance.explorer_start_instances_create(explorer_instances_start)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_start_instances_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **explorer_instances_start** | [**ExplorerInstancesStart**](ExplorerInstancesStart.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explorer_stop_instances_create**
> explorer_stop_instances_create(explorer_instances_stop)

Stops the given instances.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.explorer_instances_stop import ExplorerInstancesStop
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
    api_instance = gencove_client.ExplorerApi(api_client)
    explorer_instances_stop = gencove_client.ExplorerInstancesStop() # ExplorerInstancesStop |

    try:
        api_instance.explorer_stop_instances_create(explorer_instances_stop)
    except Exception as e:
        print("Exception when calling ExplorerApi->explorer_stop_instances_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **explorer_instances_stop** | [**ExplorerInstancesStop**](ExplorerInstancesStop.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
