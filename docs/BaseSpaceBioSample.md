# BaseSpaceBioSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basespace_id** | **str** |  |
**basespace_bio_sample_name** | **str** |  |
**basespace_date_created** | **datetime** |  |
**basespace_date_modified** | **datetime** |  |
**basespace_status** | **str** |  |
**basespace_lab_status** | **str** |  |
**basespace_user_owned_by_id** | **str** |  |

## Example

```python
from gencove_client.models.base_space_bio_sample import BaseSpaceBioSample

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSpaceBioSample from a JSON string
base_space_bio_sample_instance = BaseSpaceBioSample.from_json(json)
# print the JSON string representation of the object
print(BaseSpaceBioSample.to_json())

# convert the object into a dict
base_space_bio_sample_dict = base_space_bio_sample_instance.to_dict()
# create an instance of BaseSpaceBioSample from a dict
base_space_bio_sample_from_dict = BaseSpaceBioSample.from_dict(base_space_bio_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
