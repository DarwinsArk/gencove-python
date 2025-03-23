# BatchStatusNested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**status** | **str** |  |
**created** | **datetime** |  | [optional]

## Example

```python
from gencove_client.models.batch_status_nested import BatchStatusNested

# TODO update the JSON string below
json = "{}"
# create an instance of BatchStatusNested from a JSON string
batch_status_nested_instance = BatchStatusNested.from_json(json)
# print the JSON string representation of the object
print(BatchStatusNested.to_json())

# convert the object into a dict
batch_status_nested_dict = batch_status_nested_instance.to_dict()
# create an instance of BatchStatusNested from a dict
batch_status_nested_from_dict = BatchStatusNested.from_dict(batch_status_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
