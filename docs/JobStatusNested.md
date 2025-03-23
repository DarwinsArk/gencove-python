# JobStatusNested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**status** | **str** |  |
**note** | **str** |  | [optional]
**created** | **datetime** |  | [optional]

## Example

```python
from gencove_client.models.job_status_nested import JobStatusNested

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusNested from a JSON string
job_status_nested_instance = JobStatusNested.from_json(json)
# print the JSON string representation of the object
print(JobStatusNested.to_json())

# convert the object into a dict
job_status_nested_dict = job_status_nested_instance.to_dict()
# create an instance of JobStatusNested from a dict
job_status_nested_from_dict = JobStatusNested.from_dict(job_status_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
