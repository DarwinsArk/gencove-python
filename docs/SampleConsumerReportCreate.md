# SampleConsumerReportCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | [**ReportTypeEnum**](ReportTypeEnum.md) | Type of report to generate  * &#x60;prs&#x60; - prs | [optional]
**expires_in** | **int** | Token expiration time in seconds. Note that this value is for the JWT delivered in the URL. Once the URL is accessed, a fixed duration session (15 minutes) is created that may outlive this token | [optional] [default to 600]

## Example

```python
from gencove_client.models.sample_consumer_report_create import SampleConsumerReportCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SampleConsumerReportCreate from a JSON string
sample_consumer_report_create_instance = SampleConsumerReportCreate.from_json(json)
# print the JSON string representation of the object
print(SampleConsumerReportCreate.to_json())

# convert the object into a dict
sample_consumer_report_create_dict = sample_consumer_report_create_instance.to_dict()
# create an instance of SampleConsumerReportCreate from a dict
sample_consumer_report_create_from_dict = SampleConsumerReportCreate.from_dict(sample_consumer_report_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
