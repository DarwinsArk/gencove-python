# S3ProjectsAutoimportCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**topic_arn** | **str** | SNS Topic where events of added samples will be received. | [optional]

## Example

```python
from gencove_client.models.s3_projects_autoimport_create import S3ProjectsAutoimportCreate

# TODO update the JSON string below
json = "{}"
# create an instance of S3ProjectsAutoimportCreate from a JSON string
s3_projects_autoimport_create_instance = S3ProjectsAutoimportCreate.from_json(json)
# print the JSON string representation of the object
print(S3ProjectsAutoimportCreate.to_json())

# convert the object into a dict
s3_projects_autoimport_create_dict = s3_projects_autoimport_create_instance.to_dict()
# create an instance of S3ProjectsAutoimportCreate from a dict
s3_projects_autoimport_create_from_dict = S3ProjectsAutoimportCreate.from_dict(s3_projects_autoimport_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
