# PipelineCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly]
**name** | **str** | Name from pipeline config |
**key** | **str** | Key from pipeline config |
**private** | **bool** | True if private | [optional]
**merge_vcfs_enabled** | **bool** | Set to True if MergeVCFs can be run | [optional]
**supported_project_modifications** | **object** | List of project modification objects supported by the pipeline. Only the modifications listed under &#39;key&#39; can be used. Note that &#39;value&#39; is only used by the front-end to determine whether the check box should be set to True or False by default. | [optional]
**modifications_enabled** | **str** |  | [optional] [readonly]
**species** | **str** | Species | [optional] [readonly]
**pipeline_category** | **str** | Category of the pipeline capability | [optional]
**description_markdown** | **str** | Description markdown of a pipeline capability.  | [optional] [readonly]
**datasets** | **str** | Dataset descriptions. | [optional] [readonly]
**steps** | **str** | Pipeline capability steps that are enabled. | [optional] [readonly]

## Example

```python
from gencove_client.models.pipeline_capabilities import PipelineCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineCapabilities from a JSON string
pipeline_capabilities_instance = PipelineCapabilities.from_json(json)
# print the JSON string representation of the object
print(PipelineCapabilities.to_json())

# convert the object into a dict
pipeline_capabilities_dict = pipeline_capabilities_instance.to_dict()
# create an instance of PipelineCapabilities from a dict
pipeline_capabilities_from_dict = PipelineCapabilities.from_dict(pipeline_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
