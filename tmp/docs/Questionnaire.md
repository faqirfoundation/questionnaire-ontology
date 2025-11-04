
# Class: Questionnaire

A questionnaire that can be answered (collection of questions).

URI: [datamodel:Questionnaire](https://w3id.org/faqir/datamodel/Questionnaire)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ScoreDefinition],[QuestionnaireResponse],[Procedure]<questionnairePartOfProcedure%200..*-%20[Questionnaire&#124;questionnaireId:uriorcurie;questionnaireLabel:string;questionnaireStatus:QuestionnaireStatus;questionnaireVersion:string;questionnaireLastUpdated:datetime],[Organization]<questionnaireAuthoredByOrg%200..*-%20[Questionnaire],[ScoreDefinition]<questionnaireUsesScoreDefinition%200..*-%20[Questionnaire],[OrderedSection]<questionnaireHasOrderedSection%200..*-++[Questionnaire],[OrderedQuestion]<questionnaireHasOrderedQuestion%200..*-++[Questionnaire],[QuestionnaireResponse]<questionnaireHasQuestionnaireResponse%200..*-%20[Questionnaire],[OrderedQuestion]-%20orderedQuestionPartOfQuestionnaire%200..1>[Questionnaire],[OrderedSection]-%20orderedSectionPartOfQuestionnaire%200..1>[Questionnaire],[Organization]-%20organizationAuthorsQuestionnaire%200..*>[Questionnaire],[Procedure]-%20procedureHasQuestionnaire%200..*>[Questionnaire],[QuestionnaireResponse]-%20questionnaireResponseToQuestionnaire%201..1>[Questionnaire],[ScoreDefinition]-%20scoreDefinitionUsedByQuestionnare%200..*>[Questionnaire],[Procedure],[Organization],[OrderedSection],[OrderedQuestion])](https://yuml.me/diagram/nofunky;dir:TB/class/[ScoreDefinition],[QuestionnaireResponse],[Procedure]<questionnairePartOfProcedure%200..*-%20[Questionnaire&#124;questionnaireId:uriorcurie;questionnaireLabel:string;questionnaireStatus:QuestionnaireStatus;questionnaireVersion:string;questionnaireLastUpdated:datetime],[Organization]<questionnaireAuthoredByOrg%200..*-%20[Questionnaire],[ScoreDefinition]<questionnaireUsesScoreDefinition%200..*-%20[Questionnaire],[OrderedSection]<questionnaireHasOrderedSection%200..*-++[Questionnaire],[OrderedQuestion]<questionnaireHasOrderedQuestion%200..*-++[Questionnaire],[QuestionnaireResponse]<questionnaireHasQuestionnaireResponse%200..*-%20[Questionnaire],[OrderedQuestion]-%20orderedQuestionPartOfQuestionnaire%200..1>[Questionnaire],[OrderedSection]-%20orderedSectionPartOfQuestionnaire%200..1>[Questionnaire],[Organization]-%20organizationAuthorsQuestionnaire%200..*>[Questionnaire],[Procedure]-%20procedureHasQuestionnaire%200..*>[Questionnaire],[QuestionnaireResponse]-%20questionnaireResponseToQuestionnaire%201..1>[Questionnaire],[ScoreDefinition]-%20scoreDefinitionUsedByQuestionnare%200..*>[Questionnaire],[Procedure],[Organization],[OrderedSection],[OrderedQuestion])

## Referenced by Class

 *  **[OrderedQuestion](OrderedQuestion.md)** *[orderedQuestionPartOfQuestionnaire](orderedQuestionPartOfQuestionnaire.md)*  <sub>0..1</sub>  **[Questionnaire](Questionnaire.md)**
 *  **[OrderedSection](OrderedSection.md)** *[orderedSectionPartOfQuestionnaire](orderedSectionPartOfQuestionnaire.md)*  <sub>0..1</sub>  **[Questionnaire](Questionnaire.md)**
 *  **[Organization](Organization.md)** *[organizationAuthorsQuestionnaire](organizationAuthorsQuestionnaire.md)*  <sub>0..\*</sub>  **[Questionnaire](Questionnaire.md)**
 *  **[Procedure](Procedure.md)** *[procedureHasQuestionnaire](procedureHasQuestionnaire.md)*  <sub>0..\*</sub>  **[Questionnaire](Questionnaire.md)**
 *  **[QuestionnaireResponse](QuestionnaireResponse.md)** *[questionnaireResponseToQuestionnaire](questionnaireResponseToQuestionnaire.md)*  <sub>1..1</sub>  **[Questionnaire](Questionnaire.md)**
 *  **[ScoreDefinition](ScoreDefinition.md)** *[scoreDefinitionUsedByQuestionnare](scoreDefinitionUsedByQuestionnare.md)*  <sub>0..\*</sub>  **[Questionnaire](Questionnaire.md)**

## Attributes


### Own

 * [questionnaireHasQuestionnaireResponse](questionnaireHasQuestionnaireResponse.md)  <sub>0..\*</sub>
     * Description: The QuestionnaireResponse that is associated with this Questionnaire.
     * Range: [QuestionnaireResponse](QuestionnaireResponse.md)
 * [questionnaireHasOrderedQuestion](questionnaireHasOrderedQuestion.md)  <sub>0..\*</sub>
     * Description: The Question that is part of this Questionnaire, with their display order.
     * Range: [OrderedQuestion](OrderedQuestion.md)
 * [questionnaireHasOrderedSection](questionnaireHasOrderedSection.md)  <sub>0..\*</sub>
     * Description: The Section that is part of this Questionnaire, with their display order.
     * Range: [OrderedSection](OrderedSection.md)
 * [questionnaireUsesScoreDefinition](questionnaireUsesScoreDefinition.md)  <sub>0..\*</sub>
     * Description: The ScoreDefinition that is applied in this Questionnaire.
     * Range: [ScoreDefinition](ScoreDefinition.md)
 * [questionnaireAuthoredByOrg](questionnaireAuthoredByOrg.md)  <sub>0..\*</sub>
     * Description: The Organization that has created this Questionnaire.
     * Range: [Organization](Organization.md)
 * [questionnairePartOfProcedure](questionnairePartOfProcedure.md)  <sub>0..\*</sub>
     * Description: Procedure this questionnaire is part of.
     * Range: [Procedure](Procedure.md)
 * [➞questionnaireId](questionnaire__questionnaireId.md)  <sub>1..1</sub>
     * Description: The unique identifier for the questionnaire.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞questionnaireLabel](questionnaire__questionnaireLabel.md)  <sub>1..1</sub>
     * Description: The label or title of the questionnaire, which is displayed to the user.
     * Range: [String](types/String.md)
 * [➞questionnaireStatus](questionnaire__questionnaireStatus.md)  <sub>1..1</sub>
     * Description: The status of the questionnaire, indicating whether it is draft, active, retired or unknown.
     * Range: [QuestionnaireStatus](QuestionnaireStatus.md)
 * [➞questionnaireVersion](questionnaire__questionnaireVersion.md)  <sub>1..1</sub>
     * Description: Version of the questionnaire.
     * Range: [String](types/String.md)
 * [➞questionnaireLastUpdated](questionnaire__questionnaireLastUpdated.md)  <sub>1..1</sub>
     * Description: The date and time when the questionnaire was last updated.
     * Range: [Datetime](types/Datetime.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:Questionnaire |
|  | | fhir:Questionnaire |
|  | | euVoc:QUESTIONNAIRE |