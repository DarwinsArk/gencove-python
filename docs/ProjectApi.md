# gencove_client.ProjectApi

All URIs are relative to *https://api.gencove.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_batch_types_list**](ProjectApi.md#project_batch_types_list) | **GET** /api/v2/project-batch-types/{project_id} |
[**project_batches_create**](ProjectApi.md#project_batches_create) | **POST** /api/v2/project-batches/{project_id} |
[**project_batches_list**](ProjectApi.md#project_batches_list) | **GET** /api/v2/project-batches/{project_id} |
[**project_cancel_samples_create**](ProjectApi.md#project_cancel_samples_create) | **POST** /api/v2/project-cancel-samples/{project_id} |
[**project_delete_samples_destroy**](ProjectApi.md#project_delete_samples_destroy) | **DELETE** /api/v2/project-delete-samples/{project_id} |
[**project_hide_samples_create**](ProjectApi.md#project_hide_samples_create) | **POST** /api/v2/project-hide-samples/{project_id} |
[**project_merge_vcfs_create**](ProjectApi.md#project_merge_vcfs_create) | **POST** /api/v2/project-merge-vcfs/{project_id} |
[**project_merge_vcfs_retrieve**](ProjectApi.md#project_merge_vcfs_retrieve) | **GET** /api/v2/project-merge-vcfs/{project_id} |
[**project_organization_users_list**](ProjectApi.md#project_organization_users_list) | **GET** /api/v2/project-organization-users/{project_id} |
[**project_qc_report_retrieve**](ProjectApi.md#project_qc_report_retrieve) | **GET** /api/v2/project-qc-report/{project_id} |
[**project_qc_types_list**](ProjectApi.md#project_qc_types_list) | **GET** /api/v2/project-qc-types/{project_id} |
[**project_quality_control_histogram_retrieve**](ProjectApi.md#project_quality_control_histogram_retrieve) | **GET** /api/v2/project-quality-control-histogram/{project_id} |
[**project_restore_samples_create**](ProjectApi.md#project_restore_samples_create) | **POST** /api/v2/project-restore-samples/{project_id} |
[**project_roles_destroy**](ProjectApi.md#project_roles_destroy) | **DELETE** /api/v2/project-roles/{role_id} |
[**project_roles_retrieve**](ProjectApi.md#project_roles_retrieve) | **GET** /api/v2/project-roles/{role_id} |
[**project_sample_manifests_create**](ProjectApi.md#project_sample_manifests_create) | **POST** /api/v2/project-sample-manifests/{project_id} |
[**project_sample_manifests_retrieve**](ProjectApi.md#project_sample_manifests_retrieve) | **GET** /api/v2/project-sample-manifests/{project_id} |
[**project_samples_copy_create**](ProjectApi.md#project_samples_copy_create) | **POST** /api/v2/project-samples-copy/ |
[**project_samples_create**](ProjectApi.md#project_samples_create) | **POST** /api/v2/project-samples/{project_id} |
[**project_samples_import_create**](ProjectApi.md#project_samples_import_create) | **POST** /api/v2/project-samples-import/ |
[**project_samples_list**](ProjectApi.md#project_samples_list) | **GET** /api/v2/project-samples/{project_id} |
[**project_share_exit_create**](ProjectApi.md#project_share_exit_create) | **POST** /api/v2/project-share-exit/ |
[**project_share_revoke_create**](ProjectApi.md#project_share_revoke_create) | **POST** /api/v2/project-share-revoke/{project_share_id} |
[**project_shares_create**](ProjectApi.md#project_shares_create) | **POST** /api/v2/project-shares/ |
[**project_shares_list**](ProjectApi.md#project_shares_list) | **GET** /api/v2/project-shares/ |
[**project_shares_retrieve**](ProjectApi.md#project_shares_retrieve) | **GET** /api/v2/project-shares/{project_share_id} |
[**project_stats_retrieve**](ProjectApi.md#project_stats_retrieve) | **GET** /api/v2/project-stats/{project_id} |
[**project_subscription_details_destroy**](ProjectApi.md#project_subscription_details_destroy) | **DELETE** /api/v2/project-subscription-details/{subscription_id} |
[**project_subscription_details_retrieve**](ProjectApi.md#project_subscription_details_retrieve) | **GET** /api/v2/project-subscription-details/{subscription_id} |
[**project_subscription_event_types_list**](ProjectApi.md#project_subscription_event_types_list) | **GET** /api/v2/project-subscription-event-types/ |
[**project_subscription_notifications_list**](ProjectApi.md#project_subscription_notifications_list) | **GET** /api/v2/project-subscription-notifications/{subscription_id} |
[**project_subscription_secret_create**](ProjectApi.md#project_subscription_secret_create) | **POST** /api/v2/project-subscription-secret/{subscription_id} |
[**project_subscription_test_create**](ProjectApi.md#project_subscription_test_create) | **POST** /api/v2/project-subscription-test/{subscription_id} |
[**project_subscriptions_create**](ProjectApi.md#project_subscriptions_create) | **POST** /api/v2/project-subscriptions/{project_id} |
[**project_subscriptions_list**](ProjectApi.md#project_subscriptions_list) | **GET** /api/v2/project-subscriptions/{project_id} |
[**project_unhide_samples_create**](ProjectApi.md#project_unhide_samples_create) | **POST** /api/v2/project-unhide-samples/{project_id} |
[**project_users_create**](ProjectApi.md#project_users_create) | **POST** /api/v2/project-users/{project_id} |
[**project_users_list**](ProjectApi.md#project_users_list) | **GET** /api/v2/project-users/{project_id} |
[**projects_create**](ProjectApi.md#projects_create) | **POST** /api/v2/projects/ |
[**projects_delete_destroy**](ProjectApi.md#projects_delete_destroy) | **DELETE** /api/v2/projects-delete/ |
[**projects_hide_create**](ProjectApi.md#projects_hide_create) | **POST** /api/v2/projects-hide/ |
[**projects_list**](ProjectApi.md#projects_list) | **GET** /api/v2/projects/ |
[**projects_partial_update**](ProjectApi.md#projects_partial_update) | **PATCH** /api/v2/projects/{project_id} |
[**projects_retrieve**](ProjectApi.md#projects_retrieve) | **GET** /api/v2/projects/{project_id} |
[**projects_unhide_create**](ProjectApi.md#projects_unhide_create) | **POST** /api/v2/projects-unhide/ |


# **project_batch_types_list**
> PaginatedBatchTypeList project_batch_types_list(project_id, limit=limit, offset=offset)

List batch types that are available for current project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_batch_type_list import PaginatedBatchTypeList
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.project_batch_types_list(project_id, limit=limit, offset=offset)
        print("The response of ProjectApi->project_batch_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_batch_types_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedBatchTypeList**](PaginatedBatchTypeList.md)

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

# **project_batches_create**
> BatchDetail project_batches_create(project_id, batch_create)

Handles batch creation for current project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.batch_create import BatchCreate
from gencove_client.models.batch_detail import BatchDetail
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    batch_create = gencove_client.BatchCreate() # BatchCreate |

    try:
        api_response = api_instance.project_batches_create(project_id, batch_create)
        print("The response of ProjectApi->project_batches_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_batches_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **batch_create** | [**BatchCreate**](BatchCreate.md)|  |

### Return type

[**BatchDetail**](BatchDetail.md)

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

# **project_batches_list**
> PaginatedBatchListList project_batches_list(project_id, limit=limit, offset=offset)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_batch_list_list import PaginatedBatchListList
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.project_batches_list(project_id, limit=limit, offset=offset)
        print("The response of ProjectApi->project_batches_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_batches_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedBatchListList**](PaginatedBatchListList.md)

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

# **project_cancel_samples_create**
> ProjectCancelSamples project_cancel_samples_create(project_id, project_cancel_samples)

View for canceling sample submission to analysis in a project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_cancel_samples import ProjectCancelSamples
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    project_cancel_samples = gencove_client.ProjectCancelSamples() # ProjectCancelSamples |

    try:
        api_response = api_instance.project_cancel_samples_create(project_id, project_cancel_samples)
        print("The response of ProjectApi->project_cancel_samples_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_cancel_samples_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **project_cancel_samples** | [**ProjectCancelSamples**](ProjectCancelSamples.md)|  |

### Return type

[**ProjectCancelSamples**](ProjectCancelSamples.md)

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

# **project_delete_samples_destroy**
> project_delete_samples_destroy(project_id)

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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_instance.project_delete_samples_destroy(project_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_delete_samples_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_hide_samples_create**
> project_hide_samples_create(project_id, sample_hide_unhide)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_hide_unhide import SampleHideUnhide
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    sample_hide_unhide = gencove_client.SampleHideUnhide() # SampleHideUnhide |

    try:
        api_instance.project_hide_samples_create(project_id, sample_hide_unhide)
    except Exception as e:
        print("Exception when calling ProjectApi->project_hide_samples_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **sample_hide_unhide** | [**SampleHideUnhide**](SampleHideUnhide.md)|  |

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_merge_vcfs_create**
> ProjectMergeVCFsJob project_merge_vcfs_create(project_id)

Post takes no parameters since merge_vcfs job parameters are constructed
by the backend.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_merge_vcfs_job import ProjectMergeVCFsJob
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.project_merge_vcfs_create(project_id)
        print("The response of ProjectApi->project_merge_vcfs_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_merge_vcfs_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |

### Return type

[**ProjectMergeVCFsJob**](ProjectMergeVCFsJob.md)

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

# **project_merge_vcfs_retrieve**
> ProjectMergeVCFsJob project_merge_vcfs_retrieve(project_id)

Return last known merge_vcfs job.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_merge_vcfs_job import ProjectMergeVCFsJob
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.project_merge_vcfs_retrieve(project_id)
        print("The response of ProjectApi->project_merge_vcfs_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_merge_vcfs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |

### Return type

[**ProjectMergeVCFsJob**](ProjectMergeVCFsJob.md)

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

# **project_organization_users_list**
> PaginatedOrganizationUserList project_organization_users_list(project_id, limit=limit, offset=offset, search=search)

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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    search = 'search_example' # str | Search users by name, email or id (optional)

    try:
        api_response = api_instance.project_organization_users_list(project_id, limit=limit, offset=offset, search=search)
        print("The response of ProjectApi->project_organization_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_organization_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
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

# **project_qc_report_retrieve**
> project_qc_report_retrieve(project_id, columns=columns)

Retrieve a CSV QC report for the supplied project ID

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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    columns = ["id","client_id","project_id","year","month","day","status","sex_string","snps_min","bases_dedup_mapped_min","call_rate_min","effective_coverage_min","raw_coverage","ancestries"] # List[str] | Specify one or more column names to include in the report. (optional) (default to ["id","client_id","project_id","year","month","day","status","sex_string","snps_min","bases_dedup_mapped_min","call_rate_min","effective_coverage_min","raw_coverage","ancestries"])

    try:
        api_instance.project_qc_report_retrieve(project_id, columns=columns)
    except Exception as e:
        print("Exception when calling ProjectApi->project_qc_report_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **columns** | [**List[str]**](str.md)| Specify one or more column names to include in the report. | [optional] [default to [&quot;id&quot;,&quot;client_id&quot;,&quot;project_id&quot;,&quot;year&quot;,&quot;month&quot;,&quot;day&quot;,&quot;status&quot;,&quot;sex_string&quot;,&quot;snps_min&quot;,&quot;bases_dedup_mapped_min&quot;,&quot;call_rate_min&quot;,&quot;effective_coverage_min&quot;,&quot;raw_coverage&quot;,&quot;ancestries&quot;]]

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

# **project_qc_types_list**
> PaginatedQualityControlTypeList project_qc_types_list(project_id, limit=limit, offset=offset)

List all available QC types for current project

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_quality_control_type_list import PaginatedQualityControlTypeList
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.project_qc_types_list(project_id, limit=limit, offset=offset)
        print("The response of ProjectApi->project_qc_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_qc_types_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedQualityControlTypeList**](PaginatedQualityControlTypeList.md)

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

# **project_quality_control_histogram_retrieve**
> ProjectQualityControlHistogram project_quality_control_histogram_retrieve(project_id, qc_type, archive_status=archive_status, created_after=created_after, created_before=created_before, hidden_status=hidden_status, modified_after=modified_after, modified_before=modified_before, number_of_results=number_of_results, search=search, search_by=search_by, status=status)

Retrieve user project and desired qc results histogram.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_quality_control_histogram import ProjectQualityControlHistogram
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    qc_type = 'qc_type_example' # str | Quality control type key
    archive_status = 'archive_status_example' # str | Filter QC results by samples and their archived status (optional)
    created_after = 'created_after_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    created_before = 'created_before_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    hidden_status = 'hidden_status_example' # str | Filter QC results by samples and their hidden status (optional)
    modified_after = 'modified_after_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    modified_before = 'modified_before_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    number_of_results = 200 # int | Number of results (optional) (default to 200)
    search = 'search_example' # str | Search QC results by samples and their id or client id (optional)
    search_by = 'search_by_example' # str | Scope the search to a single field; defaults to 'any' which searches sample id, client id, metadata and provider kit id simultaneously (optional)
    status = 'status_example' # str | Filter QC results by samples and their status (optional)

    try:
        api_response = api_instance.project_quality_control_histogram_retrieve(project_id, qc_type, archive_status=archive_status, created_after=created_after, created_before=created_before, hidden_status=hidden_status, modified_after=modified_after, modified_before=modified_before, number_of_results=number_of_results, search=search, search_by=search_by, status=status)
        print("The response of ProjectApi->project_quality_control_histogram_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_quality_control_histogram_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **qc_type** | **str**| Quality control type key |
 **archive_status** | **str**| Filter QC results by samples and their archived status | [optional]
 **created_after** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **created_before** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **hidden_status** | **str**| Filter QC results by samples and their hidden status | [optional]
 **modified_after** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **modified_before** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **number_of_results** | **int**| Number of results | [optional] [default to 200]
 **search** | **str**| Search QC results by samples and their id or client id | [optional]
 **search_by** | **str**| Scope the search to a single field; defaults to &#39;any&#39; which searches sample id, client id, metadata and provider kit id simultaneously | [optional]
 **status** | **str**| Filter QC results by samples and their status | [optional]

### Return type

[**ProjectQualityControlHistogram**](ProjectQualityControlHistogram.md)

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

# **project_restore_samples_create**
> SampleRestore project_restore_samples_create(project_id, sample_restore)

Handles sample restore process for given sample ids in current project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_restore import SampleRestore
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    sample_restore = gencove_client.SampleRestore() # SampleRestore |

    try:
        api_response = api_instance.project_restore_samples_create(project_id, sample_restore)
        print("The response of ProjectApi->project_restore_samples_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_restore_samples_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **sample_restore** | [**SampleRestore**](SampleRestore.md)|  |

### Return type

[**SampleRestore**](SampleRestore.md)

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

# **project_roles_destroy**
> project_roles_destroy(role_id)

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
    api_instance = gencove_client.ProjectApi(api_client)
    role_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_instance.project_roles_destroy(role_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_roles_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **UUID**|  |

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_roles_retrieve**
> UserRoleObject project_roles_retrieve(role_id)

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
    api_instance = gencove_client.ProjectApi(api_client)
    role_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.project_roles_retrieve(role_id)
        print("The response of ProjectApi->project_roles_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_roles_retrieve: %s\n" % e)
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

# **project_sample_manifests_create**
> SampleManifestUpload project_sample_manifests_create(project_id, sample_manifest, sample_manifest2)

Upload sample manifest file for project

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_manifest_upload import SampleManifestUpload
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str | Project ID to add manifest to
    sample_manifest = 'sample_manifest_example' # str | Sample manifest CSV or XLSX file
    sample_manifest2 = 'sample_manifest_example' # str |

    try:
        api_response = api_instance.project_sample_manifests_create(project_id, sample_manifest, sample_manifest2)
        print("The response of ProjectApi->project_sample_manifests_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_sample_manifests_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID to add manifest to |
 **sample_manifest** | **str**| Sample manifest CSV or XLSX file |
 **sample_manifest2** | **str**|  |

### Return type

[**SampleManifestUpload**](SampleManifestUpload.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_sample_manifests_retrieve**
> SampleManifestUpload project_sample_manifests_retrieve(project_id)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_manifest_upload import SampleManifestUpload
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.project_sample_manifests_retrieve(project_id)
        print("The response of ProjectApi->project_sample_manifests_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_sample_manifests_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |

### Return type

[**SampleManifestUpload**](SampleManifestUpload.md)

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

# **project_samples_copy_create**
> ProjectSamplesImport project_samples_copy_create(project_samples_import)

Copy samples from another project into this one.

Creates independent copies of the source samples in the destination
project, producing new sample records. Only available when the
organization has sample copying enabled.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_samples_import import ProjectSamplesImport
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_samples_import = gencove_client.ProjectSamplesImport() # ProjectSamplesImport |

    try:
        api_response = api_instance.project_samples_copy_create(project_samples_import)
        print("The response of ProjectApi->project_samples_copy_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_samples_copy_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_samples_import** | [**ProjectSamplesImport**](ProjectSamplesImport.md)|  |

### Return type

[**ProjectSamplesImport**](ProjectSamplesImport.md)

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

# **project_samples_create**
> ExtendedSampleSheetCreate project_samples_create(project_id, extended_sample_sheet_create)

Add samples to the project.

Samples are added formatted as the `results` response value that was returned from
`/sample-sheet/` endpoint.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.extended_sample_sheet_create import ExtendedSampleSheetCreate
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    extended_sample_sheet_create = gencove_client.ExtendedSampleSheetCreate() # ExtendedSampleSheetCreate |

    try:
        api_response = api_instance.project_samples_create(project_id, extended_sample_sheet_create)
        print("The response of ProjectApi->project_samples_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_samples_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **extended_sample_sheet_create** | [**ExtendedSampleSheetCreate**](ExtendedSampleSheetCreate.md)|  |

### Return type

[**ExtendedSampleSheetCreate**](ExtendedSampleSheetCreate.md)

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

# **project_samples_import_create**
> ProjectSamplesImport project_samples_import_create(project_samples_import)

Import samples from another project into this one.

References the source samples in the destination project without
duplicating the underlying data. Sample metadata can optionally be
overridden as part of the import.

Source and destination projects must expect the same input type - FASTQ,
CRAM or array data. Whichever the type, the new sample is run from the
source sample's delivered files, so importing a sample never depends on the
object the source project was originally created from.

Note for API consumers: a destination project that expects a different
input type used to be rejected before the request body was read, returning
a bare top-level list. That check now runs alongside the source projects,
so the error arrives under the "samples" key like every other validation
error from this endpoint.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_samples_import import ProjectSamplesImport
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_samples_import = gencove_client.ProjectSamplesImport() # ProjectSamplesImport |

    try:
        api_response = api_instance.project_samples_import_create(project_samples_import)
        print("The response of ProjectApi->project_samples_import_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_samples_import_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_samples_import** | [**ProjectSamplesImport**](ProjectSamplesImport.md)|  |

### Return type

[**ProjectSamplesImport**](ProjectSamplesImport.md)

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

# **project_samples_list**
> PaginatedSampleListList project_samples_list(project_id, archive_status=archive_status, created_after=created_after, created_before=created_before, hidden_status=hidden_status, limit=limit, modified_after=modified_after, modified_before=modified_before, offset=offset, search=search, search_by=search_by, sort_by=sort_by, sort_order=sort_order, status=status)

List single project's associated samples.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_sample_list_list import PaginatedSampleListList
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    archive_status = 'archive_status_example' # str | Filter samples by their archive status (optional)
    created_after = 'created_after_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    created_before = 'created_before_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    hidden_status = 'hidden_status_example' # str | Filter samples by their hidden status (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    modified_after = 'modified_after_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    modified_before = 'modified_before_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    search = 'search_example' # str | Search samples by id or client id or metadata content (optional)
    search_by = 'search_by_example' # str | Scope the search to a single field; defaults to 'any' which searches sample id, client id, metadata and provider kit id simultaneously (optional)
    sort_by = 'sort_by_example' # str | Sort results (optional)
    sort_order = 'sort_order_example' # str | Sort direction (optional)
    status = 'status_example' # str | Filter samples by their status (optional)

    try:
        api_response = api_instance.project_samples_list(project_id, archive_status=archive_status, created_after=created_after, created_before=created_before, hidden_status=hidden_status, limit=limit, modified_after=modified_after, modified_before=modified_before, offset=offset, search=search, search_by=search_by, sort_by=sort_by, sort_order=sort_order, status=status)
        print("The response of ProjectApi->project_samples_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_samples_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **archive_status** | **str**| Filter samples by their archive status | [optional]
 **created_after** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **created_before** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **hidden_status** | **str**| Filter samples by their hidden status | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **modified_after** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **modified_before** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **search** | **str**| Search samples by id or client id or metadata content | [optional]
 **search_by** | **str**| Scope the search to a single field; defaults to &#39;any&#39; which searches sample id, client id, metadata and provider kit id simultaneously | [optional]
 **sort_by** | **str**| Sort results | [optional]
 **sort_order** | **str**| Sort direction | [optional]
 **status** | **str**| Filter samples by their status | [optional]

### Return type

[**PaginatedSampleListList**](PaginatedSampleListList.md)

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

# **project_share_exit_create**
> project_share_exit_create(project_share_exit)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_share_exit import ProjectShareExit
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_share_exit = gencove_client.ProjectShareExit() # ProjectShareExit |

    try:
        api_instance.project_share_exit_create(project_share_exit)
    except Exception as e:
        print("Exception when calling ProjectApi->project_share_exit_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_share_exit** | [**ProjectShareExit**](ProjectShareExit.md)|  |

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_share_revoke_create**
> ProjectShareRevoke project_share_revoke_create(project_share_id, project_share_revoke)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_share_revoke import ProjectShareRevoke
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_share_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    project_share_revoke = gencove_client.ProjectShareRevoke() # ProjectShareRevoke |

    try:
        api_response = api_instance.project_share_revoke_create(project_share_id, project_share_revoke)
        print("The response of ProjectApi->project_share_revoke_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_share_revoke_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_share_id** | **UUID**|  |
 **project_share_revoke** | [**ProjectShareRevoke**](ProjectShareRevoke.md)|  |

### Return type

[**ProjectShareRevoke**](ProjectShareRevoke.md)

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

# **project_shares_create**
> ProjectShare project_shares_create(project_share)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_share import ProjectShare
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_share = gencove_client.ProjectShare() # ProjectShare |

    try:
        api_response = api_instance.project_shares_create(project_share)
        print("The response of ProjectApi->project_shares_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_shares_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_share** | [**ProjectShare**](ProjectShare.md)|  |

### Return type

[**ProjectShare**](ProjectShare.md)

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

# **project_shares_list**
> PaginatedProjectShareList project_shares_list(limit=limit, offset=offset)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_project_share_list import PaginatedProjectShareList
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
    api_instance = gencove_client.ProjectApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.project_shares_list(limit=limit, offset=offset)
        print("The response of ProjectApi->project_shares_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_shares_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedProjectShareList**](PaginatedProjectShareList.md)

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

# **project_shares_retrieve**
> ProjectShare project_shares_retrieve(project_share_id)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_share import ProjectShare
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_share_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.project_shares_retrieve(project_share_id)
        print("The response of ProjectApi->project_shares_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_shares_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_share_id** | **UUID**|  |

### Return type

[**ProjectShare**](ProjectShare.md)

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

# **project_stats_retrieve**
> ProjectStats project_stats_retrieve(project_id, archive_status=archive_status, created_after=created_after, created_before=created_before, hidden_status=hidden_status, modified_after=modified_after, modified_before=modified_before, search=search, search_by=search_by, status=status)

Retrieve user project and it's sample stats.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_stats import ProjectStats
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    archive_status = 'archive_status_example' # str | Filter stats by samples and their archived status (optional)
    created_after = 'created_after_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    created_before = 'created_before_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    hidden_status = 'hidden_status_example' # str | Filter stats by samples and their hidden status (optional)
    modified_after = 'modified_after_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    modified_before = 'modified_before_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    search = 'search_example' # str | Search stats by samples and their id or client id (optional)
    search_by = 'search_by_example' # str | Scope the search to a single field; defaults to 'any' which searches sample id, client id, metadata and provider kit id simultaneously (optional)
    status = 'status_example' # str | Filter stats by samples and their status (optional)

    try:
        api_response = api_instance.project_stats_retrieve(project_id, archive_status=archive_status, created_after=created_after, created_before=created_before, hidden_status=hidden_status, modified_after=modified_after, modified_before=modified_before, search=search, search_by=search_by, status=status)
        print("The response of ProjectApi->project_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **archive_status** | **str**| Filter stats by samples and their archived status | [optional]
 **created_after** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **created_before** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **hidden_status** | **str**| Filter stats by samples and their hidden status | [optional]
 **modified_after** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **modified_before** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **search** | **str**| Search stats by samples and their id or client id | [optional]
 **search_by** | **str**| Scope the search to a single field; defaults to &#39;any&#39; which searches sample id, client id, metadata and provider kit id simultaneously | [optional]
 **status** | **str**| Filter stats by samples and their status | [optional]

### Return type

[**ProjectStats**](ProjectStats.md)

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

# **project_subscription_details_destroy**
> project_subscription_details_destroy(subscription_id)

Details of a single subscription for project related events.

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
    api_instance = gencove_client.ProjectApi(api_client)
    subscription_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_instance.project_subscription_details_destroy(subscription_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_details_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **UUID**|  |

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_subscription_details_retrieve**
> ProjectSubscription project_subscription_details_retrieve(subscription_id)

Details of a single subscription for project related events.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_subscription import ProjectSubscription
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
    api_instance = gencove_client.ProjectApi(api_client)
    subscription_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.project_subscription_details_retrieve(subscription_id)
        print("The response of ProjectApi->project_subscription_details_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_details_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **UUID**|  |

### Return type

[**ProjectSubscription**](ProjectSubscription.md)

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

# **project_subscription_event_types_list**
> PaginatedEventTypeList project_subscription_event_types_list(limit=limit, offset=offset)

List subscription event types that are available for all projects.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_event_type_list import PaginatedEventTypeList
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
    api_instance = gencove_client.ProjectApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.project_subscription_event_types_list(limit=limit, offset=offset)
        print("The response of ProjectApi->project_subscription_event_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_event_types_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedEventTypeList**](PaginatedEventTypeList.md)

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

# **project_subscription_notifications_list**
> PaginatedProjectSubscriptionNotificationList project_subscription_notifications_list(subscription_id, limit=limit, offset=offset)

List all available subscriptions for given project or create a new
subscription.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_project_subscription_notification_list import PaginatedProjectSubscriptionNotificationList
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
    api_instance = gencove_client.ProjectApi(api_client)
    subscription_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.project_subscription_notifications_list(subscription_id, limit=limit, offset=offset)
        print("The response of ProjectApi->project_subscription_notifications_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_notifications_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **UUID**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedProjectSubscriptionNotificationList**](PaginatedProjectSubscriptionNotificationList.md)

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

# **project_subscription_secret_create**
> SubscriptionSecret project_subscription_secret_create(subscription_id)

Set webhook secret for given subscription.

Webhook secret is requested by the user and generated by Gencove.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.subscription_secret import SubscriptionSecret
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
    api_instance = gencove_client.ProjectApi(api_client)
    subscription_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.project_subscription_secret_create(subscription_id)
        print("The response of ProjectApi->project_subscription_secret_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_secret_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **UUID**|  |

### Return type

[**SubscriptionSecret**](SubscriptionSecret.md)

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

# **project_subscription_test_create**
> project_subscription_test_create(subscription_id, subscription_test=subscription_test)

Send a dummy event for given subscription to test notifications integration.
By default, there are no retries for this test endpoint.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.subscription_test import SubscriptionTest
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
    api_instance = gencove_client.ProjectApi(api_client)
    subscription_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    subscription_test = gencove_client.SubscriptionTest() # SubscriptionTest |  (optional)

    try:
        api_instance.project_subscription_test_create(subscription_id, subscription_test=subscription_test)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_test_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **UUID**|  |
 **subscription_test** | [**SubscriptionTest**](SubscriptionTest.md)|  | [optional]

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

# **project_subscriptions_create**
> SubscriptionCreate project_subscriptions_create(project_id, subscription_create)

Add subscription to project events.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.subscription_create import SubscriptionCreate
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    subscription_create = gencove_client.SubscriptionCreate() # SubscriptionCreate |

    try:
        api_response = api_instance.project_subscriptions_create(project_id, subscription_create)
        print("The response of ProjectApi->project_subscriptions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscriptions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **subscription_create** | [**SubscriptionCreate**](SubscriptionCreate.md)|  |

### Return type

[**SubscriptionCreate**](SubscriptionCreate.md)

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

# **project_subscriptions_list**
> PaginatedProjectSubscriptionList project_subscriptions_list(project_id, limit=limit, offset=offset)

List all available subscriptions for given project or create a new
subscription.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_project_subscription_list import PaginatedProjectSubscriptionList
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.project_subscriptions_list(project_id, limit=limit, offset=offset)
        print("The response of ProjectApi->project_subscriptions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscriptions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedProjectSubscriptionList**](PaginatedProjectSubscriptionList.md)

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

# **project_unhide_samples_create**
> project_unhide_samples_create(project_id, sample_hide_unhide)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_hide_unhide import SampleHideUnhide
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    sample_hide_unhide = gencove_client.SampleHideUnhide() # SampleHideUnhide |

    try:
        api_instance.project_unhide_samples_create(project_id, sample_hide_unhide)
    except Exception as e:
        print("Exception when calling ProjectApi->project_unhide_samples_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **sample_hide_unhide** | [**SampleHideUnhide**](SampleHideUnhide.md)|  |

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_users_create**
> UserRoleObject project_users_create(project_id, user_role_object_create)

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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    user_role_object_create = gencove_client.UserRoleObjectCreate() # UserRoleObjectCreate |

    try:
        api_response = api_instance.project_users_create(project_id, user_role_object_create)
        print("The response of ProjectApi->project_users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
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

# **project_users_list**
> PaginatedProjectUsersList project_users_list(project_id, limit=limit, offset=offset, only_explicit_roles=only_explicit_roles, search=search)

Get project users by project id.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_project_users_list import PaginatedProjectUsersList
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    only_explicit_roles = True # bool | Show only project level granted roles (optional)
    search = 'search_example' # str | Search users by name, email or id (optional)

    try:
        api_response = api_instance.project_users_list(project_id, limit=limit, offset=offset, only_explicit_roles=only_explicit_roles, search=search)
        print("The response of ProjectApi->project_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **only_explicit_roles** | **bool**| Show only project level granted roles | [optional]
 **search** | **str**| Search users by name, email or id | [optional]

### Return type

[**PaginatedProjectUsersList**](PaginatedProjectUsersList.md)

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

# **projects_create**
> Project projects_create(project)

Create project

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project import Project
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
    api_instance = gencove_client.ProjectApi(api_client)
    project = gencove_client.Project() # Project |

    try:
        api_response = api_instance.projects_create(project)
        print("The response of ProjectApi->projects_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)|  |

### Return type

[**Project**](Project.md)

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

# **projects_delete_destroy**
> projects_delete_destroy()

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
    api_instance = gencove_client.ProjectApi(api_client)

    try:
        api_instance.projects_delete_destroy()
    except Exception as e:
        print("Exception when calling ProjectApi->projects_delete_destroy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_hide_create**
> projects_hide_create(project_hide_unhide)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_hide_unhide import ProjectHideUnhide
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_hide_unhide = gencove_client.ProjectHideUnhide() # ProjectHideUnhide |

    try:
        api_instance.projects_hide_create(project_hide_unhide)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_hide_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_hide_unhide** | [**ProjectHideUnhide**](ProjectHideUnhide.md)|  |

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list**
> PaginatedProjectList projects_list(additional_permission=additional_permission, hidden_status=hidden_status, limit=limit, locked=locked, offset=offset, search=search, shared=shared, sort_by=sort_by, sort_order=sort_order, status=status)

Retrieve list of user projects.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_project_list import PaginatedProjectList
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
    api_instance = gencove_client.ProjectApi(api_client)
    additional_permission = 'additional_permission_example' # str | Additional permission (optional)
    hidden_status = 'hidden_status_example' # str | Filter projects by their hidden status (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    locked = True # bool | Filter projects by locked status (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    search = 'search_example' # str | A search term. (optional)
    shared = True # bool | Filter projects by shared status (optional)
    sort_by = 'sort_by_example' # str | Sort results (optional)
    sort_order = 'sort_order_example' # str | Sort direction (optional)
    status = 'status_example' # str | Filter projects by sample statuses (optional)

    try:
        api_response = api_instance.projects_list(additional_permission=additional_permission, hidden_status=hidden_status, limit=limit, locked=locked, offset=offset, search=search, shared=shared, sort_by=sort_by, sort_order=sort_order, status=status)
        print("The response of ProjectApi->projects_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_permission** | **str**| Additional permission | [optional]
 **hidden_status** | **str**| Filter projects by their hidden status | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **locked** | **bool**| Filter projects by locked status | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **search** | **str**| A search term. | [optional]
 **shared** | **bool**| Filter projects by shared status | [optional]
 **sort_by** | **str**| Sort results | [optional]
 **sort_order** | **str**| Sort direction | [optional]
 **status** | **str**| Filter projects by sample statuses | [optional]

### Return type

[**PaginatedProjectList**](PaginatedProjectList.md)

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

# **projects_partial_update**
> Project projects_partial_update(project_id, patched_project=patched_project)

Update single project details

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.patched_project import PatchedProject
from gencove_client.models.project import Project
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    patched_project = gencove_client.PatchedProject() # PatchedProject |  (optional)

    try:
        api_response = api_instance.projects_partial_update(project_id, patched_project=patched_project)
        print("The response of ProjectApi->projects_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |
 **patched_project** | [**PatchedProject**](PatchedProject.md)|  | [optional]

### Return type

[**Project**](Project.md)

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

# **projects_retrieve**
> ProjectDetail projects_retrieve(project_id)

Fetch single project details

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_detail import ProjectDetail
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.projects_retrieve(project_id)
        print("The response of ProjectApi->projects_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  |

### Return type

[**ProjectDetail**](ProjectDetail.md)

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

# **projects_unhide_create**
> projects_unhide_create(project_hide_unhide)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_hide_unhide import ProjectHideUnhide
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_hide_unhide = gencove_client.ProjectHideUnhide() # ProjectHideUnhide |

    try:
        api_instance.projects_unhide_create(project_hide_unhide)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_unhide_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_hide_unhide** | [**ProjectHideUnhide**](ProjectHideUnhide.md)|  |

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
