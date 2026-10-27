# gencove_client.SampleApi

All URIs are relative to *https://api.gencove.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sample_ancestry_retrieve**](SampleApi.md#sample_ancestry_retrieve) | **GET** /api/v2/sample-ancestry/{sample_id} |
[**sample_consumer_report_create**](SampleApi.md#sample_consumer_report_create) | **POST** /api/v2/sample-consumer-report/{sample_id} |
[**sample_genomic_variants_list**](SampleApi.md#sample_genomic_variants_list) | **GET** /api/v2/sample-genomic-variants/{sample_id} |
[**sample_kit_create**](SampleApi.md#sample_kit_create) | **POST** /api/v2/sample-kit/ |
[**sample_kit_form_create**](SampleApi.md#sample_kit_form_create) | **POST** /api/v2/sample-kit-form/ |
[**sample_kit_partial_update**](SampleApi.md#sample_kit_partial_update) | **PATCH** /api/v2/sample-kit/{sample_id} |
[**sample_kit_retrieve**](SampleApi.md#sample_kit_retrieve) | **GET** /api/v2/sample-kit/{sample_id} |
[**sample_manifests_csv_template_retrieve**](SampleApi.md#sample_manifests_csv_template_retrieve) | **GET** /api/v2/sample-manifests-csv-template/ |
[**sample_manifests_retrieve**](SampleApi.md#sample_manifests_retrieve) | **GET** /api/v2/sample-manifests/{sample_manifest_id} |
[**sample_manifests_xlsx_template_retrieve**](SampleApi.md#sample_manifests_xlsx_template_retrieve) | **GET** /api/v2/sample-manifests-xlsx-template/ |
[**sample_metadata_create**](SampleApi.md#sample_metadata_create) | **POST** /api/v2/sample-metadata/{sample_id} |
[**sample_metadata_retrieve**](SampleApi.md#sample_metadata_retrieve) | **GET** /api/v2/sample-metadata/{sample_id} |
[**sample_parentage_retrieve**](SampleApi.md#sample_parentage_retrieve) | **GET** /api/v2/sample-parentage/{sample_id} |
[**sample_quality_controls_list**](SampleApi.md#sample_quality_controls_list) | **GET** /api/v2/sample-quality-controls/{sample_id} |
[**sample_restore_group_list**](SampleApi.md#sample_restore_group_list) | **GET** /api/v2/sample-restore-group/{restore_group_id} |
[**sample_sheet_list**](SampleApi.md#sample_sheet_list) | **GET** /api/v2/sample-sheet/ |
[**sample_stats_retrieve**](SampleApi.md#sample_stats_retrieve) | **GET** /api/v2/sample-stats/{sample_id} |
[**sample_statuses_list**](SampleApi.md#sample_statuses_list) | **GET** /api/v2/sample-statuses/{sample_id} |
[**sample_trait_scores_list**](SampleApi.md#sample_trait_scores_list) | **GET** /api/v2/sample-trait-scores/{sample_id} |
[**samples_retrieve**](SampleApi.md#samples_retrieve) | **GET** /api/v2/samples/{sample_id} |


# **sample_ancestry_retrieve**
> SampleAncestry sample_ancestry_retrieve(sample_id)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_ancestry import SampleAncestry
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.sample_ancestry_retrieve(sample_id)
        print("The response of SampleApi->sample_ancestry_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_ancestry_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |

### Return type

[**SampleAncestry**](SampleAncestry.md)

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

# **sample_consumer_report_create**
> SampleConsumerReportResponse sample_consumer_report_create(sample_id, sample_consumer_report_create=sample_consumer_report_create)

Generate presigned URL for consumer report.

Args:
    request: HTTP request

Returns:
    Response with presigned URL and expiration time

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_consumer_report_create import SampleConsumerReportCreate
from gencove_client.models.sample_consumer_report_response import SampleConsumerReportResponse
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    sample_consumer_report_create = gencove_client.SampleConsumerReportCreate() # SampleConsumerReportCreate |  (optional)

    try:
        api_response = api_instance.sample_consumer_report_create(sample_id, sample_consumer_report_create=sample_consumer_report_create)
        print("The response of SampleApi->sample_consumer_report_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_consumer_report_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |
 **sample_consumer_report_create** | [**SampleConsumerReportCreate**](SampleConsumerReportCreate.md)|  | [optional]

### Return type

[**SampleConsumerReportResponse**](SampleConsumerReportResponse.md)

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

# **sample_genomic_variants_list**
> PaginatedGenomicVariantList sample_genomic_variants_list(sample_id, chromosome=chromosome, end_position=end_position, limit=limit, offset=offset, position=position, rsid=rsid, start_position=start_position)

Return variant-level results from a sample's imputed VCF.

Provide exactly one of the three query modes:

- point: `?chromosome=chr11&position=<pos>`
- range: `?chromosome=chr11&start_position=<start>&end_position=<end>`
- rsid:  `?rsid=rs1,rs2,...`

`chromosome` must be an h38 contig name with the `chr` prefix
(chr1..chr22, chrX, chrY, chrM).

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_genomic_variant_list import PaginatedGenomicVariantList
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    chromosome = 'chromosome_example' # str | h38 contig name with the `chr` prefix, e.g. `chr1`, `chr11`, `chrX`, `chrY`, `chrM` (point and range queries) (optional)
    end_position = 56 # int | Range end (1-based); use with `start_position`. The span may not exceed 100000 bp. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    position = 56 # int | 1-based position for a point query (optional)
    rsid = 'rsid_example' # str | Comma-separated rsIDs, e.g. `rs429358,rs7412` (at most 50 per request). (optional)
    start_position = 56 # int | Range start (1-based); use with `end_position` (optional)

    try:
        api_response = api_instance.sample_genomic_variants_list(sample_id, chromosome=chromosome, end_position=end_position, limit=limit, offset=offset, position=position, rsid=rsid, start_position=start_position)
        print("The response of SampleApi->sample_genomic_variants_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_genomic_variants_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |
 **chromosome** | **str**| h38 contig name with the &#x60;chr&#x60; prefix, e.g. &#x60;chr1&#x60;, &#x60;chr11&#x60;, &#x60;chrX&#x60;, &#x60;chrY&#x60;, &#x60;chrM&#x60; (point and range queries) | [optional]
 **end_position** | **int**| Range end (1-based); use with &#x60;start_position&#x60;. The span may not exceed 100000 bp. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **position** | **int**| 1-based position for a point query | [optional]
 **rsid** | **str**| Comma-separated rsIDs, e.g. &#x60;rs429358,rs7412&#x60; (at most 50 per request). | [optional]
 **start_position** | **int**| Range start (1-based); use with &#x60;end_position&#x60; | [optional]

### Return type

[**PaginatedGenomicVariantList**](PaginatedGenomicVariantList.md)

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

# **sample_kit_create**
> SampleKitResponse sample_kit_create(sample_kit)

Order a new kit for a sample

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_kit import SampleKit
from gencove_client.models.sample_kit_response import SampleKitResponse
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_kit = gencove_client.SampleKit() # SampleKit |

    try:
        api_response = api_instance.sample_kit_create(sample_kit)
        print("The response of SampleApi->sample_kit_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_kit_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_kit** | [**SampleKit**](SampleKit.md)|  |

### Return type

[**SampleKitResponse**](SampleKitResponse.md)

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

# **sample_kit_form_create**
> SampleKitFormResponse sample_kit_form_create(sample_kit_form_create)

Create a temporary, payment-free kit-order session.

Auth-gated to ``consumer_provider`` orgs and the ``sample_kit_create`` role
(project-scoped). Creates a placeholder ``samples.Sample`` (status
``consumer_awaiting_kit_order``), pins the JWT ``jti`` on it for replay
protection, and returns a tokenized URL the partner hands to an end user.
The ``Kit`` is only created once the end user submits the form.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_kit_form_create import SampleKitFormCreate
from gencove_client.models.sample_kit_form_response import SampleKitFormResponse
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_kit_form_create = gencove_client.SampleKitFormCreate() # SampleKitFormCreate |

    try:
        api_response = api_instance.sample_kit_form_create(sample_kit_form_create)
        print("The response of SampleApi->sample_kit_form_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_kit_form_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_kit_form_create** | [**SampleKitFormCreate**](SampleKitFormCreate.md)|  |

### Return type

[**SampleKitFormResponse**](SampleKitFormResponse.md)

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

# **sample_kit_partial_update**
> SampleKitDetails sample_kit_partial_update(sample_id, patched_sample_kit_address_update=patched_sample_kit_address_update)

Correct the shipping address of a kit order the sequencing provider rejected, and resubmit the order. Only allowed while the sample's status is `kit order failed wrong address`. Send only the fields to change; they are validated together with the current address. `recipient_email` cannot be changed. On success the sample moves to `kit order address update` and the order is resubmitted to the sequencing provider.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.patched_sample_kit_address_update import PatchedSampleKitAddressUpdate
from gencove_client.models.sample_kit_details import SampleKitDetails
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    patched_sample_kit_address_update = gencove_client.PatchedSampleKitAddressUpdate() # PatchedSampleKitAddressUpdate |  (optional)

    try:
        api_response = api_instance.sample_kit_partial_update(sample_id, patched_sample_kit_address_update=patched_sample_kit_address_update)
        print("The response of SampleApi->sample_kit_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_kit_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |
 **patched_sample_kit_address_update** | [**PatchedSampleKitAddressUpdate**](PatchedSampleKitAddressUpdate.md)|  | [optional]

### Return type

[**SampleKitDetails**](SampleKitDetails.md)

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

# **sample_kit_retrieve**
> SampleKitDetails sample_kit_retrieve(sample_id)

Return kit details for the sample or 404 if it has no kit.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_kit_details import SampleKitDetails
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.sample_kit_retrieve(sample_id)
        print("The response of SampleApi->sample_kit_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_kit_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |

### Return type

[**SampleKitDetails**](SampleKitDetails.md)

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

# **sample_manifests_csv_template_retrieve**
> sample_manifests_csv_template_retrieve(template_type=template_type)

Download a sample manifest CSV template file based on the template_type parameter.

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
    api_instance = gencove_client.SampleApi(api_client)
    template_type = 'template_type_example' # str | Type of the sample manifest CSV template. Options are 96_well, 384_well, tube. (optional)

    try:
        api_instance.sample_manifests_csv_template_retrieve(template_type=template_type)
    except Exception as e:
        print("Exception when calling SampleApi->sample_manifests_csv_template_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| Type of the sample manifest CSV template. Options are 96_well, 384_well, tube. | [optional]

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

# **sample_manifests_retrieve**
> SampleManifest sample_manifests_retrieve(sample_manifest_id)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_manifest import SampleManifest
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_manifest_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.sample_manifests_retrieve(sample_manifest_id)
        print("The response of SampleApi->sample_manifests_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_manifests_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_manifest_id** | **UUID**|  |

### Return type

[**SampleManifest**](SampleManifest.md)

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

# **sample_manifests_xlsx_template_retrieve**
> sample_manifests_xlsx_template_retrieve()

Download a sample manifest XLSX template file.

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
    api_instance = gencove_client.SampleApi(api_client)

    try:
        api_instance.sample_manifests_xlsx_template_retrieve()
    except Exception as e:
        print("Exception when calling SampleApi->sample_manifests_xlsx_template_retrieve: %s\n" % e)
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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_metadata_create**
> SampleMetadata sample_metadata_create(sample_id, sample_metadata=sample_metadata)

Create sample metadata.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_metadata import SampleMetadata
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    sample_metadata = gencove_client.SampleMetadata() # SampleMetadata |  (optional)

    try:
        api_response = api_instance.sample_metadata_create(sample_id, sample_metadata=sample_metadata)
        print("The response of SampleApi->sample_metadata_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_metadata_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |
 **sample_metadata** | [**SampleMetadata**](SampleMetadata.md)|  | [optional]

### Return type

[**SampleMetadata**](SampleMetadata.md)

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

# **sample_metadata_retrieve**
> SampleMetadata sample_metadata_retrieve(sample_id)

Return sample metadata.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_metadata import SampleMetadata
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.sample_metadata_retrieve(sample_id)
        print("The response of SampleApi->sample_metadata_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_metadata_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |

### Return type

[**SampleMetadata**](SampleMetadata.md)

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

# **sample_parentage_retrieve**
> SampleParentage sample_parentage_retrieve(sample_id, display_results=display_results)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_parentage import SampleParentage
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    display_results = 'display_results_example' # str | Display mode for parentage records. Options are: - 'matches': Only display records where a parent has been identified (default) - 'checks': Only display records where no parent has been identified - 'all': Display all parentage records (optional)

    try:
        api_response = api_instance.sample_parentage_retrieve(sample_id, display_results=display_results)
        print("The response of SampleApi->sample_parentage_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_parentage_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |
 **display_results** | **str**| Display mode for parentage records. Options are: - &#39;matches&#39;: Only display records where a parent has been identified (default) - &#39;checks&#39;: Only display records where no parent has been identified - &#39;all&#39;: Display all parentage records | [optional]

### Return type

[**SampleParentage**](SampleParentage.md)

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

# **sample_quality_controls_list**
> PaginatedQualityControlList sample_quality_controls_list(sample_id, limit=limit, offset=offset)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_quality_control_list import PaginatedQualityControlList
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.sample_quality_controls_list(sample_id, limit=limit, offset=offset)
        print("The response of SampleApi->sample_quality_controls_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_quality_controls_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedQualityControlList**](PaginatedQualityControlList.md)

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

# **sample_restore_group_list**
> PaginatedSampleListList sample_restore_group_list(restore_group_id, archive_status=archive_status, created_after=created_after, created_before=created_before, hidden_status=hidden_status, limit=limit, modified_after=modified_after, modified_before=modified_before, offset=offset, search=search, status=status)

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
    api_instance = gencove_client.SampleApi(api_client)
    restore_group_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    archive_status = 'archive_status_example' # str | Filter samples by their archive status (optional)
    created_after = 'created_after_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    created_before = 'created_before_example' # str | Filter samples by created timestamp; use ISO8601 format (optional)
    hidden_status = 'hidden_status_example' # str | Filter samples by their hidden status (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    modified_after = 'modified_after_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    modified_before = 'modified_before_example' # str | Filter samples by modified timestamp; use ISO8601 format (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    search = 'search_example' # str | Search samples by id or client id or metadata content (optional)
    status = 'status_example' # str | Filter samples by their status (optional)

    try:
        api_response = api_instance.sample_restore_group_list(restore_group_id, archive_status=archive_status, created_after=created_after, created_before=created_before, hidden_status=hidden_status, limit=limit, modified_after=modified_after, modified_before=modified_before, offset=offset, search=search, status=status)
        print("The response of SampleApi->sample_restore_group_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_restore_group_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_group_id** | **UUID**|  |
 **archive_status** | **str**| Filter samples by their archive status | [optional]
 **created_after** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **created_before** | **str**| Filter samples by created timestamp; use ISO8601 format | [optional]
 **hidden_status** | **str**| Filter samples by their hidden status | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **modified_after** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **modified_before** | **str**| Filter samples by modified timestamp; use ISO8601 format | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **search** | **str**| Search samples by id or client id or metadata content | [optional]
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

# **sample_sheet_list**
> PaginatedSampleSheetList sample_sheet_list(limit=limit, offset=offset, search=search, sort_by=sort_by, sort_order=sort_order, status=status)

Return generated sample sheet.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_sample_sheet_list import PaginatedSampleSheetList
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
    api_instance = gencove_client.SampleApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    search = 'search_example' # str | gncv:// notated sample path to search for (optional)
    sort_by = 'sort_by_example' # str | Sort results (optional)
    sort_order = 'sort_order_example' # str | Sort direction (optional)
    status = 'status_example' # str | One of: assigned, unassigned, all; default is 'all' (optional)

    try:
        api_response = api_instance.sample_sheet_list(limit=limit, offset=offset, search=search, sort_by=sort_by, sort_order=sort_order, status=status)
        print("The response of SampleApi->sample_sheet_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_sheet_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **search** | **str**| gncv:// notated sample path to search for | [optional]
 **sort_by** | **str**| Sort results | [optional]
 **sort_order** | **str**| Sort direction | [optional]
 **status** | **str**| One of: assigned, unassigned, all; default is &#39;all&#39; | [optional]

### Return type

[**PaginatedSampleSheetList**](PaginatedSampleSheetList.md)

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

# **sample_stats_retrieve**
> SampleStats sample_stats_retrieve(sample_id)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_stats import SampleStats
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.sample_stats_retrieve(sample_id)
        print("The response of SampleApi->sample_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |

### Return type

[**SampleStats**](SampleStats.md)

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

# **sample_statuses_list**
> PaginatedSampleStatusListList sample_statuses_list(sample_id, limit=limit, offset=offset)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_sample_status_list_list import PaginatedSampleStatusListList
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.sample_statuses_list(sample_id, limit=limit, offset=offset)
        print("The response of SampleApi->sample_statuses_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_statuses_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedSampleStatusListList**](PaginatedSampleStatusListList.md)

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

# **sample_trait_scores_list**
> PaginatedTraitScoreList sample_trait_scores_list(sample_id, limit=limit, offset=offset)

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_trait_score_list import PaginatedTraitScoreList
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.sample_trait_scores_list(sample_id, limit=limit, offset=offset)
        print("The response of SampleApi->sample_trait_scores_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->sample_trait_scores_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedTraitScoreList**](PaginatedTraitScoreList.md)

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

# **samples_retrieve**
> SampleDetails samples_retrieve(sample_id)

Retrieve sample model. Overridden to store audit action.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.sample_details import SampleDetails
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
    api_instance = gencove_client.SampleApi(api_client)
    sample_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |

    try:
        api_response = api_instance.samples_retrieve(sample_id)
        print("The response of SampleApi->samples_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SampleApi->samples_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_id** | **UUID**|  |

### Return type

[**SampleDetails**](SampleDetails.md)

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
