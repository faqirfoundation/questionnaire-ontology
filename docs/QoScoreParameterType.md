# Enum: QoScoreParameterType 




_The type of parameter used in the score definition._



URI: [QoScoreParameterType](QoScoreParameterType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| numerical | xsd:float | Numerical parameter (e |
| dateTime | xsd:dateTime | dateTime parameter formatted as YYYY-MM-DDThh:mm:ss+zz:zz |




## Slots

| Name | Description |
| ---  | --- |
| [prov_type](prov_type.md) | Type of parameter: numerical or dateTime |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o






## LinkML Source

<details>
```yaml
name: qo_ScoreParameterType
description: The type of parameter used in the score definition.
from_schema: https://ns.faqir.org/q-o
rank: 1000
enum_uri: qo:ScoreParameterType
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
