# Enum: ScoreParameterType 




_The type of parameter used in the score definition._



URI: [ScoreParameterType](ScoreParameterType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| numerical | xsd:float | Numerical parameter (e |
| dateTime | xsd:dateTime | dateTime parameter formatted as YYYY-MM-DDThh:mm:ss+zz:zz |




## Slots

| Name | Description |
| ---  | --- |
| [scoreParameterType](scoreParameterType.md) | Type of parameter: numerical or dateTime |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel






## LinkML Source

<details>
```yaml
name: ScoreParameterType
description: The type of parameter used in the score definition.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
enum_uri: faqir:ScoreParameterType
permissible_values:
  numerical:
    text: numerical
    description: Numerical parameter (e.g., 0.785, 82)
    meaning: xsd:float
  dateTime:
    text: dateTime
    description: dateTime parameter formatted as YYYY-MM-DDThh:mm:ss+zz:zz.
    meaning: xsd:dateTime

```
</details>
