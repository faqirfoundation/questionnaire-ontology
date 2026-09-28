
# Enum: qo_ScoreType

The type of score definition, which can be numerical or categorical.

URI: [qo:qo_ScoreType](https://ns.faqir.org/q-o#qo_ScoreType)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| numerical_continuous | Continuous numerical score (e.g., 0.785, 82.5) | xsd:float |  |
| numerical_integer | Integer numerical score (e.g., 5, 10, 27) | xsd:integer |  |
| numerical_percentage | Percentage score (0-100%) | xsd:float |  |
| numerical_z_score | Standardized Z-score (mean=0, std=1) | xsd:float |  |
| numerical_t_score | Standardized T-score (mean=50, std=10) | xsd:float |  |
| categorical | Ordinal categories (e.g., Low, Medium, High or Yes, No or Type a, Type b) | xsd:NMTOKENS |  |

