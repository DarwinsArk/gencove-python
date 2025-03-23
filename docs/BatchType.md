# BatchType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key from pipeline config |
**description** | **str** |  | [optional]

## Example

```python
from gencove_client.models.batch_type import BatchType

# TODO update the JSON string below
json = "{}"
# create an instance of BatchType from a JSON string
batch_type_instance = BatchType.from_json(json)
# print the JSON string representation of the object
print(BatchType.to_json())

# convert the object into a dict
batch_type_dict = batch_type_instance.to_dict()
# create an instance of BatchType from a dict
batch_type_from_dict = BatchType.from_dict(batch_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
