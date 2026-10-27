# gencove_client.UploadApi

All URIs are relative to *https://api.gencove.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_credentials_create**](UploadApi.md#upload_credentials_create) | **POST** /api/v2/upload-credentials/ |
[**uploads_delete_unassigned_create**](UploadApi.md#uploads_delete_unassigned_create) | **POST** /api/v2/uploads-delete-unassigned/ |
[**uploads_list**](UploadApi.md#uploads_list) | **GET** /api/v2/uploads/ |
[**uploads_post_data_create**](UploadApi.md#uploads_post_data_create) | **POST** /api/v2/uploads-post-data/ |
[**uploads_presigned_post_data_create**](UploadApi.md#uploads_presigned_post_data_create) | **POST** /api/v2/uploads-presigned-post-data/ |
[**uploads_retrieve**](UploadApi.md#uploads_retrieve) | **GET** /api/v2/uploads/{upload_id} |
[**uploads_url_create**](UploadApi.md#uploads_url_create) | **POST** /api/v2/uploads-url/ |


# **upload_credentials_create**
> GetUploadCredentialsResponse upload_credentials_create()

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.get_upload_credentials_response import GetUploadCredentialsResponse
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
    api_instance = gencove_client.UploadApi(api_client)

    try:
        api_response = api_instance.upload_credentials_create()
        print("The response of UploadApi->upload_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->upload_credentials_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUploadCredentialsResponse**](GetUploadCredentialsResponse.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploads_delete_unassigned_create**
> DeletedUnassignedUploads uploads_delete_unassigned_create(deleted_unassigned_uploads)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.deleted_unassigned_uploads import DeletedUnassignedUploads
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
    api_instance = gencove_client.UploadApi(api_client)
    deleted_unassigned_uploads = gencove_client.DeletedUnassignedUploads() # DeletedUnassignedUploads |

    try:
        api_response = api_instance.uploads_delete_unassigned_create(deleted_unassigned_uploads)
        print("The response of UploadApi->uploads_delete_unassigned_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->uploads_delete_unassigned_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleted_unassigned_uploads** | [**DeletedUnassignedUploads**](DeletedUnassignedUploads.md)|  |

### Return type

[**DeletedUnassignedUploads**](DeletedUnassignedUploads.md)

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

# **uploads_list**
> PaginatedUploadList uploads_list(limit=limit, offset=offset, search=search, status=status)

Retrieve list of user uploads.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_upload_list import PaginatedUploadList
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
    api_instance = gencove_client.UploadApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    search = 'search_example' # str | Search uploads by id (optional)
    status = 'status_example' # str | Filter uploads by upload statuses (optional)

    try:
        api_response = api_instance.uploads_list(limit=limit, offset=offset, search=search, status=status)
        print("The response of UploadApi->uploads_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->uploads_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **search** | **str**| Search uploads by id | [optional]
 **status** | **str**| Filter uploads by upload statuses | [optional]

### Return type

[**PaginatedUploadList**](PaginatedUploadList.md)

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

# **uploads_post_data_create**
> UploadPostDataResponse uploads_post_data_create(upload_post_data_create)

Returns info about initialized file upload based on posted file
destination path.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.upload_post_data_create import UploadPostDataCreate
from gencove_client.models.upload_post_data_response import UploadPostDataResponse
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
    api_instance = gencove_client.UploadApi(api_client)
    upload_post_data_create = gencove_client.UploadPostDataCreate() # UploadPostDataCreate |

    try:
        api_response = api_instance.uploads_post_data_create(upload_post_data_create)
        print("The response of UploadApi->uploads_post_data_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->uploads_post_data_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_post_data_create** | [**UploadPostDataCreate**](UploadPostDataCreate.md)|  |

### Return type

[**UploadPostDataResponse**](UploadPostDataResponse.md)

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

# **uploads_presigned_post_data_create**
> UploadPresignedPostDataResponse uploads_presigned_post_data_create(upload_post_data_create)

Returns S3 presigned parameters needed for file upload as response for
given file attributes.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.upload_post_data_create import UploadPostDataCreate
from gencove_client.models.upload_presigned_post_data_response import UploadPresignedPostDataResponse
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
    api_instance = gencove_client.UploadApi(api_client)
    upload_post_data_create = gencove_client.UploadPostDataCreate() # UploadPostDataCreate |

    try:
        api_response = api_instance.uploads_presigned_post_data_create(upload_post_data_create)
        print("The response of UploadApi->uploads_presigned_post_data_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->uploads_presigned_post_data_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_post_data_create** | [**UploadPostDataCreate**](UploadPostDataCreate.md)|  |

### Return type

[**UploadPresignedPostDataResponse**](UploadPresignedPostDataResponse.md)

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

# **uploads_retrieve**
> Upload uploads_retrieve(upload_id)

Fetch single upload details

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.upload import Upload
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
    api_instance = gencove_client.UploadApi(api_client)
    upload_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.uploads_retrieve(upload_id)
        print("The response of UploadApi->uploads_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->uploads_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **UUID**|  |

### Return type

[**Upload**](Upload.md)

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

# **uploads_url_create**
> UploadURLResponse uploads_url_create(upload_url_create)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.upload_url_create import UploadURLCreate
from gencove_client.models.upload_url_response import UploadURLResponse
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
    api_instance = gencove_client.UploadApi(api_client)
    upload_url_create = gencove_client.UploadURLCreate() # UploadURLCreate |

    try:
        api_response = api_instance.uploads_url_create(upload_url_create)
        print("The response of UploadApi->uploads_url_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->uploads_url_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_url_create** | [**UploadURLCreate**](UploadURLCreate.md)|  |

### Return type

[**UploadURLResponse**](UploadURLResponse.md)

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
