# gencove_client.ProjectApi

All URIs are relative to *https://api.gencove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_batch_types_read**](ProjectApi.md#project_batch_types_read) | **GET** /project-batch-types/{project_id} |
[**project_batches_create**](ProjectApi.md#project_batches_create) | **POST** /project-batches/{project_id} |
[**project_batches_read**](ProjectApi.md#project_batches_read) | **GET** /project-batches/{project_id} |
[**project_cancel_samples_create**](ProjectApi.md#project_cancel_samples_create) | **POST** /project-cancel-samples/{project_id} |
[**project_delete_samples_delete**](ProjectApi.md#project_delete_samples_delete) | **DELETE** /project-delete-samples/{project_id} |
[**project_hide_samples_create**](ProjectApi.md#project_hide_samples_create) | **POST** /project-hide-samples/{project_id} |
[**project_merge_vcfs_create**](ProjectApi.md#project_merge_vcfs_create) | **POST** /project-merge-vcfs/{project_id} |
[**project_merge_vcfs_read**](ProjectApi.md#project_merge_vcfs_read) | **GET** /project-merge-vcfs/{project_id} |
[**project_organization_users_list**](ProjectApi.md#project_organization_users_list) | **GET** /project-organization-users/{project_id} |
[**project_qc_report_read**](ProjectApi.md#project_qc_report_read) | **GET** /project-qc-report/{project_id} |
[**project_qc_types_read**](ProjectApi.md#project_qc_types_read) | **GET** /project-qc-types/{project_id} |
[**project_quality_control_histogram_read**](ProjectApi.md#project_quality_control_histogram_read) | **GET** /project-quality-control-histogram/{project_id} |
[**project_restore_samples_create**](ProjectApi.md#project_restore_samples_create) | **POST** /project-restore-samples/{project_id} |
[**project_roles_delete**](ProjectApi.md#project_roles_delete) | **DELETE** /project-roles/{role_id} |
[**project_roles_read**](ProjectApi.md#project_roles_read) | **GET** /project-roles/{role_id} |
[**project_sample_manifests_create**](ProjectApi.md#project_sample_manifests_create) | **POST** /project-sample-manifests/{project_id} |
[**project_sample_manifests_read**](ProjectApi.md#project_sample_manifests_read) | **GET** /project-sample-manifests/{project_id} |
[**project_samples_create**](ProjectApi.md#project_samples_create) | **POST** /project-samples/{project_id} | Add samples to the project.
[**project_samples_import_create**](ProjectApi.md#project_samples_import_create) | **POST** /project-samples-import/ |
[**project_samples_list**](ProjectApi.md#project_samples_list) | **GET** /project-samples/{project_id} |
[**project_share_revoke_create**](ProjectApi.md#project_share_revoke_create) | **POST** /project-share-revoke/{project_share_id} |
[**project_shares_create**](ProjectApi.md#project_shares_create) | **POST** /project-shares/ |
[**project_shares_list**](ProjectApi.md#project_shares_list) | **GET** /project-shares/ |
[**project_shares_read**](ProjectApi.md#project_shares_read) | **GET** /project-shares/{project_share_id} |
[**project_stats_read**](ProjectApi.md#project_stats_read) | **GET** /project-stats/{project_id} |
[**project_subscription_details_delete**](ProjectApi.md#project_subscription_details_delete) | **DELETE** /project-subscription-details/{subscription_id} |
[**project_subscription_details_read**](ProjectApi.md#project_subscription_details_read) | **GET** /project-subscription-details/{subscription_id} |
[**project_subscription_event_types_list**](ProjectApi.md#project_subscription_event_types_list) | **GET** /project-subscription-event-types/ |
[**project_subscription_notifications_list**](ProjectApi.md#project_subscription_notifications_list) | **GET** /project-subscription-notifications/{subscription_id} |
[**project_subscription_secret_create**](ProjectApi.md#project_subscription_secret_create) | **POST** /project-subscription-secret/{subscription_id} | Set webhook secret for given subscription.
[**project_subscription_test_create**](ProjectApi.md#project_subscription_test_create) | **POST** /project-subscription-test/{subscription_id} |
[**project_subscriptions_create**](ProjectApi.md#project_subscriptions_create) | **POST** /project-subscriptions/{project_id} |
[**project_subscriptions_list**](ProjectApi.md#project_subscriptions_list) | **GET** /project-subscriptions/{project_id} |
[**project_unhide_samples_create**](ProjectApi.md#project_unhide_samples_create) | **POST** /project-unhide-samples/{project_id} |
[**project_users_create**](ProjectApi.md#project_users_create) | **POST** /project-users/{project_id} |
[**project_users_list**](ProjectApi.md#project_users_list) | **GET** /project-users/{project_id} |
[**projects_create**](ProjectApi.md#projects_create) | **POST** /projects/ |
[**projects_delete_delete**](ProjectApi.md#projects_delete_delete) | **DELETE** /projects-delete/ |
[**projects_hide_create**](ProjectApi.md#projects_hide_create) | **POST** /projects-hide/ |
[**projects_list**](ProjectApi.md#projects_list) | **GET** /projects/ |
[**projects_partial_update**](ProjectApi.md#projects_partial_update) | **PATCH** /projects/{project_id} |
[**projects_read**](ProjectApi.md#projects_read) | **GET** /projects/{project_id} |
[**projects_unhide_create**](ProjectApi.md#projects_unhide_create) | **POST** /projects-unhide/ |


# **project_batch_types_read**
> ProjectBatchTypesRead200Response project_batch_types_read(project_id)



List batch types that are available for current project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_batch_types_read200_response import ProjectBatchTypesRead200Response
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |

    try:
        api_response = api_instance.project_batch_types_read(project_id)
        print("The response of ProjectApi->project_batch_types_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_batch_types_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**ProjectBatchTypesRead200Response**](ProjectBatchTypesRead200Response.md)

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
> BatchDetail project_batches_create(project_id, data)



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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    data = gencove_client.BatchCreate() # BatchCreate |

    try:
        api_response = api_instance.project_batches_create(project_id, data)
        print("The response of ProjectApi->project_batches_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_batches_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data** | [**BatchCreate**](BatchCreate.md)|  |

### Return type

[**BatchDetail**](BatchDetail.md)

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

# **project_batches_read**
> ProjectBatchesRead200Response project_batches_read(project_id)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_batches_read200_response import ProjectBatchesRead200Response
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |

    try:
        api_response = api_instance.project_batches_read(project_id)
        print("The response of ProjectApi->project_batches_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_batches_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**ProjectBatchesRead200Response**](ProjectBatchesRead200Response.md)

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
> ProjectCancelSamples project_cancel_samples_create(project_id, data)



View for canceling sample submission to analysis in a project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_cancel_samples import ProjectCancelSamples
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    data = gencove_client.ProjectCancelSamples() # ProjectCancelSamples |

    try:
        api_response = api_instance.project_cancel_samples_create(project_id, data)
        print("The response of ProjectApi->project_cancel_samples_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_cancel_samples_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data** | [**ProjectCancelSamples**](ProjectCancelSamples.md)|  |

### Return type

[**ProjectCancelSamples**](ProjectCancelSamples.md)

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

# **project_delete_samples_delete**
> project_delete_samples_delete(project_id, data)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_delete import SampleDelete
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    data = gencove_client.SampleDelete() # SampleDelete |

    try:
        api_instance.project_delete_samples_delete(project_id, data)
    except Exception as e:
        print("Exception when calling ProjectApi->project_delete_samples_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data** | [**SampleDelete**](SampleDelete.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_hide_samples_create**
> project_hide_samples_create(project_id, data)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_hide_unhide import SampleHideUnhide
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    data = gencove_client.SampleHideUnhide() # SampleHideUnhide |

    try:
        api_instance.project_hide_samples_create(project_id, data)
    except Exception as e:
        print("Exception when calling ProjectApi->project_hide_samples_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data** | [**SampleHideUnhide**](SampleHideUnhide.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_merge_vcfs_create**
> ProjectMergeVCFsJob project_merge_vcfs_create(project_id)



Post takes no parameters since merge_vcfs job parameters are constructed by the backend.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_merge_vcfs_job import ProjectMergeVCFsJob
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |

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
 **project_id** | **str**|  |

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

# **project_merge_vcfs_read**
> ProjectMergeVCFsJob project_merge_vcfs_read(project_id)



Return last known merge_vcfs job.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_merge_vcfs_job import ProjectMergeVCFsJob
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |

    try:
        api_response = api_instance.project_merge_vcfs_read(project_id)
        print("The response of ProjectApi->project_merge_vcfs_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_merge_vcfs_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

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
> OrganizationUsersList200Response project_organization_users_list(project_id, search=search)



Get organization users.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.organization_users_list200_response import OrganizationUsersList200Response
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    search = 'search_example' # str | Search users by name, email or id (optional)

    try:
        api_response = api_instance.project_organization_users_list(project_id, search=search)
        print("The response of ProjectApi->project_organization_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_organization_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **search** | **str**| Search users by name, email or id | [optional]

### Return type

[**OrganizationUsersList200Response**](OrganizationUsersList200Response.md)

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

# **project_qc_report_read**
> project_qc_report_read(project_id, columns=columns)



Retrieve a CSV QC report for the supplied project ID

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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    columns = ["id","client_id","project_id","year","month","day","status","sex_string","snps_min","bases_dedup_mapped_min","call_rate_min","effective_coverage_min","raw_coverage","ancestries"] # List[str] | Specify one or more column names to include in the report. (optional) (default to ["id","client_id","project_id","year","month","day","status","sex_string","snps_min","bases_dedup_mapped_min","call_rate_min","effective_coverage_min","raw_coverage","ancestries"])

    try:
        api_instance.project_qc_report_read(project_id, columns=columns)
    except Exception as e:
        print("Exception when calling ProjectApi->project_qc_report_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_qc_types_read**
> ProjectQcTypesRead200Response project_qc_types_read(project_id)



List all available QC types for current project

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_qc_types_read200_response import ProjectQcTypesRead200Response
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |

    try:
        api_response = api_instance.project_qc_types_read(project_id)
        print("The response of ProjectApi->project_qc_types_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_qc_types_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**ProjectQcTypesRead200Response**](ProjectQcTypesRead200Response.md)

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

# **project_quality_control_histogram_read**
> ProjectQualityControlHistogram project_quality_control_histogram_read(project_id, qc_type, number_of_results=number_of_results, status=status, search=search, archive_status=archive_status, hidden_status=hidden_status, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)



Retrieve user project and desired qc results histogram.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_quality_control_histogram import ProjectQualityControlHistogram
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    qc_type = 'qc_type_example' # str | Quality control type key
    number_of_results = 200 # int | Number of results (optional) (default to 200)
    status = 'status_example' # str | Filter QC results by samples and their status (optional)
    search = 'search_example' # str | Search QC results by samples and their id or client id (optional)
    archive_status = 'archive_status_example' # str | Filter QC results by samples and their archived status (optional)
    hidden_status = 'hidden_status_example' # str | Filter QC results by samples and their hidden status (optional)
    created_after = 'created_after_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    created_before = 'created_before_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    modified_after = 'modified_after_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    modified_before = 'modified_before_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)

    try:
        api_response = api_instance.project_quality_control_histogram_read(project_id, qc_type, number_of_results=number_of_results, status=status, search=search, archive_status=archive_status, hidden_status=hidden_status, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)
        print("The response of ProjectApi->project_quality_control_histogram_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_quality_control_histogram_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **qc_type** | **str**| Quality control type key |
 **number_of_results** | **int**| Number of results | [optional] [default to 200]
 **status** | **str**| Filter QC results by samples and their status | [optional]
 **search** | **str**| Search QC results by samples and their id or client id | [optional]
 **archive_status** | **str**| Filter QC results by samples and their archived status | [optional]
 **hidden_status** | **str**| Filter QC results by samples and their hidden status | [optional]
 **created_after** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **created_before** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **modified_after** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **modified_before** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]

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
> SampleRestore project_restore_samples_create(project_id, data)



Handles sample restore process for given sample ids in current project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_restore import SampleRestore
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    data = gencove_client.SampleRestore() # SampleRestore |

    try:
        api_response = api_instance.project_restore_samples_create(project_id, data)
        print("The response of ProjectApi->project_restore_samples_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_restore_samples_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data** | [**SampleRestore**](SampleRestore.md)|  |

### Return type

[**SampleRestore**](SampleRestore.md)

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

# **project_roles_delete**
> project_roles_delete(role_id)



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
    api_instance = gencove_client.ProjectApi(api_client)
    role_id = 'role_id_example' # str |

    try:
        api_instance.project_roles_delete(role_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_roles_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  |

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

# **project_roles_read**
> UserRoleObject project_roles_read(role_id)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.user_role_object import UserRoleObject
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
    api_instance = gencove_client.ProjectApi(api_client)
    role_id = 'role_id_example' # str |

    try:
        api_response = api_instance.project_roles_read(role_id)
        print("The response of ProjectApi->project_roles_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_roles_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  |

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
> SampleManifestUpload project_sample_manifests_create(project_id, sample_manifest)



Upload sample manifest file for project

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_manifest_upload import SampleManifestUpload
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str | Project ID to add manifest to
    sample_manifest = None # bytearray | Sample manifest CSV or XLSX file

    try:
        api_response = api_instance.project_sample_manifests_create(project_id, sample_manifest)
        print("The response of ProjectApi->project_sample_manifests_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_sample_manifests_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID to add manifest to |
 **sample_manifest** | **bytearray**| Sample manifest CSV or XLSX file |

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

# **project_sample_manifests_read**
> SampleManifestUpload project_sample_manifests_read(project_id)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_manifest_upload import SampleManifestUpload
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |

    try:
        api_response = api_instance.project_sample_manifests_read(project_id)
        print("The response of ProjectApi->project_sample_manifests_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_sample_manifests_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

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

# **project_samples_create**
> ExtendedSampleSheetCreate project_samples_create(project_id, data)

Add samples to the project.

Samples are added formatted as the `results` response value that was returned from `/sample-sheet/` endpoint.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.extended_sample_sheet_create import ExtendedSampleSheetCreate
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    data = gencove_client.ExtendedSampleSheetCreate() # ExtendedSampleSheetCreate |

    try:
        # Add samples to the project.
        api_response = api_instance.project_samples_create(project_id, data)
        print("The response of ProjectApi->project_samples_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_samples_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data** | [**ExtendedSampleSheetCreate**](ExtendedSampleSheetCreate.md)|  |

### Return type

[**ExtendedSampleSheetCreate**](ExtendedSampleSheetCreate.md)

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

# **project_samples_import_create**
> ProjectSamplesImport project_samples_import_create(data)



Class for the import of samples from the existing project.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_samples_import import ProjectSamplesImport
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
    api_instance = gencove_client.ProjectApi(api_client)
    data = gencove_client.ProjectSamplesImport() # ProjectSamplesImport |

    try:
        api_response = api_instance.project_samples_import_create(data)
        print("The response of ProjectApi->project_samples_import_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_samples_import_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProjectSamplesImport**](ProjectSamplesImport.md)|  |

### Return type

[**ProjectSamplesImport**](ProjectSamplesImport.md)

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

# **project_samples_list**
> ProjectSamplesList200Response project_samples_list(project_id, status=status, archive_status=archive_status, hidden_status=hidden_status, search=search, sort_by=sort_by, sort_order=sort_order, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)



List single project's associated samples.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_samples_list200_response import ProjectSamplesList200Response
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    status = 'status_example' # str | Filter samples by their status (optional)
    archive_status = 'archive_status_example' # str | Filter samples by their archive status (optional)
    hidden_status = 'hidden_status_example' # str | Filter samples by their hidden status (optional)
    search = 'search_example' # str | Search samples by id or client id or metadata content (optional)
    sort_by = 'sort_by_example' # str | Sort results (optional)
    sort_order = 'sort_order_example' # str | Sort direction (optional)
    created_after = 'created_after_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    created_before = 'created_before_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    modified_after = 'modified_after_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    modified_before = 'modified_before_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)

    try:
        api_response = api_instance.project_samples_list(project_id, status=status, archive_status=archive_status, hidden_status=hidden_status, search=search, sort_by=sort_by, sort_order=sort_order, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)
        print("The response of ProjectApi->project_samples_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_samples_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **status** | **str**| Filter samples by their status | [optional]
 **archive_status** | **str**| Filter samples by their archive status | [optional]
 **hidden_status** | **str**| Filter samples by their hidden status | [optional]
 **search** | **str**| Search samples by id or client id or metadata content | [optional]
 **sort_by** | **str**| Sort results | [optional]
 **sort_order** | **str**| Sort direction | [optional]
 **created_after** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **created_before** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **modified_after** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **modified_before** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]

### Return type

[**ProjectSamplesList200Response**](ProjectSamplesList200Response.md)

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

# **project_share_revoke_create**
> ProjectShareRevoke project_share_revoke_create(project_share_id, data)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_share_revoke import ProjectShareRevoke
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_share_id = 'project_share_id_example' # str |
    data = gencove_client.ProjectShareRevoke() # ProjectShareRevoke |

    try:
        api_response = api_instance.project_share_revoke_create(project_share_id, data)
        print("The response of ProjectApi->project_share_revoke_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_share_revoke_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_share_id** | **str**|  |
 **data** | [**ProjectShareRevoke**](ProjectShareRevoke.md)|  |

### Return type

[**ProjectShareRevoke**](ProjectShareRevoke.md)

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

# **project_shares_create**
> ProjectShare project_shares_create(data)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_share import ProjectShare
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
    api_instance = gencove_client.ProjectApi(api_client)
    data = gencove_client.ProjectShare() # ProjectShare |

    try:
        api_response = api_instance.project_shares_create(data)
        print("The response of ProjectApi->project_shares_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_shares_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProjectShare**](ProjectShare.md)|  |

### Return type

[**ProjectShare**](ProjectShare.md)

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

# **project_shares_list**
> ProjectSharesList200Response project_shares_list()



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_shares_list200_response import ProjectSharesList200Response
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
    api_instance = gencove_client.ProjectApi(api_client)

    try:
        api_response = api_instance.project_shares_list()
        print("The response of ProjectApi->project_shares_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_shares_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProjectSharesList200Response**](ProjectSharesList200Response.md)

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

# **project_shares_read**
> ProjectShare project_shares_read(project_share_id)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_share import ProjectShare
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_share_id = 'project_share_id_example' # str |

    try:
        api_response = api_instance.project_shares_read(project_share_id)
        print("The response of ProjectApi->project_shares_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_shares_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_share_id** | **str**|  |

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

# **project_stats_read**
> ProjectStats project_stats_read(project_id, status=status, search=search, archive_status=archive_status, hidden_status=hidden_status, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)



Retrieve user project and it's sample stats.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_stats import ProjectStats
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    status = 'status_example' # str | Filter stats by samples and their status (optional)
    search = 'search_example' # str | Search stats by samples and their id or client id (optional)
    archive_status = 'archive_status_example' # str | Filter stats by samples and their archived status (optional)
    hidden_status = 'hidden_status_example' # str | Filter stats by samples and their hidden status (optional)
    created_after = 'created_after_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    created_before = 'created_before_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    modified_after = 'modified_after_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    modified_before = 'modified_before_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)

    try:
        api_response = api_instance.project_stats_read(project_id, status=status, search=search, archive_status=archive_status, hidden_status=hidden_status, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before)
        print("The response of ProjectApi->project_stats_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_stats_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **status** | **str**| Filter stats by samples and their status | [optional]
 **search** | **str**| Search stats by samples and their id or client id | [optional]
 **archive_status** | **str**| Filter stats by samples and their archived status | [optional]
 **hidden_status** | **str**| Filter stats by samples and their hidden status | [optional]
 **created_after** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **created_before** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **modified_after** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **modified_before** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]

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

# **project_subscription_details_delete**
> project_subscription_details_delete(subscription_id)



Details of a single subscription for project related events.

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
    api_instance = gencove_client.ProjectApi(api_client)
    subscription_id = 'subscription_id_example' # str |

    try:
        api_instance.project_subscription_details_delete(subscription_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_details_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  |

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

# **project_subscription_details_read**
> ProjectSubscription project_subscription_details_read(subscription_id)



Details of a single subscription for project related events.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_subscription import ProjectSubscription
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
    api_instance = gencove_client.ProjectApi(api_client)
    subscription_id = 'subscription_id_example' # str |

    try:
        api_response = api_instance.project_subscription_details_read(subscription_id)
        print("The response of ProjectApi->project_subscription_details_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_details_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  |

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
> ProjectSubscriptionEventTypesList200Response project_subscription_event_types_list()



List subscription event types that are available for all projects.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_subscription_event_types_list200_response import ProjectSubscriptionEventTypesList200Response
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
    api_instance = gencove_client.ProjectApi(api_client)

    try:
        api_response = api_instance.project_subscription_event_types_list()
        print("The response of ProjectApi->project_subscription_event_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_event_types_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProjectSubscriptionEventTypesList200Response**](ProjectSubscriptionEventTypesList200Response.md)

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
> ProjectSubscriptionNotificationsList200Response project_subscription_notifications_list(subscription_id)



List all available subscriptions for given project or create a new subscription.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_subscription_notifications_list200_response import ProjectSubscriptionNotificationsList200Response
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
    api_instance = gencove_client.ProjectApi(api_client)
    subscription_id = 'subscription_id_example' # str |

    try:
        api_response = api_instance.project_subscription_notifications_list(subscription_id)
        print("The response of ProjectApi->project_subscription_notifications_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_notifications_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  |

### Return type

[**ProjectSubscriptionNotificationsList200Response**](ProjectSubscriptionNotificationsList200Response.md)

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
    api_instance = gencove_client.ProjectApi(api_client)
    subscription_id = 'subscription_id_example' # str |

    try:
        # Set webhook secret for given subscription.
        api_response = api_instance.project_subscription_secret_create(subscription_id)
        print("The response of ProjectApi->project_subscription_secret_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_secret_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  |

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
> project_subscription_test_create(subscription_id, data)



Send a dummy event for given subscription to test notifications integration. By default, there are no retries for this test endpoint.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.subscription_test import SubscriptionTest
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
    api_instance = gencove_client.ProjectApi(api_client)
    subscription_id = 'subscription_id_example' # str |
    data = gencove_client.SubscriptionTest() # SubscriptionTest |

    try:
        api_instance.project_subscription_test_create(subscription_id, data)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscription_test_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  |
 **data** | [**SubscriptionTest**](SubscriptionTest.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_subscriptions_create**
> SubscriptionCreate project_subscriptions_create(project_id, data)



Add subscription to project events.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.subscription_create import SubscriptionCreate
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    data = gencove_client.SubscriptionCreate() # SubscriptionCreate |

    try:
        api_response = api_instance.project_subscriptions_create(project_id, data)
        print("The response of ProjectApi->project_subscriptions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscriptions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data** | [**SubscriptionCreate**](SubscriptionCreate.md)|  |

### Return type

[**SubscriptionCreate**](SubscriptionCreate.md)

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

# **project_subscriptions_list**
> ProjectSubscriptionsList200Response project_subscriptions_list(project_id)



List all available subscriptions for given project or create a new subscription.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_subscriptions_list200_response import ProjectSubscriptionsList200Response
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |

    try:
        api_response = api_instance.project_subscriptions_list(project_id)
        print("The response of ProjectApi->project_subscriptions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_subscriptions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**ProjectSubscriptionsList200Response**](ProjectSubscriptionsList200Response.md)

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
> project_unhide_samples_create(project_id, data)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_hide_unhide import SampleHideUnhide
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    data = gencove_client.SampleHideUnhide() # SampleHideUnhide |

    try:
        api_instance.project_unhide_samples_create(project_id, data)
    except Exception as e:
        print("Exception when calling ProjectApi->project_unhide_samples_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data** | [**SampleHideUnhide**](SampleHideUnhide.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_users_create**
> UserRoleObject project_users_create(project_id, data)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.user_role_object import UserRoleObject
from gencove_client.models.user_role_object_create import UserRoleObjectCreate
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    data = gencove_client.UserRoleObjectCreate() # UserRoleObjectCreate |

    try:
        api_response = api_instance.project_users_create(project_id, data)
        print("The response of ProjectApi->project_users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data** | [**UserRoleObjectCreate**](UserRoleObjectCreate.md)|  |

### Return type

[**UserRoleObject**](UserRoleObject.md)

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

# **project_users_list**
> ProjectUsers project_users_list(project_id, search=search, only_explicit_roles=only_explicit_roles)



Get project users by project id.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_users import ProjectUsers
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    search = 'search_example' # str | Search users by name, email or id (optional)
    only_explicit_roles = True # bool | Show only project level granted roles (optional)

    try:
        api_response = api_instance.project_users_list(project_id, search=search, only_explicit_roles=only_explicit_roles)
        print("The response of ProjectApi->project_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **search** | **str**| Search users by name, email or id | [optional]
 **only_explicit_roles** | **bool**| Show only project level granted roles | [optional]

### Return type

[**ProjectUsers**](ProjectUsers.md)

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
> Project projects_create(data)



Create project

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project import Project
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
    api_instance = gencove_client.ProjectApi(api_client)
    data = gencove_client.Project() # Project |

    try:
        api_response = api_instance.projects_create(data)
        print("The response of ProjectApi->projects_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Project**](Project.md)|  |

### Return type

[**Project**](Project.md)

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

# **projects_delete_delete**
> projects_delete_delete(data)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_delete import ProjectDelete
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
    api_instance = gencove_client.ProjectApi(api_client)
    data = gencove_client.ProjectDelete() # ProjectDelete |

    try:
        api_instance.projects_delete_delete(data)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProjectDelete**](ProjectDelete.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_hide_create**
> projects_hide_create(data)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_hide_unhide import ProjectHideUnhide
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
    api_instance = gencove_client.ProjectApi(api_client)
    data = gencove_client.ProjectHideUnhide() # ProjectHideUnhide |

    try:
        api_instance.projects_hide_create(data)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_hide_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProjectHideUnhide**](ProjectHideUnhide.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list**
> ProjectsList200Response projects_list(search=search, status=status, hidden_status=hidden_status, sort_by=sort_by, sort_order=sort_order, additional_permission=additional_permission, shared=shared, locked=locked)



Retrieve list of user projects.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.projects_list200_response import ProjectsList200Response
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
    api_instance = gencove_client.ProjectApi(api_client)
    search = 'search_example' # str | A search term. (optional)
    status = 'status_example' # str | Filter projects by sample statuses (optional)
    hidden_status = 'hidden_status_example' # str | Filter projects by their hidden status (optional)
    sort_by = 'sort_by_example' # str | Sort results (optional)
    sort_order = 'sort_order_example' # str | Sort direction (optional)
    additional_permission = 'additional_permission_example' # str | Additional permission (optional)
    shared = True # bool | Filter projects by shared status (optional)
    locked = True # bool | Filter projects by locked status (optional)

    try:
        api_response = api_instance.projects_list(search=search, status=status, hidden_status=hidden_status, sort_by=sort_by, sort_order=sort_order, additional_permission=additional_permission, shared=shared, locked=locked)
        print("The response of ProjectApi->projects_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **status** | **str**| Filter projects by sample statuses | [optional]
 **hidden_status** | **str**| Filter projects by their hidden status | [optional]
 **sort_by** | **str**| Sort results | [optional]
 **sort_order** | **str**| Sort direction | [optional]
 **additional_permission** | **str**| Additional permission | [optional]
 **shared** | **bool**| Filter projects by shared status | [optional]
 **locked** | **bool**| Filter projects by locked status | [optional]

### Return type

[**ProjectsList200Response**](ProjectsList200Response.md)

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
> Project projects_partial_update(project_id, data)



Update single project details

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project import Project
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |
    data = gencove_client.Project() # Project |

    try:
        api_response = api_instance.projects_partial_update(project_id, data)
        print("The response of ProjectApi->projects_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **data** | [**Project**](Project.md)|  |

### Return type

[**Project**](Project.md)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_read**
> ProjectDetail projects_read(project_id)



Fetch single project details

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_detail import ProjectDetail
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
    api_instance = gencove_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str |

    try:
        api_response = api_instance.projects_read(project_id)
        print("The response of ProjectApi->projects_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

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
> projects_unhide_create(data)



### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.project_hide_unhide import ProjectHideUnhide
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
    api_instance = gencove_client.ProjectApi(api_client)
    data = gencove_client.ProjectHideUnhide() # ProjectHideUnhide |

    try:
        api_instance.projects_unhide_create(data)
    except Exception as e:
        print("Exception when calling ProjectApi->projects_unhide_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProjectHideUnhide**](ProjectHideUnhide.md)|  |

### Return type

void (empty response body)

### Authorization

[API key](../README.md#API key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
