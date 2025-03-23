# Activation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  |
**token** | **str** |  |

## Example

```python
from gencove_client.models.activation import Activation

# TODO update the JSON string below
json = "{}"
# create an instance of Activation from a JSON string
activation_instance = Activation.from_json(json)
# print the JSON string representation of the object
print(Activation.to_json())

# convert the object into a dict
activation_dict = activation_instance.to_dict()
# create an instance of Activation from a dict
activation_from_dict = Activation.from_dict(activation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
