
# Class: ScoreDefinition

A score calculated from questions.

URI: [datamodel:ScoreDefinition](https://w3id.org/faqir/datamodel/ScoreDefinition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Section],[ScoreValue],[ScoreParameter],[IntervalParams]<scoreDefinitionIntervalParams%200..1-++[ScoreDefinition&#124;scoreDefinitionType:ScoreType;scoreDefinitionId:uriorcurie;scoreDefinitionLabel:string;scoreDefinitionFormula:string;scoreDefinitionCategories:string%20*;scoreDefinitionInterpretationGuide:string%20%3F],[Section]<scoreDefinitionUsedBySection%200..*-%20[ScoreDefinition],[Questionnaire]<scoreDefinitionUsedByQuestionnare%200..*-%20[ScoreDefinition],[Organization]<scoreDefinitionAuthoredByOrg%200..*-%20[ScoreDefinition],[ScoreValue]<scoreDefinitionHasScoreValue%200..*-%20[ScoreDefinition],[Question]<scoreDefinitionUsesQuestion%201..*-%20[ScoreDefinition],[ScoreParameter]<scoreDefinitionHasScoreParameter%200..*-%20[ScoreDefinition],[Organization]-%20organizationAuthorsScoreDefinition%200..*>[ScoreDefinition],[Question]-%20questionUsedInScoreDefinition%200..*>[ScoreDefinition],[Questionnaire]-%20questionnaireUsesScoreDefinition%200..*>[ScoreDefinition],[ScoreParameter]-%20scoreParameterPartOfScoreDefinition%201..1>[ScoreDefinition],[ScoreValue]-%20scoreValueBasedOnScoreDefinition%201..1>[ScoreDefinition],[Section]-%20sectionUsesScoreDefinition%200..*>[ScoreDefinition],[Questionnaire],[Question],[Organization],[IntervalParams])](https://yuml.me/diagram/nofunky;dir:TB/class/[Section],[ScoreValue],[ScoreParameter],[IntervalParams]<scoreDefinitionIntervalParams%200..1-++[ScoreDefinition&#124;scoreDefinitionType:ScoreType;scoreDefinitionId:uriorcurie;scoreDefinitionLabel:string;scoreDefinitionFormula:string;scoreDefinitionCategories:string%20*;scoreDefinitionInterpretationGuide:string%20%3F],[Section]<scoreDefinitionUsedBySection%200..*-%20[ScoreDefinition],[Questionnaire]<scoreDefinitionUsedByQuestionnare%200..*-%20[ScoreDefinition],[Organization]<scoreDefinitionAuthoredByOrg%200..*-%20[ScoreDefinition],[ScoreValue]<scoreDefinitionHasScoreValue%200..*-%20[ScoreDefinition],[Question]<scoreDefinitionUsesQuestion%201..*-%20[ScoreDefinition],[ScoreParameter]<scoreDefinitionHasScoreParameter%200..*-%20[ScoreDefinition],[Organization]-%20organizationAuthorsScoreDefinition%200..*>[ScoreDefinition],[Question]-%20questionUsedInScoreDefinition%200..*>[ScoreDefinition],[Questionnaire]-%20questionnaireUsesScoreDefinition%200..*>[ScoreDefinition],[ScoreParameter]-%20scoreParameterPartOfScoreDefinition%201..1>[ScoreDefinition],[ScoreValue]-%20scoreValueBasedOnScoreDefinition%201..1>[ScoreDefinition],[Section]-%20sectionUsesScoreDefinition%200..*>[ScoreDefinition],[Questionnaire],[Question],[Organization],[IntervalParams])

## Referenced by Class

 *  **[Organization](Organization.md)** *[organizationAuthorsScoreDefinition](organizationAuthorsScoreDefinition.md)*  <sub>0..\*</sub>  **[ScoreDefinition](ScoreDefinition.md)**
 *  **[Question](Question.md)** *[questionUsedInScoreDefinition](questionUsedInScoreDefinition.md)*  <sub>0..\*</sub>  **[ScoreDefinition](ScoreDefinition.md)**
 *  **[Questionnaire](Questionnaire.md)** *[questionnaireUsesScoreDefinition](questionnaireUsesScoreDefinition.md)*  <sub>0..\*</sub>  **[ScoreDefinition](ScoreDefinition.md)**
 *  **[ScoreParameter](ScoreParameter.md)** *[scoreParameterPartOfScoreDefinition](scoreParameterPartOfScoreDefinition.md)*  <sub>1..1</sub>  **[ScoreDefinition](ScoreDefinition.md)**
 *  **[ScoreValue](ScoreValue.md)** *[scoreValueBasedOnScoreDefinition](scoreValueBasedOnScoreDefinition.md)*  <sub>1..1</sub>  **[ScoreDefinition](ScoreDefinition.md)**
 *  **[Section](Section.md)** *[sectionUsesScoreDefinition](sectionUsesScoreDefinition.md)*  <sub>0..\*</sub>  **[ScoreDefinition](ScoreDefinition.md)**

## Attributes


### Own

 * [scoreDefinitionType](scoreDefinitionType.md)  <sub>1..1</sub>
     * Description: Type of score: numerical_continuous, numerical_integer, numerical_percentage, numerical_z_score, numerical_t_score or categorical. Determines valid score values.
     * Range: [ScoreType](ScoreType.md)
 * [scoreDefinitionHasScoreParameter](scoreDefinitionHasScoreParameter.md)  <sub>0..\*</sub>
     * Description: The ScoreParameter that is required for this ScoreDefinition.
     * Range: [ScoreParameter](ScoreParameter.md)
 * [scoreDefinitionUsesQuestion](scoreDefinitionUsesQuestion.md)  <sub>1..\*</sub>
     * Description: The Question(s) that this ScoreDefinition is based on.
     * Range: [Question](Question.md)
 * [scoreDefinitionHasScoreValue](scoreDefinitionHasScoreValue.md)  <sub>0..\*</sub>
     * Description: The ScoreValue that is calculated following this ScoreDefinition.
     * Range: [ScoreValue](ScoreValue.md)
 * [scoreDefinitionAuthoredByOrg](scoreDefinitionAuthoredByOrg.md)  <sub>0..\*</sub>
     * Description: The Organization that has created this ScoreDefinition.
     * Range: [Organization](Organization.md)
 * [scoreDefinitionUsedByQuestionnare](scoreDefinitionUsedByQuestionnare.md)  <sub>0..\*</sub>
     * Description: The Questionnaires that this ScoreDefinition is applied in.
     * Range: [Questionnaire](Questionnaire.md)
 * [scoreDefinitionUsedBySection](scoreDefinitionUsedBySection.md)  <sub>0..\*</sub>
     * Description: The Sections that this ScoreDefinition is applied in.
     * Range: [Section](Section.md)
 * [➞scoreDefinitionId](scoreDefinition__scoreDefinitionId.md)  <sub>1..1</sub>
     * Description: Unique identifier for the score definition.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞scoreDefinitionLabel](scoreDefinition__scoreDefinitionLabel.md)  <sub>1..1</sub>
     * Description: Label or title of the score definition.
     * Range: [String](types/String.md)
 * [➞scoreDefinitionIntervalParams](scoreDefinition__scoreDefinitionIntervalParams.md)  <sub>0..1</sub>
     * Description: Minimum and maximum values for numerical_percentage and numerical_z_score scores.
     * Range: [IntervalParams](IntervalParams.md)
 * [➞scoreDefinitionFormula](scoreDefinition__scoreDefinitionFormula.md)  <sub>1..1</sub>
     * Description: The formula used to calculate the score.
     * Range: [String](types/String.md)
 * [➞scoreDefinitionCategories](scoreDefinition__scoreDefinitionCategories.md)  <sub>0..\*</sub>
     * Description: Categories for categorical scores.
     * Range: [String](types/String.md)
 * [➞scoreDefinitionInterpretationGuide](scoreDefinition__scoreDefinitionInterpretationGuide.md)  <sub>0..1</sub>
     * Description: How to interpret the score values. English explanation.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:ScoreDefinition |