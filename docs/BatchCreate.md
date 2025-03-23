# BatchCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  |
**batch_type** | **str** |  |
**sample_ids** | **List[str]** | List of sample IDs or if empty all available samples will be used |

## Example

```python
from gencove_client.models.batch_create import BatchCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCreate from a JSON string
batch_create_instance = BatchCreate.from_json(json)
# print the JSON string representation of the object
print(BatchCreate.to_json())

# convert the object into a dict
batch_create_dict = batch_create_instance.to_dict()
# create an instance of BatchCreate from a dict
batch_create_from_dict = BatchCreate.from_dict(batch_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
