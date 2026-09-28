# Enum: QoScoreType 




_The type of score definition, which can be numerical or categorical._



URI: [QoScoreType](QoScoreType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| numerical_continuous | xsd:float | Continuous numerical score (e |
| numerical_integer | xsd:integer | Integer numerical score (e |
| numerical_percentage | xsd:float | Percentage score (0-100%) |
| numerical_z_score | xsd:float | Standardized Z-score (mean=0, std=1) |
| numerical_t_score | xsd:float | Standardized T-score (mean=50, std=10) |
| categorical | xsd:NMTOKENS | Ordinal categories (e |




## Slots

| Name | Description |
| ---  | --- |
| [prov_type](prov_type.md) | Type of score: numerical_continuous, numerical_integer, numerical_percentage,... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o






## LinkML Source

<details>
```yaml
name: qo_ScoreType
description: The type of score definition, which can be numerical or categorical.
from_schema: https://ns.faqir.org/q-o
rank: 1000
enum_uri: qo:ScoreType
permissible_values:
  numerical_continuous:
    text: numerical_continuous
    description: Continuous numerical score (e.g., 0.785, 82.5)
    meaning: xsd:float
  numerical_integer:
    text: numerical_integer
    description: Integer numerical score (e.g., 5, 10, 27)
    meaning: xsd:integer
  numerical_percentage:
    text: numerical_percentage
    description: Percentage score (0-100%)
    meaning: xsd:float
  numerical_z_score:
    text: numerical_z_score
    description: Standardized Z-score (mean=0, std=1)
    meaning: xsd:float
  numerical_t_score:
    text: numerical_t_score
    description: Standardized T-score (mean=50, std=10)
    meaning: xsd:float
  categorical:
    text: categorical
    description: Ordinal categories (e.g., Low, Medium, High or Yes, No or Type a,
      Type b)
    meaning: xsd:NMTOKENS

```
</details>
