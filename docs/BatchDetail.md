# BatchDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**name** | **str** |  | [optional]
**batch_type** | **str** |  | [optional] [readonly]
**sample_ids** | **List[str]** |  |
**last_status** | [**BatchStatusNested**](BatchStatusNested.md) |  | [optional]
**files** | [**List[BatchFileNested]**](BatchFileNested.md) | Batch files | [optional] [readonly]

## Example

```python
from gencove_client.models.batch_detail import BatchDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDetail from a JSON string
batch_detail_instance = BatchDetail.from_json(json)
# print the JSON string representation of the object
print(BatchDetail.to_json())

# convert the object into a dict
batch_detail_dict = batch_detail_instance.to_dict()
# create an instance of BatchDetail from a dict
batch_detail_from_dict = BatchDetail.from_dict(batch_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
