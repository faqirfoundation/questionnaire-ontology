
# Class: Organization

An entity acting in a healthcare context

URI: [datamodel:Organization](https://w3id.org/faqir/datamodel/Organization)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vault],[Section],[ScoreDefinition],[Questionnaire],[Question],[Procedure],[Vault]<organizationManagesVault%200..*-%20[Organization&#124;organizationId:uriorcurie;organizationLabel:string;organizationType:OrganizationType],[ScoreDefinition]<organizationAuthorsScoreDefinition%200..*-%20[Organization],[Question]<organizationAuthorsQuestion%200..*-%20[Organization],[Section]<organizationAuthorsSection%200..*-%20[Organization],[Questionnaire]<organizationAuthorsQuestionnaire%200..*-%20[Organization],[Procedure]-%20procedurePerformedByOrg%200..*>[Organization],[Question]-%20questionAuthoredByOrg%200..*>[Organization],[Questionnaire]-%20questionnaireAuthoredByOrg%200..*>[Organization],[ScoreDefinition]-%20scoreDefinitionAuthoredByOrg%200..*>[Organization],[Section]-%20sectionAuthoredByOrg%200..*>[Organization],[Vault]-%20vaultManagedByOrg%201..1>[Organization])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vault],[Section],[ScoreDefinition],[Questionnaire],[Question],[Procedure],[Vault]<organizationManagesVault%200..*-%20[Organization&#124;organizationId:uriorcurie;organizationLabel:string;organizationType:OrganizationType],[ScoreDefinition]<organizationAuthorsScoreDefinition%200..*-%20[Organization],[Question]<organizationAuthorsQuestion%200..*-%20[Organization],[Section]<organizationAuthorsSection%200..*-%20[Organization],[Questionnaire]<organizationAuthorsQuestionnaire%200..*-%20[Organization],[Procedure]-%20procedurePerformedByOrg%200..*>[Organization],[Question]-%20questionAuthoredByOrg%200..*>[Organization],[Questionnaire]-%20questionnaireAuthoredByOrg%200..*>[Organization],[ScoreDefinition]-%20scoreDefinitionAuthoredByOrg%200..*>[Organization],[Section]-%20sectionAuthoredByOrg%200..*>[Organization],[Vault]-%20vaultManagedByOrg%201..1>[Organization])

## Referenced by Class

 *  **[Procedure](Procedure.md)** *[procedurePerformedByOrg](procedurePerformedByOrg.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**
 *  **[Question](Question.md)** *[questionAuthoredByOrg](questionAuthoredByOrg.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**
 *  **[Questionnaire](Questionnaire.md)** *[questionnaireAuthoredByOrg](questionnaireAuthoredByOrg.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**
 *  **[ScoreDefinition](ScoreDefinition.md)** *[scoreDefinitionAuthoredByOrg](scoreDefinitionAuthoredByOrg.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**
 *  **[Section](Section.md)** *[sectionAuthoredByOrg](sectionAuthoredByOrg.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**
 *  **[Vault](Vault.md)** *[vaultManagedByOrg](vaultManagedByOrg.md)*  <sub>1..1</sub>  **[Organization](Organization.md)**

## Attributes


### Own

 * [organizationAuthorsQuestionnaire](organizationAuthorsQuestionnaire.md)  <sub>0..\*</sub>
     * Description: Questionnaire created by this organization.
     * Range: [Questionnaire](Questionnaire.md)
 * [organizationAuthorsSection](organizationAuthorsSection.md)  <sub>0..\*</sub>
     * Description: Section created by this organization.
     * Range: [Section](Section.md)
 * [organizationAuthorsQuestion](organizationAuthorsQuestion.md)  <sub>0..\*</sub>
     * Description: Question created by this organization.
     * Range: [Question](Question.md)
 * [organizationAuthorsScoreDefinition](organizationAuthorsScoreDefinition.md)  <sub>0..\*</sub>
     * Description: Score definition created by this organization.
     * Range: [ScoreDefinition](ScoreDefinition.md)
 * [organizationManagesVault](organizationManagesVault.md)  <sub>0..\*</sub>
     * Description: Vault managed by this organization.
     * Range: [Vault](Vault.md)
 * [➞organizationId](organization__organizationId.md)  <sub>1..1</sub>
     * Description: Unique identifier of the organization.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞organizationLabel](organization__organizationLabel.md)  <sub>1..1</sub>
     * Description: Name of the organization.
     * Range: [String](types/String.md)
 * [➞organizationType](organization__organizationType.md)  <sub>1..1</sub>
     * Description: Type of organization.
     * Range: [OrganizationType](OrganizationType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:Organization |
|  | | fhir:Organization |