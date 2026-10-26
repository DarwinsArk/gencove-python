# CostReportFile

A report file, its link signed with the reader (``x-gncv-userid`` names who downloaded it), as sample files are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly]
**s3_path** | **str** | S3 object key | [optional]
**size** | **int** | Size as reported by AWS in bytes | [optional]
**download_url** | **str** | Download url | [readonly]
**file_type** | **str** | File extension | [readonly]
**checksum_sha256** | **str** | Object&#39;s sha256 Checksum | [optional]
**shadow_mode** | **bool** | If true, file is only accessible by organizations with shadow mode access enabled. | [optional]

## Example

```python
from gencove_client.models.cost_report_file import CostReportFile

# TODO update the JSON string below
json = "{}"
# create an instance of CostReportFile from a JSON string
cost_report_file_instance = CostReportFile.from_json(json)
# print the JSON string representation of the object
print(CostReportFile.to_json())

# convert the object into a dict
cost_report_file_dict = cost_report_file_instance.to_dict()
# create an instance of CostReportFile from a dict
cost_report_file_from_dict = CostReportFile.from_dict(cost_report_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
