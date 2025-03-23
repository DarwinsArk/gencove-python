# SampleCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_samples** | **int** |  |
**running_samples** | **int** |  |
**scheduled_samples** | **int** |  |
**succeeded_samples** | **int** |  |
**failed_samples** | **int** |  |

## Example

```python
from gencove_client.models.sample_counts import SampleCounts

# TODO update the JSON string below
json = "{}"
# create an instance of SampleCounts from a JSON string
sample_counts_instance = SampleCounts.from_json(json)
# print the JSON string representation of the object
print(SampleCounts.to_json())

# convert the object into a dict
sample_counts_dict = sample_counts_instance.to_dict()
# create an instance of SampleCounts from a dict
sample_counts_from_dict = SampleCounts.from_dict(sample_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
