# SampleAncestry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ancestry** | [**AncestrySelfNested**](AncestrySelfNested.md) |  |
**metadata** | [**AncestryMetadata**](AncestryMetadata.md) |  |

## Example

```python
from gencove_client.models.sample_ancestry import SampleAncestry

# TODO update the JSON string below
json = "{}"
# create an instance of SampleAncestry from a JSON string
sample_ancestry_instance = SampleAncestry.from_json(json)
# print the JSON string representation of the object
print(SampleAncestry.to_json())

# convert the object into a dict
sample_ancestry_dict = sample_ancestry_instance.to_dict()
# create an instance of SampleAncestry from a dict
sample_ancestry_from_dict = SampleAncestry.from_dict(sample_ancestry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
