# ExistingSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional]
**sample_id** | **str** |  |

## Example

```python
from gencove_client.models.existing_sample import ExistingSample

# TODO update the JSON string below
json = "{}"
# create an instance of ExistingSample from a JSON string
existing_sample_instance = ExistingSample.from_json(json)
# print the JSON string representation of the object
print(ExistingSample.to_json())

# convert the object into a dict
existing_sample_dict = existing_sample_instance.to_dict()
# create an instance of ExistingSample from a dict
existing_sample_from_dict = ExistingSample.from_dict(existing_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
