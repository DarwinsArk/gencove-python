# gencove_client.FirstmileApi

All URIs are relative to *https://api.gencove.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firstmile_s3_role_element_create**](FirstmileApi.md#firstmile_s3_role_element_create) | **POST** /api/v2/firstmile-s3-role-element/ |
[**firstmile_s3_role_element_retrieve**](FirstmileApi.md#firstmile_s3_role_element_retrieve) | **GET** /api/v2/firstmile-s3-role-element/ |
[**firstmile_validate_illumina_samplesheet_create**](FirstmileApi.md#firstmile_validate_illumina_samplesheet_create) | **POST** /api/v2/firstmile-validate-illumina-samplesheet/ |


# **firstmile_s3_role_element_create**
> S3RoleElement firstmile_s3_role_element_create(s3_role_element=s3_role_element)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.s3_role_element import S3RoleElement
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
    api_instance = gencove_client.FirstmileApi(api_client)
    s3_role_element = gencove_client.S3RoleElement() # S3RoleElement |  (optional)

    try:
        api_response = api_instance.firstmile_s3_role_element_create(s3_role_element=s3_role_element)
        print("The response of FirstmileApi->firstmile_s3_role_element_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirstmileApi->firstmile_s3_role_element_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_role_element** | [**S3RoleElement**](S3RoleElement.md)|  | [optional]

### Return type

[**S3RoleElement**](S3RoleElement.md)

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

# **firstmile_s3_role_element_retrieve**
> S3RoleElement firstmile_s3_role_element_retrieve()

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.s3_role_element import S3RoleElement
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
    api_instance = gencove_client.FirstmileApi(api_client)

    try:
        api_response = api_instance.firstmile_s3_role_element_retrieve()
        print("The response of FirstmileApi->firstmile_s3_role_element_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirstmileApi->firstmile_s3_role_element_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**S3RoleElement**](S3RoleElement.md)

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

# **firstmile_validate_illumina_samplesheet_create**
> firstmile_validate_illumina_samplesheet_create(illumina_samplesheet)

Upload Illumina SampleSheet.csv and validate that it conforms with FirstMile demultiplexing
requirements. Under the `[Data]` section, a custom column called `Gencove_Project_ID` must
be present; each sample must contain a valid, existing Gencove project ID value in this
column.

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
    api_instance = gencove_client.FirstmileApi(api_client)
    illumina_samplesheet = None # bytes | Illumina SampleSheet.csv file

    try:
        api_instance.firstmile_validate_illumina_samplesheet_create(illumina_samplesheet)
    except Exception as e:
        print("Exception when calling FirstmileApi->firstmile_validate_illumina_samplesheet_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **illumina_samplesheet** | **bytes**| Illumina SampleSheet.csv file |

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
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
