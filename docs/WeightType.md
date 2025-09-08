# Enum: WeightType 




_Allowed LOINC codes for weight._



URI: [WeightType](WeightType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| BODY_WEIGHT_MEASURED | loinc:3141-9 | Body weight measured |
| BODY_WEIGHT_STATED | loinc:3142-7 | Body weight Stated |




## Slots

| Name | Description |
| ---  | --- |
| [weightType](weightType.md) | The type of weight measurement, e |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel






## LinkML Source

<details>
```yaml
name: WeightType
description: Allowed LOINC codes for weight.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
permissible_values:
  BODY_WEIGHT_MEASURED:
    text: BODY_WEIGHT_MEASURED
    description: Body weight measured
    meaning: loinc:3141-9
  BODY_WEIGHT_STATED:
    text: BODY_WEIGHT_STATED
    description: Body weight Stated
    meaning: loinc:3142-7

```
</details>
