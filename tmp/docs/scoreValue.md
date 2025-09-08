
# Class: ScoreValue

The score value calculated from a QuestionnaireResponse following a ScoreDefinition.

URI: [datamodel:ScoreValue](https://w3id.org/faqir/datamodel/ScoreValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ValueString],[ValueNumerical],[ValueNumerical]<scoreValueNumerical%200..1-++[ScoreValue&#124;scoreDefinitionType:ScoreType;scoreValueId:uriorcurie;scoreValueTimeStamp:datetime;scoreValueStatus:ScoreValueStatus],[ValueString]<scoreValueString%200..1-++[ScoreValue],[QuestionnaireResponse]<scoreValueDerivedFromQuestionnaireResponse%201..*-%20[ScoreValue],[ScoreDefinition]<scoreValueBasedOnScoreDefinition%201..1-%20[ScoreValue],[QuestionnaireResponse]-%20questionnaireResponseHasDerivedScoreValue%200..*>[ScoreValue],[ScoreDefinition]-%20scoreDefinitionHasScoreValue%200..*>[ScoreValue],[ScoreDefinition],[QuestionnaireResponse])](https://yuml.me/diagram/nofunky;dir:TB/class/[ValueString],[ValueNumerical],[ValueNumerical]<scoreValueNumerical%200..1-++[ScoreValue&#124;scoreDefinitionType:ScoreType;scoreValueId:uriorcurie;scoreValueTimeStamp:datetime;scoreValueStatus:ScoreValueStatus],[ValueString]<scoreValueString%200..1-++[ScoreValue],[QuestionnaireResponse]<scoreValueDerivedFromQuestionnaireResponse%201..*-%20[ScoreValue],[ScoreDefinition]<scoreValueBasedOnScoreDefinition%201..1-%20[ScoreValue],[QuestionnaireResponse]-%20questionnaireResponseHasDerivedScoreValue%200..*>[ScoreValue],[ScoreDefinition]-%20scoreDefinitionHasScoreValue%200..*>[ScoreValue],[ScoreDefinition],[QuestionnaireResponse])

## Referenced by Class

 *  **[QuestionnaireResponse](QuestionnaireResponse.md)** *[questionnaireResponseHasDerivedScoreValue](questionnaireResponseHasDerivedScoreValue.md)*  <sub>0..\*</sub>  **[ScoreValue](ScoreValue.md)**
 *  **[ScoreDefinition](ScoreDefinition.md)** *[scoreDefinitionHasScoreValue](scoreDefinitionHasScoreValue.md)*  <sub>0..\*</sub>  **[ScoreValue](ScoreValue.md)**

## Attributes


### Own

 * [scoreDefinitionType](scoreDefinitionType.md)  <sub>1..1</sub>
     * Description: Type of score: numerical_continuous, numerical_integer, numerical_percentage, numerical_z_score, numerical_t_score or categorical. Determines valid score values.
     * Range: [ScoreType](ScoreType.md)
 * [scoreValueBasedOnScoreDefinition](scoreValueBasedOnScoreDefinition.md)  <sub>1..1</sub>
     * Description: The ScoreDefinition that this ScoreValue is based on.
     * Range: [ScoreDefinition](ScoreDefinition.md)
 * [scoreValueDerivedFromQuestionnaireResponse](scoreValueDerivedFromQuestionnaireResponse.md)  <sub>1..\*</sub>
     * Description: The QuestionnaireResponse that contains the answers this ScoreValue is calculated from.
     * Range: [QuestionnaireResponse](QuestionnaireResponse.md)
 * [➞scoreValueId](scoreValue__scoreValueId.md)  <sub>1..1</sub>
     * Description: Unique identifier for the score value.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞scoreValueString](scoreValue__scoreValueString.md)  <sub>0..1</sub>
     * Description: String representation of the score value, used for categorical scores.
     * Range: [ValueString](ValueString.md)
 * [➞scoreValueNumerical](scoreValue__scoreValueNumerical.md)  <sub>0..1</sub>
     * Description: Numerical value of the score, used for numerical scores.
     * Range: [ValueNumerical](ValueNumerical.md)
 * [➞scoreValueTimeStamp](scoreValue__scoreValueTimeStamp.md)  <sub>1..1</sub>
     * Description: Timestamp when the score value was calculated.
     * Range: [Datetime](types/Datetime.md)
 * [➞scoreValueStatus](scoreValue__scoreValueStatus.md)  <sub>1..1</sub>
     * Description: Status of the score value, e.g., draft, final.
     * Range: [ScoreValueStatus](ScoreValueStatus.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:ScoreValue |