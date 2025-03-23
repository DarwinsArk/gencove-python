# QualityControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quality_control_type** | [**QualityControlType**](QualityControlType.md) |  |
**quality_control** | [**QualityControlSelfNested**](QualityControlSelfNested.md) |  |

## Example

```python
from gencove_client.models.quality_control import QualityControl

# TODO update the JSON string below
json = "{}"
# create an instance of QualityControl from a JSON string
quality_control_instance = QualityControl.from_json(json)
# print the JSON string representation of the object
print(QualityControl.to_json())

# convert the object into a dict
quality_control_dict = quality_control_instance.to_dict()
# create an instance of QualityControl from a dict
quality_control_from_dict = QualityControl.from_dict(quality_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
