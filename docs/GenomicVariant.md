# GenomicVariant

Serializes a `genomic_variants.services.Variant` record.  `genotype` is an object keyed by the VCF FORMAT field names, e.g. `{\"GT\": \"0|0\", \"DS\": \"0\", \"GP\": \"1,0,0\", \"RC\": \"1\", \"AC\": \"0\", \"DP\": \"1\"}`. All values are kept as raw strings so the payload mirrors the VCF exactly; callers interpret `GT` allele indexes against `alt`.  `genotype_confidence` is the confidence of the called genotype: the max of the `GP` posteriors (the same quantity the VCF's LOWCONF filter thresholds at 0.9), a probability in [0, 1] or null when the record has no `GP` field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chromosome** | **str** |  |
**position** | **int** |  |
**rsid** | **str** |  |
**ref** | **str** |  |
**alt** | **List[str]** |  |
**genotype** | **Dict[str, str]** |  |
**genotype_confidence** | **float** |  |
**quality** | **float** |  |
**info** | **Dict[str, object]** |  |

## Example

```python
from gencove_client.models.genomic_variant import GenomicVariant

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicVariant from a JSON string
genomic_variant_instance = GenomicVariant.from_json(json)
# print the JSON string representation of the object
print(GenomicVariant.to_json())

# convert the object into a dict
genomic_variant_dict = genomic_variant_instance.to_dict()
# create an instance of GenomicVariant from a dict
genomic_variant_from_dict = GenomicVariant.from_dict(genomic_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
