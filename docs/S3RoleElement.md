# S3RoleElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_arn** | **str** |  | [optional]
**external_id** | **str** |  | [optional]
**aws_region** | **str** |  | [optional] [readonly]
**s3_bucket** | **str** |  | [optional]
**s3_prefix** | **str** |  | [optional]

## Example

```python
from gencove_client.models.s3_role_element import S3RoleElement

# TODO update the JSON string below
json = "{}"
# create an instance of S3RoleElement from a JSON string
s3_role_element_instance = S3RoleElement.from_json(json)
# print the JSON string representation of the object
print(S3RoleElement.to_json())

# convert the object into a dict
s3_role_element_dict = s3_role_element_instance.to_dict()
# create an instance of S3RoleElement from a dict
s3_role_element_from_dict = S3RoleElement.from_dict(s3_role_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
