# SampleManifestUpload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_manifest** | **str** |  | [optional] [readonly]

## Example

```python
from gencove_client.models.sample_manifest_upload import SampleManifestUpload

# TODO update the JSON string below
json = "{}"
# create an instance of SampleManifestUpload from a JSON string
sample_manifest_upload_instance = SampleManifestUpload.from_json(json)
# print the JSON string representation of the object
print(SampleManifestUpload.to_json())

# convert the object into a dict
sample_manifest_upload_dict = sample_manifest_upload_instance.to_dict()
# create an instance of SampleManifestUpload from a dict
sample_manifest_upload_from_dict = SampleManifestUpload.from_dict(sample_manifest_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
