# gencove_client.ArrayApi

All URIs are relative to *https://api.gencove.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**array_data_upload_create**](ArrayApi.md#array_data_upload_create) | **POST** /api/v2/array-data-upload/ |
[**array_data_upload_form_create**](ArrayApi.md#array_data_upload_form_create) | **POST** /api/v2/array-data-upload-form/ |


# **array_data_upload_create**
> ArrayDataUploadResponse array_data_upload_create(array_data_upload_create=array_data_upload_create)

Create an array-data upload and return a short-lived presigned upload for a single .zip file.

Post the file as `multipart/form-data` to `upload_url`: send every entry of `upload_fields` as a form field, then the file itself as a field named `file`, which **must be the last field in the body** — anything after it is ignored and the upload is rejected. Send `upload_fields` back exactly as received; the set of keys is storage-provider controlled and may change.

Only `application/zip` is accepted (already prefilled in `upload_fields`), and the file must be no larger than `max_file_size_bytes`. A successful upload returns an empty response with no body.

The upload is valid until `expires_at`. If it lapses or the upload fails, call this endpoint again — that creates a new sample; an existing one cannot be refreshed. Once the file arrives the sample is scheduled for analysis automatically.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.array_data_upload_create import ArrayDataUploadCreate
from gencove_client.models.array_data_upload_response import ArrayDataUploadResponse
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
    api_instance = gencove_client.ArrayApi(api_client)
    array_data_upload_create = gencove_client.ArrayDataUploadCreate() # ArrayDataUploadCreate |  (optional)

    try:
        api_response = api_instance.array_data_upload_create(array_data_upload_create=array_data_upload_create)
        print("The response of ArrayApi->array_data_upload_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArrayApi->array_data_upload_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **array_data_upload_create** | [**ArrayDataUploadCreate**](ArrayDataUploadCreate.md)|  | [optional]

### Return type

[**ArrayDataUploadResponse**](ArrayDataUploadResponse.md)

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

# **array_data_upload_form_create**
> ArrayDataUploadFormResponse array_data_upload_form_create(array_data_upload_form_create=array_data_upload_form_create)

Create a temporary consumer-data upload session.

Auth-gated to ``consumer_provider`` orgs (``org.consumer_mode_enabled``)
and requires the ``upload_create`` role. Each call creates a
``samples.Sample`` in the org's consumer-array-data project and returns a
tokenized URL that the partner hands off to one of their end users.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.array_data_upload_form_create import ArrayDataUploadFormCreate
from gencove_client.models.array_data_upload_form_response import ArrayDataUploadFormResponse
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
    api_instance = gencove_client.ArrayApi(api_client)
    array_data_upload_form_create = gencove_client.ArrayDataUploadFormCreate() # ArrayDataUploadFormCreate |  (optional)

    try:
        api_response = api_instance.array_data_upload_form_create(array_data_upload_form_create=array_data_upload_form_create)
        print("The response of ArrayApi->array_data_upload_form_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArrayApi->array_data_upload_form_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **array_data_upload_form_create** | [**ArrayDataUploadFormCreate**](ArrayDataUploadFormCreate.md)|  | [optional]

### Return type

[**ArrayDataUploadFormResponse**](ArrayDataUploadFormResponse.md)

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
