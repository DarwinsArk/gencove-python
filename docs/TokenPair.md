# TokenPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh** | **str** |  | [optional]
**access** | **str** |  | [optional]

## Example

```python
from gencove_client.models.token_pair import TokenPair

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPair from a JSON string
token_pair_instance = TokenPair.from_json(json)
# print the JSON string representation of the object
print(TokenPair.to_json())

# convert the object into a dict
token_pair_dict = token_pair_instance.to_dict()
# create an instance of TokenPair from a dict
token_pair_from_dict = TokenPair.from_dict(token_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
