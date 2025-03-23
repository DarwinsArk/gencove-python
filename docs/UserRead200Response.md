# UserRead200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**BasespaceProjectBiosamplesRead200ResponseMeta**](BasespaceProjectBiosamplesRead200ResponseMeta.md) |  | [optional]
**results** | [**List[User]**](User.md) |  |

## Example

```python
from gencove_client.models.user_read200_response import UserRead200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserRead200Response from a JSON string
user_read200_response_instance = UserRead200Response.from_json(json)
# print the JSON string representation of the object
print(UserRead200Response.to_json())

# convert the object into a dict
user_read200_response_dict = user_read200_response_instance.to_dict()
# create an instance of UserRead200Response from a dict
user_read200_response_from_dict = UserRead200Response.from_dict(user_read200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
