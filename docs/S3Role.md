# S3Role


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_arn** | **str** |  |

## Example

```python
from gencove_client.models.s3_role import S3Role

# TODO update the JSON string below
json = "{}"
# create an instance of S3Role from a JSON string
s3_role_instance = S3Role.from_json(json)
# print the JSON string representation of the object
print(S3Role.to_json())

# convert the object into a dict
s3_role_dict = s3_role_instance.to_dict()
# create an instance of S3Role from a dict
s3_role_from_dict = S3Role.from_dict(s3_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
