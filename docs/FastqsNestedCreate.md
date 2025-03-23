# FastqsNestedCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**r1** | [**UploadNestedCreate**](UploadNestedCreate.md) |  |
**r2** | [**UploadNestedCreate**](UploadNestedCreate.md) |  | [optional]

## Example

```python
from gencove_client.models.fastqs_nested_create import FastqsNestedCreate

# TODO update the JSON string below
json = "{}"
# create an instance of FastqsNestedCreate from a JSON string
fastqs_nested_create_instance = FastqsNestedCreate.from_json(json)
# print the JSON string representation of the object
print(FastqsNestedCreate.to_json())

# convert the object into a dict
fastqs_nested_create_dict = fastqs_nested_create_instance.to_dict()
# create an instance of FastqsNestedCreate from a dict
fastqs_nested_create_from_dict = FastqsNestedCreate.from_dict(fastqs_nested_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
