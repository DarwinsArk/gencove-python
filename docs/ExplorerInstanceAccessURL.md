# ExplorerInstanceAccessURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  |
**access_token_expiration** | **int** | Number of seconds before the URL expires. Maximum is 86400 seconds. | [optional]

## Example

```python
from gencove_client.models.explorer_instance_access_url import ExplorerInstanceAccessURL

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerInstanceAccessURL from a JSON string
explorer_instance_access_url_instance = ExplorerInstanceAccessURL.from_json(json)
# print the JSON string representation of the object
print(ExplorerInstanceAccessURL.to_json())

# convert the object into a dict
explorer_instance_access_url_dict = explorer_instance_access_url_instance.to_dict()
# create an instance of ExplorerInstanceAccessURL from a dict
explorer_instance_access_url_from_dict = ExplorerInstanceAccessURL.from_dict(explorer_instance_access_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
