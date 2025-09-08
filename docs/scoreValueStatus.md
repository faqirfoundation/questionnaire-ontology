# Enum: ScoreValueStatus 




_The status of a score value, indicating its validity and completeness._



URI: [ScoreValueStatus](ScoreValueStatus.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| valid | None | Score is valid and complete |
| incomplete | None | Score calculated with missing optional data |
| estimated | None | Score is an estimate due to missing data |
| warning | None | Score calculated with warnings or anomalies |
| error | None | Score calculation error or invalid data |
| pending | None | Score calculation is pending |
| amended | None | Score has been amended after initial calculation |




## Slots

| Name | Description |
| ---  | --- |
| [scoreValueStatus](scoreValueStatus.md) | Status of the score value, e |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel






## LinkML Source

<details>
```yaml
name: ScoreValueStatus
description: The status of a score value, indicating its validity and completeness.
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
enum_uri: faqir:ScoreValueStatus
permissible_values:
  valid:
    text: valid
    description: Score is valid and complete
  incomplete:
    text: incomplete
    description: Score calculated with missing optional data
  estimated:
    text: estimated
    description: Score is an estimate due to missing data
  warning:
    text: warning
    description: Score calculated with warnings or anomalies
  error:
    text: error
    description: Score calculation error or invalid data
  pending:
    text: pending
    description: Score calculation is pending
  amended:
    text: amended
    description: Score has been amended after initial calculation

```
</details>
