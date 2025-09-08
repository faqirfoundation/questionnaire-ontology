
# Class: Procedure

A clinical or administrative process that uses resources like questionnaires

URI: [datamodel:Procedure](https://w3id.org/faqir/datamodel/Procedure)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Questionnaire],[Questionnaire]<procedureHasQuestionnaire%200..*-%20[Procedure&#124;procedureId:uriorcurie;procedureLabel:string;procedureDescription:string%20%3F],[Organization]<procedurePerformedByOrg%200..*-%20[Procedure],[Questionnaire]-%20questionnairePartOfProcedure%200..*>[Procedure],[Organization])](https://yuml.me/diagram/nofunky;dir:TB/class/[Questionnaire],[Questionnaire]<procedureHasQuestionnaire%200..*-%20[Procedure&#124;procedureId:uriorcurie;procedureLabel:string;procedureDescription:string%20%3F],[Organization]<procedurePerformedByOrg%200..*-%20[Procedure],[Questionnaire]-%20questionnairePartOfProcedure%200..*>[Procedure],[Organization])

## Referenced by Class

 *  **[Organization](Organization.md)** *[organizationPerformsProcedure](organizationPerformsProcedure.md)*  <sub>0..\*</sub>  **[Procedure](Procedure.md)**
 *  **[Questionnaire](Questionnaire.md)** *[questionnairePartOfProcedure](questionnairePartOfProcedure.md)*  <sub>0..\*</sub>  **[Procedure](Procedure.md)**

## Attributes


### Own

 * [procedurePerformedByOrg](procedurePerformedByOrg.md)  <sub>0..\*</sub>
     * Description: Organization that manages and perfomes this procedure.
     * Range: [Organization](Organization.md)
 * [procedureHasQuestionnaire](procedureHasQuestionnaire.md)  <sub>0..\*</sub>
     * Description: Questionnaires part of this procedure.
     * Range: [Questionnaire](Questionnaire.md)
 * [➞procedureId](procedure__procedureId.md)  <sub>1..1</sub>
     * Description: unique identifier of the procedure.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞procedureLabel](procedure__procedureLabel.md)  <sub>1..1</sub>
     * Description: Name of the procedure.
     * Range: [String](types/String.md)
 * [➞procedureDescription](procedure__procedureDescription.md)  <sub>0..1</sub>
     * Description: Description of the procedure
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:Procedure |
|  | | fhir:Procedure |