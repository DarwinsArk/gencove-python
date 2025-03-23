# S3ObjectNested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | [optional]
**object_name** | **str** |  | [optional]

## Example

```python
from gencove_client.models.s3_object_nested import S3ObjectNested

# TODO update the JSON string below
json = "{}"
# create an instance of S3ObjectNested from a JSON string
s3_object_nested_instance = S3ObjectNested.from_json(json)
# print the JSON string representation of the object
print(S3ObjectNested.to_json())

# convert the object into a dict
s3_object_nested_dict = s3_object_nested_instance.to_dict()
# create an instance of S3ObjectNested from a dict
s3_object_nested_from_dict = S3ObjectNested.from_dict(s3_object_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
