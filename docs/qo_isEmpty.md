

# Slot: qo_isEmpty 


_Specifies an explicit assertion that an item was purposefully omitted or unpopulated by the respondent rather than skipped due to systemic error._





URI: [qo:isEmpty](https://ns.faqir.org/q-o#isEmpty)
Alias: qo_isEmpty

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QoAnswer](QoAnswer.md) | A recorded value, or selection provided in response to a specific inquiry ite... |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:isEmpty |
| native | qo:qo_isEmpty |




## LinkML Source

<details>
```yaml
name: qo_isEmpty
description: Specifies an explicit assertion that an item was purposefully omitted
  or unpopulated by the respondent rather than skipped due to systemic error.
from_schema: https://ns.faqir.org/q-o
rank: 1000
slot_uri: qo:isEmpty
ifabsent: 'False'
alias: qo_isEmpty
owner: qo_Answer
domain_of:
- qo_Answer
range: boolean

```
</details>