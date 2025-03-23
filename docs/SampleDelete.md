# SampleDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_ids** | **List[str]** | List of sample IDs |

## Example

```python
from gencove_client.models.sample_delete import SampleDelete

# TODO update the JSON string below
json = "{}"
# create an instance of SampleDelete from a JSON string
sample_delete_instance = SampleDelete.from_json(json)
# print the JSON string representation of the object
print(SampleDelete.to_json())

# convert the object into a dict
sample_delete_dict = sample_delete_instance.to_dict()
# create an instance of SampleDelete from a dict
sample_delete_from_dict = SampleDelete.from_dict(sample_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
