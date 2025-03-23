# QualityControlSelfNested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_expected** | **float** |  | [optional]
**value_measured** | **float** |  | [optional]
**value_string** | **str** |  | [optional]
**status** | **str** |  |

## Example

```python
from gencove_client.models.quality_control_self_nested import QualityControlSelfNested

# TODO update the JSON string below
json = "{}"
# create an instance of QualityControlSelfNested from a JSON string
quality_control_self_nested_instance = QualityControlSelfNested.from_json(json)
# print the JSON string representation of the object
print(QualityControlSelfNested.to_json())

# convert the object into a dict
quality_control_self_nested_dict = quality_control_self_nested_instance.to_dict()
# create an instance of QualityControlSelfNested from a dict
quality_control_self_nested_from_dict = QualityControlSelfNested.from_dict(quality_control_self_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
