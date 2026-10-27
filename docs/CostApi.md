# gencove_client.CostApi

All URIs are relative to *https://api.gencove.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cost_reporting_list**](CostApi.md#cost_reporting_list) | **GET** /api/v2/cost-reporting/ |


# **cost_reporting_list**
> PaginatedCostReportRecordList cost_reporting_list(include_cross_org=include_cross_org, limit=limit, offset=offset)

The caller's organization's cost report files: one record per month,
newest first, each with its summary CSV and, for an organization opted
in to platform costs, its line-items CSV (``costs.report_records``).

``include_cross_org`` picks the series. Left out or ``true``: the
cross-organization record of every month that has one (the
organization's costs with those of every organization a grant it held
covered that month) and the own record of the other months. ``false``:
the own records only. Every organization covered on the page is told
in the audit trail, once.

### Example

* Api Key Authentication (API key):
* Api Key Authentication (JWT):

```python
import gencove_client
from gencove_client.models.paginated_cost_report_record_list import PaginatedCostReportRecordList
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
    api_instance = gencove_client.CostApi(api_client)
    include_cross_org = True # bool | The reports covering the organizations a grant of the caller's covered, where there are any (the default), or the caller's own reports only (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.cost_reporting_list(include_cross_org=include_cross_org, limit=limit, offset=offset)
        print("The response of CostApi->cost_reporting_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_reporting_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_cross_org** | **bool**| The reports covering the organizations a grant of the caller&#39;s covered, where there are any (the default), or the caller&#39;s own reports only | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**PaginatedCostReportRecordList**](PaginatedCostReportRecordList.md)

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
