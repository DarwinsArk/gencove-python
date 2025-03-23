# gencove_client.BasespaceApi

All URIs are relative to *https://api.gencove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**basespace_biosamples_import_create**](BasespaceApi.md#basespace_biosamples_import_create) | **POST** /basespace-biosamples-import/ |
[**basespace_project_biosamples_read**](BasespaceApi.md#basespace_project_biosamples_read) | **GET** /basespace-project-biosamples/{basespace_project_id} |
[**basespace_projects_autoimport_create**](BasespaceApi.md#basespace_projects_autoimport_create) | **POST** /basespace-projects-autoimport/ |
[**basespace_projects_autoimport_delete**](BasespaceApi.md#basespace_projects_autoimport_delete) | **DELETE** /basespace-projects-autoimport/{basespace_project_import_id} |
[**basespace_projects_autoimport_list**](BasespaceApi.md#basespace_projects_autoimport_list) | **GET** /basespace-projects-autoimport/ |
[**basespace_projects_import_create**](BasespaceApi.md#basespace_projects_import_create) | **POST** /basespace-projects-import/ |
[**basespace_projects_list**](BasespaceApi.md#basespace_projects_list) | **GET** /basespace-projects/ |


# **basespace_biosamples_import_create**
> BaseSpaceBioSamplesImport basespace_biosamples_import_create(data)



Add BaseSpace biosamples to a Gencove project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.base_space_bio_samples_import import BaseSpaceBioSamplesImport
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
    api_instance = gencove_client.BasespaceApi(api_client)
    data = gencove_client.BaseSpaceBioSamplesImport() # BaseSpaceBioSamplesImport |

    try:
        api_response = api_instance.basespace_biosamples_import_create(data)
        print("The response of BasespaceApi->basespace_biosamples_import_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasespaceApi->basespace_biosamples_import_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**BaseSpaceBioSamplesImport**](BaseSpaceBioSamplesImport.md)|  |

### Return type

[**BaseSpaceBioSamplesImport**](BaseSpaceBioSamplesImport.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **basespace_project_biosamples_read**
> BasespaceProjectBiosamplesRead200Response basespace_project_biosamples_read(basespace_project_id, sort_by=sort_by, sort_order=sort_order)



List currently logged in user's biosamples in a BaseSpace project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.basespace_project_biosamples_read200_response import BasespaceProjectBiosamplesRead200Response
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
    api_instance = gencove_client.BasespaceApi(api_client)
    basespace_project_id = 'basespace_project_id_example' # str |
    sort_by = 'sort_by_example' # str | Sort results (optional)
    sort_order = 'sort_order_example' # str | Sort direction (optional)

    try:
        api_response = api_instance.basespace_project_biosamples_read(basespace_project_id, sort_by=sort_by, sort_order=sort_order)
        print("The response of BasespaceApi->basespace_project_biosamples_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasespaceApi->basespace_project_biosamples_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basespace_project_id** | **str**|  |
 **sort_by** | **str**| Sort results | [optional]
 **sort_order** | **str**| Sort direction | [optional]

### Return type

[**BasespaceProjectBiosamplesRead200Response**](BasespaceProjectBiosamplesRead200Response.md)

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

# **basespace_projects_autoimport_create**
> BaseSpaceProjectsAutoimportCreate basespace_projects_autoimport_create(data)



Creates new autoimport job, if the job already exists updates metadata.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.base_space_projects_autoimport import BaseSpaceProjectsAutoimport
from gencove_client.models.base_space_projects_autoimport_create import BaseSpaceProjectsAutoimportCreate
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
    api_instance = gencove_client.BasespaceApi(api_client)
    data = gencove_client.BaseSpaceProjectsAutoimport() # BaseSpaceProjectsAutoimport |

    try:
        api_response = api_instance.basespace_projects_autoimport_create(data)
        print("The response of BasespaceApi->basespace_projects_autoimport_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasespaceApi->basespace_projects_autoimport_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**BaseSpaceProjectsAutoimport**](BaseSpaceProjectsAutoimport.md)|  |

### Return type

[**BaseSpaceProjectsAutoimportCreate**](BaseSpaceProjectsAutoimportCreate.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **basespace_projects_autoimport_delete**
> basespace_projects_autoimport_delete(basespace_project_import_id)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
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
    api_instance = gencove_client.BasespaceApi(api_client)
    basespace_project_import_id = 'basespace_project_import_id_example' # str |

    try:
        api_instance.basespace_projects_autoimport_delete(basespace_project_import_id)
    except Exception as e:
        print("Exception when calling BasespaceApi->basespace_projects_autoimport_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **basespace_project_import_id** | **str**|  |

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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **basespace_projects_autoimport_list**
> BasespaceProjectsAutoimportList200Response basespace_projects_autoimport_list()



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.basespace_projects_autoimport_list200_response import BasespaceProjectsAutoimportList200Response
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
    api_instance = gencove_client.BasespaceApi(api_client)

    try:
        api_response = api_instance.basespace_projects_autoimport_list()
        print("The response of BasespaceApi->basespace_projects_autoimport_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasespaceApi->basespace_projects_autoimport_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BasespaceProjectsAutoimportList200Response**](BasespaceProjectsAutoimportList200Response.md)

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

# **basespace_projects_import_create**
> BaseSpaceProjectsImport basespace_projects_import_create(data)



Add all BaseSpace biosamples from BaseSpace projects to Gencove project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.base_space_projects_import import BaseSpaceProjectsImport
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
    api_instance = gencove_client.BasespaceApi(api_client)
    data = gencove_client.BaseSpaceProjectsImport() # BaseSpaceProjectsImport |

    try:
        api_response = api_instance.basespace_projects_import_create(data)
        print("The response of BasespaceApi->basespace_projects_import_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasespaceApi->basespace_projects_import_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**BaseSpaceProjectsImport**](BaseSpaceProjectsImport.md)|  |

### Return type

[**BaseSpaceProjectsImport**](BaseSpaceProjectsImport.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **basespace_projects_list**
> BasespaceProjectsList200Response basespace_projects_list(sort_by=sort_by, sort_order=sort_order)



List currently logged in user's BaseSpace projects.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.basespace_projects_list200_response import BasespaceProjectsList200Response
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
    api_instance = gencove_client.BasespaceApi(api_client)
    sort_by = 'sort_by_example' # str | Sort results (optional)
    sort_order = 'sort_order_example' # str | Sort direction (optional)

    try:
        api_response = api_instance.basespace_projects_list(sort_by=sort_by, sort_order=sort_order)
        print("The response of BasespaceApi->basespace_projects_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasespaceApi->basespace_projects_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Sort results | [optional]
 **sort_order** | **str**| Sort direction | [optional]

### Return type

[**BasespaceProjectsList200Response**](BasespaceProjectsList200Response.md)

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
