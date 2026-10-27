# gencove_client.FileApi

All URIs are relative to *https://api.gencove.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_types_list**](FileApi.md#file_types_list) | **GET** /api/v2/file-types/ |
[**files_sha256_retrieve**](FileApi.md#files_sha256_retrieve) | **GET** /api/v2/files/{file_id}.sha256 |


# **file_types_list**
> PaginatedFileTypeList file_types_list(limit=limit, object=object, offset=offset, project_id=project_id)

List all legal file types

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_file_type_list import PaginatedFileTypeList
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
    api_instance = gencove_client.FileApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    object = 'object_example' # str | List file types for a specific object, defaults to sample (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    project_id = 'project_id_example' # str | List file types for a project (optional)

    try:
        api_response = api_instance.file_types_list(limit=limit, object=object, offset=offset, project_id=project_id)
        print("The response of FileApi->file_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->file_types_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **object** | **str**| List file types for a specific object, defaults to sample | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **project_id** | **str**| List file types for a project | [optional]

### Return type

[**PaginatedFileTypeList**](PaginatedFileTypeList.md)

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

# **files_sha256_retrieve**
> files_sha256_retrieve(file_id)

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
    api_instance = gencove_client.FileApi(api_client)
    file_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_instance.files_sha256_retrieve(file_id)
    except Exception as e:
        print("Exception when calling FileApi->files_sha256_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **UUID**|  |

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
