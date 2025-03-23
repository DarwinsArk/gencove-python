# BatchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**name** | **str** |  | [optional]
**batch_type** | **str** |  | [optional] [readonly]
**last_status** | [**BatchStatusNested**](BatchStatusNested.md) |  | [optional]
**files** | [**List[BatchFileNested]**](BatchFileNested.md) | Batch files | [optional] [readonly]

## Example

```python
from gencove_client.models.batch_list import BatchList

# TODO update the JSON string below
json = "{}"
# create an instance of BatchList from a JSON string
batch_list_instance = BatchList.from_json(json)
# print the JSON string representation of the object
print(BatchList.to_json())

# convert the object into a dict
batch_list_dict = batch_list_instance.to_dict()
# create an instance of BatchList from a dict
batch_list_from_dict = BatchList.from_dict(batch_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
