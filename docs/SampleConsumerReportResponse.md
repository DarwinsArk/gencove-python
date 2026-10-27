# SampleConsumerReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Presigned URL for accessing the consumer report |
**expires_at** | **datetime** | When the presigned URL will expire |

## Example

```python
from gencove_client.models.sample_consumer_report_response import SampleConsumerReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SampleConsumerReportResponse from a JSON string
sample_consumer_report_response_instance = SampleConsumerReportResponse.from_json(json)
# print the JSON string representation of the object
print(SampleConsumerReportResponse.to_json())

# convert the object into a dict
sample_consumer_report_response_dict = sample_consumer_report_response_instance.to_dict()
# create an instance of SampleConsumerReportResponse from a dict
sample_consumer_report_response_from_dict = SampleConsumerReportResponse.from_dict(sample_consumer_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
