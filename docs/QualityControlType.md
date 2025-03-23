# QualityControlType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  |
**type** | **str** |  |
**name** | **str** |  | [optional] [readonly]
**description_markdown** | **str** |  | [optional] [readonly]
**display_type** | **str** |  | [optional] [readonly]
**display_only_if_failed** | **str** |  | [optional] [readonly]

## Example

```python
from gencove_client.models.quality_control_type import QualityControlType

# TODO update the JSON string below
json = "{}"
# create an instance of QualityControlType from a JSON string
quality_control_type_instance = QualityControlType.from_json(json)
# print the JSON string representation of the object
print(QualityControlType.to_json())

# convert the object into a dict
quality_control_type_dict = quality_control_type_instance.to_dict()
# create an instance of QualityControlType from a dict
quality_control_type_from_dict = QualityControlType.from_dict(quality_control_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
