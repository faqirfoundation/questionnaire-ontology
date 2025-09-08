-- # Class: "Vault" Description: "The FAQIR healthdata vault."
--     * Slot: vaultManagedByOrg Description: Organization managing this vault.
--     * Slot: vaultId Description: The unique identifier for a vault.
--     * Slot: birthdate Description: The date of birth.
--     * Slot: lastUpdated Description: The date and time when the entity was last updated.
--     * Slot: weight_id Description: The weight of the vault's user.
--     * Slot: full_name_id Description: The full name of the vault's user.
-- # Class: "FullName" Description: "Structured full name."
--     * Slot: id Description: 
--     * Slot: first_name Description: Given or first name.
--     * Slot: middle_name Description: Middle name.
--     * Slot: family_name Description: Family or last name.
-- # Class: "Weight" Description: "Weight."
--     * Slot: id Description: 
--     * Slot: weightType Description: The type of weight measurement, e.g. measured or stated.
--     * Slot: numericalValue Description: The quantitative value, which can be an integer or a float.
-- # Class: "ValueNumerical" Description: "Base class for quantitative values, they may have units and precision."
--     * Slot: id Description: 
--     * Slot: numericalValue Description: The quantitative value, which can be an integer or a float.
-- # Class: "NumericalParams" Description: "Parameters for quantitative values, including unit and precision."
--     * Slot: id Description: 
--     * Slot: numericalUnit Description: The unit of measure for the quantitative value, from UCUM standard.
--     * Slot: numericalPrecision Description: The precision of the quantitative value, e.g. number of decimal places.
-- # Class: "IntervalParams" Description: "Parameters for interval values, including minimum and maximum values."
--     * Slot: id Description: 
--     * Slot: minValue Description: The minimum value of the interval.
--     * Slot: minLabel Description: The label for the minimum value of the interval.
--     * Slot: maxValue Description: The maximum value of the interval.
--     * Slot: maxLabel Description: The label for the maximum value of the interval.
-- # Class: "ValueString" Description: "A string value, typically used for text or identifiers."
--     * Slot: id Description: 
--     * Slot: stringValue Description: The string value, which can be any text.
-- # Class: "ValueDateTime" Description: "A date and time value, typically in ISO 8601 format."
--     * Slot: id Description: 
--     * Slot: dateTimeValue Description: The date and time value in ISO 8601 format.
-- # Class: "ValueCoding" Description: "A coded value with a unique code for each display text, typically used for standardized questionnaires."
--     * Slot: id Description: 
--     * Slot: code Description: The code representing the value (e.g. code '1' for display 'Yes').
--     * Slot: display Description: The human-readable display text for the code (e.g. code '1' for display 'Yes').
-- # Class: "Metadata" Description: "Base class for metadata tracking (e.g. schema versioning & last updated)."
--     * Slot: id Description: 
--     * Slot: lastUpdated Description: The date and time when the entity was last updated.
-- # Class: "Organization" Description: "An entity acting in a healthcare context"
--     * Slot: organizationId Description: Unique identifier of the organization.
--     * Slot: organizationLabel Description: Name of the organization.
--     * Slot: organizationType Description: Type of organization.
-- # Class: "Procedure" Description: "A clinical or administrative process that uses resources like questionnaires"
--     * Slot: procedureId Description: unique identifier of the procedure.
--     * Slot: procedureLabel Description: Name of the procedure.
--     * Slot: procedureDescription Description: Description of the procedure
-- # Class: "QuestionnaireResponse" Description: "A response to a questionnaire (collection of answers)."
--     * Slot: questionnaireResponseBySubject Description: The subject that has authored this QuestionnaireResponse.
--     * Slot: questionnaireResponseToQuestionnaire Description: The Questionnaire that this QuestionnaireResponse is for.
--     * Slot: questionnaireResponseId Description: The unique identifier for a specific questionnaire response.
--     * Slot: questionnaireResponseStatus Description: The status of the questionnaire response, indicating whether it is 	'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.
--     * Slot: questionnaireResponseTimeStamp Description: The date and time when the questionnaire response was created (when the questionnaire starts to be answered, not when it's finished).
--     * Slot: questionnaireResponseLastUpdated Description: The date and time when the questionnaire response was last updated.
-- # Class: "Answer" Description: "Answer in the questionnaire response."
--     * Slot: answerInQuestionnaireResponse Description: The QuestionnaireResponse that this Answer is part of.
--     * Slot: answerToQuestion Description: The Question that this Answer is for.
--     * Slot: questionType Description: Type of the question (e.g., choice, openChoice, numberInterval, decimal, dateTime, text). Determines valid answers.
--     * Slot: answerId Description: The unique identifier for an answer in the questionnaire response.
--     * Slot: answerIsEmpty Description: True if the answer is intentionally empty.
--     * Slot: answerTimeStamp Description: The exact date and time when the answer was provided.
--     * Slot: answerValueNumerical_id Description: The value of the answer to a decimal or numberInterval type of question, which is a numeric value.
--     * Slot: answerValueDateTime_id Description: The value of the answer to a dateTime type of question, which is a datetime value.
-- # Class: "OrderedQuestion" Description: "Question's position within a specific questionnaire or section."
--     * Slot: orderedQuestionHasQuestion Description: Question indexed in this OrderedQuestion.
--     * Slot: orderedQuestionPartOfQuestionnaire Description: The Questionnaire that this Question is part of in the specified order.
--     * Slot: orderedQuestionPartOfSection Description: The Section that this Question is part of in the specified order.
--     * Slot: orderedQuestionId Description: The unique identifier for the ordered question.
--     * Slot: questionOrder Description: Question position in the questionnaire or section (1-based index).
--     * Slot: Questionnaire_questionnaireId Description: Autocreated FK slot
--     * Slot: Section_sectionId Description: Autocreated FK slot
-- # Class: "Question" Description: "A question in the questionnaire."
--     * Slot: questionType Description: Type of the question (e.g., choice, openChoice, numberInterval, decimal, dateTime, text). Determines valid answers.
--     * Slot: questionId Description: The unique identifier for a question in the questionnaire.
--     * Slot: questionTag Description: Internal English identifier, e.g., 'q_pain_level'.
--     * Slot: questionRequired Description: Indicates whether answering this question is mandatory (true) or it's optional (false).
--     * Slot: questionNumericalParams_id Description: Unit and Precision limiting the quantitative answer for the question.
--     * Slot: questionIntervalParams_id Description: Minimum and Maximum limiting the range the answer must be in for the question.
-- # Class: "QuestionRepresentation" Description: "The text representation of the question, in a specific language."
--     * Slot: questionRepresentationOfQuestion Description: The Question that this QuestionRepresentation describes.
--     * Slot: questionRepresentationId Description: The unique identifier for the question representation.
--     * Slot: questionRepresentationText Description: The text of the question as presented to the user.
--     * Slot: questionRepresentationLanguage Description: The language of the question text, represented as a BCP 47 language tag (e.g., 'en', 'fr', 'es').
--     * Slot: Question_questionId Description: Autocreated FK slot
-- # Class: "Questionnaire" Description: "A questionnaire that can be answered (collection of questions)."
--     * Slot: questionnaireId Description: The unique identifier for the questionnaire.
--     * Slot: questionnaireLabel Description: The label or title of the questionnaire, which is displayed to the user.
--     * Slot: questionnaireStatus Description: The status of the questionnaire, indicating whether it is draft, active, retired or unknown.
--     * Slot: questionnaireVersion Description: Version of the questionnaire.
--     * Slot: questionnaireLastUpdated Description: The date and time when the questionnaire was last updated.
-- # Class: "OrderedSection" Description: "Section's position within a specific questionnaire or section."
--     * Slot: orderedSectionHasSection Description: Section indexed in this OrderedSection.
--     * Slot: orderedSectionPartOfQuestionnaire Description: The Questionnaire that this Section is part of in the specified order.
--     * Slot: orderedSectionPartOfSection Description: The Section that this Section is part of in the specified order.
--     * Slot: orderedSectionId Description: The unique identifier for the ordered Section.
--     * Slot: sectionOrder Description: Section position in the questionnaire or section (1-based index).
--     * Slot: Questionnaire_questionnaireId Description: Autocreated FK slot
--     * Slot: Section_sectionId Description: Autocreated FK slot
-- # Class: "Section" Description: "A section of questions in the questionnaire."
--     * Slot: sectionId Description: The unique identifier for a section in the questionnaire.
--     * Slot: sectionLabel Description: The label or title of the section, which is displayed to the user.
-- # Class: "ScoreDefinition" Description: "A score calculated from questions."
--     * Slot: scoreDefinitionType Description: Type of score: numerical_continuous, numerical_integer, numerical_percentage, numerical_z_score, numerical_t_score or categorical. Determines valid score values.
--     * Slot: scoreDefinitionId Description: Unique identifier for the score definition.
--     * Slot: scoreDefinitionLabel Description: Label or title of the score definition.
--     * Slot: scoreDefinitionFormula Description: The formula used to calculate the score.
--     * Slot: scoreDefinitionInterpretationGuide Description: How to interpret the score values. English explanation.
--     * Slot: scoreDefinitionIntervalParams_id Description: Minimum and maximum values for numerical_percentage and numerical_z_score scores.
-- # Class: "ScoreParameter" Description: "Parameters for score definitions, such as min/max values, categories or constants needed."
--     * Slot: scoreParameterPartOfScoreDefinition Description: The ScoreDefinition(s) that this ScoreParameter is part of.
--     * Slot: scoreParameterId Description: Unique identifier for the score parameter.
--     * Slot: scoreParameterLabel Description: Label or title of the parameter. Standard English name.
--     * Slot: scoreParameterType Description: Type of parameter: numerical or dateTime.
--     * Slot: scoreParameterValueNumerical_id Description: Numerical value parameter (e.g., 0.785, 82).
--     * Slot: scoreParameterValueDateTime_id Description: DateTime value parameter formatted as YYYY-MM-DDThh:mm:ss+zz:zz.
-- # Class: "ScoreValue" Description: "The score value calculated from a QuestionnaireResponse following a ScoreDefinition."
--     * Slot: scoreDefinitionType Description: Type of score: numerical_continuous, numerical_integer, numerical_percentage, numerical_z_score, numerical_t_score or categorical. Determines valid score values.
--     * Slot: scoreValueBasedOnScoreDefinition Description: The ScoreDefinition that this ScoreValue is based on.
--     * Slot: scoreValueId Description: Unique identifier for the score value.
--     * Slot: scoreValueTimeStamp Description: Timestamp when the score value was calculated.
--     * Slot: scoreValueStatus Description: Status of the score value, e.g., draft, final.
--     * Slot: scoreValueString_id Description: String representation of the score value, used for categorical scores.
--     * Slot: scoreValueNumerical_id Description: Numerical value of the score, used for numerical scores.
-- # Class: "Vault_hasQuestionnaireResponse" Description: ""
--     * Slot: Vault_vaultId Description: Autocreated FK slot
--     * Slot: hasQuestionnaireResponse_questionnaireResponseId Description: QuestionnaireResponse authored by this vault's user.
-- # Class: "Organization_organizationAuthorsQuestionnaire" Description: ""
--     * Slot: Organization_organizationId Description: Autocreated FK slot
--     * Slot: organizationAuthorsQuestionnaire_questionnaireId Description: Questionnaire created by this organization.
-- # Class: "Organization_organizationAuthorsSection" Description: ""
--     * Slot: Organization_organizationId Description: Autocreated FK slot
--     * Slot: organizationAuthorsSection_sectionId Description: Section created by this organization.
-- # Class: "Organization_organizationAuthorsQuestion" Description: ""
--     * Slot: Organization_organizationId Description: Autocreated FK slot
--     * Slot: organizationAuthorsQuestion_questionId Description: Question created by this organization.
-- # Class: "Organization_organizationAuthorsScoreDefinition" Description: ""
--     * Slot: Organization_organizationId Description: Autocreated FK slot
--     * Slot: organizationAuthorsScoreDefinition_scoreDefinitionId Description: Score definition created by this organization.
-- # Class: "Organization_organizationManagesVault" Description: ""
--     * Slot: Organization_organizationId Description: Autocreated FK slot
--     * Slot: organizationManagesVault_vaultId Description: Vault managed by this organization.
-- # Class: "Procedure_procedurePerformedByOrg" Description: ""
--     * Slot: Procedure_procedureId Description: Autocreated FK slot
--     * Slot: procedurePerformedByOrg_organizationId Description: Organization that manages and perfomes this procedure.
-- # Class: "Procedure_procedureHasQuestionnaire" Description: ""
--     * Slot: Procedure_procedureId Description: Autocreated FK slot
--     * Slot: procedureHasQuestionnaire_questionnaireId Description: Questionnaires part of this procedure.
-- # Class: "QuestionnaireResponse_questionnaireResponseHasAnswer" Description: ""
--     * Slot: QuestionnaireResponse_questionnaireResponseId Description: Autocreated FK slot
--     * Slot: questionnaireResponseHasAnswer_answerId Description: The Answer that is part of this QuestionnaireResponse.
-- # Class: "QuestionnaireResponse_questionnaireResponseHasDerivedScoreValue" Description: ""
--     * Slot: QuestionnaireResponse_questionnaireResponseId Description: Autocreated FK slot
--     * Slot: questionnaireResponseHasDerivedScoreValue_scoreValueId Description: The ScoreValue that is calculated from this QuestionnaireResponse's answers.
-- # Class: "Answer_answerValueString" Description: ""
--     * Slot: Answer_answerId Description: Autocreated FK slot
--     * Slot: answerValueString_id Description: The value of the answer to a choice, openChoice or text type of question, which is a stringValue.
-- # Class: "Question_questionAuthoredByOrg" Description: ""
--     * Slot: Question_questionId Description: Autocreated FK slot
--     * Slot: questionAuthoredByOrg_organizationId Description: The organization that has designed this Question.
-- # Class: "Question_questionInOrderedQuestion" Description: ""
--     * Slot: Question_questionId Description: Autocreated FK slot
--     * Slot: questionInOrderedQuestion_orderedQuestionId Description: OrderedQuestions that this Question is indexed in.
-- # Class: "Question_questionHasAnswer" Description: ""
--     * Slot: Question_questionId Description: Autocreated FK slot
--     * Slot: questionHasAnswer_answerId Description: The Answer to this Question.
-- # Class: "Question_questionUsedInScoreDefinition" Description: ""
--     * Slot: Question_questionId Description: Autocreated FK slot
--     * Slot: questionUsedInScoreDefinition_scoreDefinitionId Description: The ScoreDefinition that this Question is used in.
-- # Class: "Question_questionCodingParams" Description: ""
--     * Slot: Question_questionId Description: Autocreated FK slot
--     * Slot: questionCodingParams_id Description: Code and Display of each option offered as answer to the choice or open-choice question.
-- # Class: "Questionnaire_questionnaireHasQuestionnaireResponse" Description: ""
--     * Slot: Questionnaire_questionnaireId Description: Autocreated FK slot
--     * Slot: questionnaireHasQuestionnaireResponse_questionnaireResponseId Description: The QuestionnaireResponse that is associated with this Questionnaire.
-- # Class: "Questionnaire_questionnaireAuthoredByOrg" Description: ""
--     * Slot: Questionnaire_questionnaireId Description: Autocreated FK slot
--     * Slot: questionnaireAuthoredByOrg_organizationId Description: The Organization that has created this Questionnaire.
-- # Class: "Questionnaire_questionnairePartOfProcedure" Description: ""
--     * Slot: Questionnaire_questionnaireId Description: Autocreated FK slot
--     * Slot: questionnairePartOfProcedure_procedureId Description: Procedure this questionnaire is part of.
-- # Class: "Section_sectionInOrderedSection" Description: ""
--     * Slot: Section_sectionId Description: Autocreated FK slot
--     * Slot: sectionInOrderedSection_orderedSectionId Description: OrderedSections that this Section is indexed in.
-- # Class: "Section_sectionAuthoredByOrg" Description: ""
--     * Slot: Section_sectionId Description: Autocreated FK slot
--     * Slot: sectionAuthoredByOrg_organizationId Description: The Organization that has created this Section.
-- # Class: "ScoreDefinition_scoreDefinitionHasScoreParameter" Description: ""
--     * Slot: ScoreDefinition_scoreDefinitionId Description: Autocreated FK slot
--     * Slot: scoreDefinitionHasScoreParameter_scoreParameterId Description: The ScoreParameter that is required for this ScoreDefinition.
-- # Class: "ScoreDefinition_scoreDefinitionUsesQuestion" Description: ""
--     * Slot: ScoreDefinition_scoreDefinitionId Description: Autocreated FK slot
--     * Slot: scoreDefinitionUsesQuestion_questionId Description: The Question(s) that this ScoreDefinition is based on.
-- # Class: "ScoreDefinition_scoreDefinitionHasScoreValue" Description: ""
--     * Slot: ScoreDefinition_scoreDefinitionId Description: Autocreated FK slot
--     * Slot: scoreDefinitionHasScoreValue_scoreValueId Description: The ScoreValue that is calculated following this ScoreDefinition.
-- # Class: "ScoreDefinition_scoreDefinitionAuthoredByOrg" Description: ""
--     * Slot: ScoreDefinition_scoreDefinitionId Description: Autocreated FK slot
--     * Slot: scoreDefinitionAuthoredByOrg_organizationId Description: The Organization that has created this ScoreDefinition.
-- # Class: "ScoreDefinition_scoreDefinitionCategories" Description: ""
--     * Slot: ScoreDefinition_scoreDefinitionId Description: Autocreated FK slot
--     * Slot: scoreDefinitionCategories Description: Categories for categorical scores.
-- # Class: "ScoreValue_scoreValueDerivedFromQuestionnaireResponse" Description: ""
--     * Slot: ScoreValue_scoreValueId Description: Autocreated FK slot
--     * Slot: scoreValueDerivedFromQuestionnaireResponse_questionnaireResponseId Description: The QuestionnaireResponse that contains the answers this ScoreValue is calculated from.

CREATE TABLE "FullName" (
	id INTEGER NOT NULL, 
	first_name TEXT, 
	middle_name TEXT, 
	family_name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Weight" (
	id INTEGER NOT NULL, 
	"weightType" VARCHAR(20) NOT NULL, 
	"numericalValue" INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ValueNumerical" (
	id INTEGER NOT NULL, 
	"numericalValue" INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "NumericalParams" (
	id INTEGER NOT NULL, 
	"numericalUnit" VARCHAR(3), 
	"numericalPrecision" INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "IntervalParams" (
	id INTEGER NOT NULL, 
	"minValue" FLOAT NOT NULL, 
	"minLabel" TEXT, 
	"maxValue" FLOAT NOT NULL, 
	"maxLabel" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ValueString" (
	id INTEGER NOT NULL, 
	"stringValue" TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ValueDateTime" (
	id INTEGER NOT NULL, 
	"dateTimeValue" DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE "ValueCoding" (
	id INTEGER NOT NULL, 
	code TEXT NOT NULL, 
	display TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Metadata" (
	id INTEGER NOT NULL, 
	"lastUpdated" DATETIME NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Organization" (
	"organizationId" TEXT NOT NULL, 
	"organizationLabel" TEXT NOT NULL, 
	"organizationType" VARCHAR(15) NOT NULL, 
	PRIMARY KEY ("organizationId")
);
CREATE TABLE "Procedure" (
	"procedureId" TEXT NOT NULL, 
	"procedureLabel" TEXT NOT NULL, 
	"procedureDescription" TEXT, 
	PRIMARY KEY ("procedureId")
);
CREATE TABLE "Questionnaire" (
	"questionnaireId" TEXT NOT NULL, 
	"questionnaireLabel" TEXT NOT NULL, 
	"questionnaireStatus" VARCHAR(7) NOT NULL, 
	"questionnaireVersion" TEXT NOT NULL, 
	"questionnaireLastUpdated" DATETIME NOT NULL, 
	PRIMARY KEY ("questionnaireId")
);
CREATE TABLE "Section" (
	"sectionId" TEXT NOT NULL, 
	"sectionLabel" TEXT NOT NULL, 
	PRIMARY KEY ("sectionId")
);
CREATE TABLE "Vault" (
	"vaultManagedByOrg" TEXT NOT NULL, 
	"vaultId" TEXT NOT NULL, 
	birthdate DATETIME, 
	"lastUpdated" DATETIME NOT NULL, 
	weight_id INTEGER, 
	full_name_id INTEGER, 
	PRIMARY KEY ("vaultId"), 
	FOREIGN KEY("vaultManagedByOrg") REFERENCES "Organization" ("organizationId"), 
	FOREIGN KEY(weight_id) REFERENCES "Weight" (id), 
	FOREIGN KEY(full_name_id) REFERENCES "FullName" (id)
);
CREATE TABLE "Question" (
	"questionType" VARCHAR(14) NOT NULL, 
	"questionId" TEXT NOT NULL, 
	"questionTag" TEXT NOT NULL, 
	"questionRequired" BOOLEAN, 
	"questionNumericalParams_id" INTEGER, 
	"questionIntervalParams_id" INTEGER, 
	PRIMARY KEY ("questionId"), 
	FOREIGN KEY("questionNumericalParams_id") REFERENCES "NumericalParams" (id), 
	FOREIGN KEY("questionIntervalParams_id") REFERENCES "IntervalParams" (id)
);
CREATE TABLE "OrderedSection" (
	"orderedSectionHasSection" TEXT NOT NULL, 
	"orderedSectionPartOfQuestionnaire" TEXT, 
	"orderedSectionPartOfSection" TEXT, 
	"orderedSectionId" TEXT NOT NULL, 
	"sectionOrder" INTEGER NOT NULL, 
	"Questionnaire_questionnaireId" TEXT, 
	"Section_sectionId" TEXT, 
	PRIMARY KEY ("orderedSectionId"), 
	UNIQUE ("sectionOrder", "orderedSectionPartOfQuestionnaire"), 
	UNIQUE ("sectionOrder", "orderedSectionPartOfSection"), 
	FOREIGN KEY("orderedSectionHasSection") REFERENCES "Section" ("sectionId"), 
	FOREIGN KEY("orderedSectionPartOfQuestionnaire") REFERENCES "Questionnaire" ("questionnaireId"), 
	FOREIGN KEY("orderedSectionPartOfSection") REFERENCES "Section" ("sectionId"), 
	FOREIGN KEY("Questionnaire_questionnaireId") REFERENCES "Questionnaire" ("questionnaireId"), 
	FOREIGN KEY("Section_sectionId") REFERENCES "Section" ("sectionId")
);
CREATE TABLE "ScoreDefinition" (
	"scoreDefinitionType" VARCHAR(20) NOT NULL, 
	"scoreDefinitionId" TEXT NOT NULL, 
	"scoreDefinitionLabel" TEXT NOT NULL, 
	"scoreDefinitionFormula" TEXT NOT NULL, 
	"scoreDefinitionInterpretationGuide" TEXT, 
	"scoreDefinitionIntervalParams_id" INTEGER, 
	PRIMARY KEY ("scoreDefinitionId"), 
	FOREIGN KEY("scoreDefinitionIntervalParams_id") REFERENCES "IntervalParams" (id)
);
CREATE TABLE "Organization_organizationAuthorsQuestionnaire" (
	"Organization_organizationId" TEXT, 
	"organizationAuthorsQuestionnaire_questionnaireId" TEXT, 
	PRIMARY KEY ("Organization_organizationId", "organizationAuthorsQuestionnaire_questionnaireId"), 
	FOREIGN KEY("Organization_organizationId") REFERENCES "Organization" ("organizationId"), 
	FOREIGN KEY("organizationAuthorsQuestionnaire_questionnaireId") REFERENCES "Questionnaire" ("questionnaireId")
);
CREATE TABLE "Organization_organizationAuthorsSection" (
	"Organization_organizationId" TEXT, 
	"organizationAuthorsSection_sectionId" TEXT, 
	PRIMARY KEY ("Organization_organizationId", "organizationAuthorsSection_sectionId"), 
	FOREIGN KEY("Organization_organizationId") REFERENCES "Organization" ("organizationId"), 
	FOREIGN KEY("organizationAuthorsSection_sectionId") REFERENCES "Section" ("sectionId")
);
CREATE TABLE "Procedure_procedurePerformedByOrg" (
	"Procedure_procedureId" TEXT, 
	"procedurePerformedByOrg_organizationId" TEXT, 
	PRIMARY KEY ("Procedure_procedureId", "procedurePerformedByOrg_organizationId"), 
	FOREIGN KEY("Procedure_procedureId") REFERENCES "Procedure" ("procedureId"), 
	FOREIGN KEY("procedurePerformedByOrg_organizationId") REFERENCES "Organization" ("organizationId")
);
CREATE TABLE "Procedure_procedureHasQuestionnaire" (
	"Procedure_procedureId" TEXT, 
	"procedureHasQuestionnaire_questionnaireId" TEXT, 
	PRIMARY KEY ("Procedure_procedureId", "procedureHasQuestionnaire_questionnaireId"), 
	FOREIGN KEY("Procedure_procedureId") REFERENCES "Procedure" ("procedureId"), 
	FOREIGN KEY("procedureHasQuestionnaire_questionnaireId") REFERENCES "Questionnaire" ("questionnaireId")
);
CREATE TABLE "Questionnaire_questionnaireAuthoredByOrg" (
	"Questionnaire_questionnaireId" TEXT, 
	"questionnaireAuthoredByOrg_organizationId" TEXT, 
	PRIMARY KEY ("Questionnaire_questionnaireId", "questionnaireAuthoredByOrg_organizationId"), 
	FOREIGN KEY("Questionnaire_questionnaireId") REFERENCES "Questionnaire" ("questionnaireId"), 
	FOREIGN KEY("questionnaireAuthoredByOrg_organizationId") REFERENCES "Organization" ("organizationId")
);
CREATE TABLE "Questionnaire_questionnairePartOfProcedure" (
	"Questionnaire_questionnaireId" TEXT, 
	"questionnairePartOfProcedure_procedureId" TEXT, 
	PRIMARY KEY ("Questionnaire_questionnaireId", "questionnairePartOfProcedure_procedureId"), 
	FOREIGN KEY("Questionnaire_questionnaireId") REFERENCES "Questionnaire" ("questionnaireId"), 
	FOREIGN KEY("questionnairePartOfProcedure_procedureId") REFERENCES "Procedure" ("procedureId")
);
CREATE TABLE "Section_sectionAuthoredByOrg" (
	"Section_sectionId" TEXT, 
	"sectionAuthoredByOrg_organizationId" TEXT, 
	PRIMARY KEY ("Section_sectionId", "sectionAuthoredByOrg_organizationId"), 
	FOREIGN KEY("Section_sectionId") REFERENCES "Section" ("sectionId"), 
	FOREIGN KEY("sectionAuthoredByOrg_organizationId") REFERENCES "Organization" ("organizationId")
);
CREATE TABLE "QuestionnaireResponse" (
	"questionnaireResponseBySubject" TEXT NOT NULL, 
	"questionnaireResponseToQuestionnaire" TEXT NOT NULL, 
	"questionnaireResponseId" TEXT NOT NULL, 
	"questionnaireResponseStatus" VARCHAR(16) NOT NULL, 
	"questionnaireResponseTimeStamp" DATETIME NOT NULL, 
	"questionnaireResponseLastUpdated" DATETIME NOT NULL, 
	PRIMARY KEY ("questionnaireResponseId"), 
	FOREIGN KEY("questionnaireResponseBySubject") REFERENCES "Vault" ("vaultId"), 
	FOREIGN KEY("questionnaireResponseToQuestionnaire") REFERENCES "Questionnaire" ("questionnaireId")
);
CREATE TABLE "OrderedQuestion" (
	"orderedQuestionHasQuestion" TEXT NOT NULL, 
	"orderedQuestionPartOfQuestionnaire" TEXT, 
	"orderedQuestionPartOfSection" TEXT, 
	"orderedQuestionId" TEXT NOT NULL, 
	"questionOrder" INTEGER NOT NULL, 
	"Questionnaire_questionnaireId" TEXT, 
	"Section_sectionId" TEXT, 
	PRIMARY KEY ("orderedQuestionId"), 
	UNIQUE ("questionOrder", "orderedQuestionPartOfQuestionnaire"), 
	UNIQUE ("questionOrder", "orderedQuestionPartOfSection"), 
	FOREIGN KEY("orderedQuestionHasQuestion") REFERENCES "Question" ("questionId"), 
	FOREIGN KEY("orderedQuestionPartOfQuestionnaire") REFERENCES "Questionnaire" ("questionnaireId"), 
	FOREIGN KEY("orderedQuestionPartOfSection") REFERENCES "Section" ("sectionId"), 
	FOREIGN KEY("Questionnaire_questionnaireId") REFERENCES "Questionnaire" ("questionnaireId"), 
	FOREIGN KEY("Section_sectionId") REFERENCES "Section" ("sectionId")
);
CREATE TABLE "QuestionRepresentation" (
	"questionRepresentationOfQuestion" TEXT NOT NULL, 
	"questionRepresentationId" TEXT NOT NULL, 
	"questionRepresentationText" TEXT NOT NULL, 
	"questionRepresentationLanguage" TEXT NOT NULL, 
	"Question_questionId" TEXT, 
	PRIMARY KEY ("questionRepresentationId"), 
	FOREIGN KEY("questionRepresentationOfQuestion") REFERENCES "Question" ("questionId"), 
	FOREIGN KEY("Question_questionId") REFERENCES "Question" ("questionId")
);
CREATE TABLE "ScoreParameter" (
	"scoreParameterPartOfScoreDefinition" TEXT NOT NULL, 
	"scoreParameterId" TEXT NOT NULL, 
	"scoreParameterLabel" TEXT NOT NULL, 
	"scoreParameterType" VARCHAR(9) NOT NULL, 
	"scoreParameterValueNumerical_id" INTEGER, 
	"scoreParameterValueDateTime_id" INTEGER, 
	PRIMARY KEY ("scoreParameterId"), 
	FOREIGN KEY("scoreParameterPartOfScoreDefinition") REFERENCES "ScoreDefinition" ("scoreDefinitionId"), 
	FOREIGN KEY("scoreParameterValueNumerical_id") REFERENCES "ValueNumerical" (id), 
	FOREIGN KEY("scoreParameterValueDateTime_id") REFERENCES "ValueDateTime" (id)
);
CREATE TABLE "ScoreValue" (
	"scoreDefinitionType" VARCHAR(20) NOT NULL, 
	"scoreValueBasedOnScoreDefinition" TEXT NOT NULL, 
	"scoreValueId" TEXT NOT NULL, 
	"scoreValueTimeStamp" DATETIME NOT NULL, 
	"scoreValueStatus" VARCHAR(10) NOT NULL, 
	"scoreValueString_id" INTEGER, 
	"scoreValueNumerical_id" INTEGER, 
	PRIMARY KEY ("scoreValueId"), 
	FOREIGN KEY("scoreValueBasedOnScoreDefinition") REFERENCES "ScoreDefinition" ("scoreDefinitionId"), 
	FOREIGN KEY("scoreValueString_id") REFERENCES "ValueString" (id), 
	FOREIGN KEY("scoreValueNumerical_id") REFERENCES "ValueNumerical" (id)
);
CREATE TABLE "Organization_organizationAuthorsQuestion" (
	"Organization_organizationId" TEXT, 
	"organizationAuthorsQuestion_questionId" TEXT, 
	PRIMARY KEY ("Organization_organizationId", "organizationAuthorsQuestion_questionId"), 
	FOREIGN KEY("Organization_organizationId") REFERENCES "Organization" ("organizationId"), 
	FOREIGN KEY("organizationAuthorsQuestion_questionId") REFERENCES "Question" ("questionId")
);
CREATE TABLE "Organization_organizationAuthorsScoreDefinition" (
	"Organization_organizationId" TEXT, 
	"organizationAuthorsScoreDefinition_scoreDefinitionId" TEXT, 
	PRIMARY KEY ("Organization_organizationId", "organizationAuthorsScoreDefinition_scoreDefinitionId"), 
	FOREIGN KEY("Organization_organizationId") REFERENCES "Organization" ("organizationId"), 
	FOREIGN KEY("organizationAuthorsScoreDefinition_scoreDefinitionId") REFERENCES "ScoreDefinition" ("scoreDefinitionId")
);
CREATE TABLE "Organization_organizationManagesVault" (
	"Organization_organizationId" TEXT, 
	"organizationManagesVault_vaultId" TEXT, 
	PRIMARY KEY ("Organization_organizationId", "organizationManagesVault_vaultId"), 
	FOREIGN KEY("Organization_organizationId") REFERENCES "Organization" ("organizationId"), 
	FOREIGN KEY("organizationManagesVault_vaultId") REFERENCES "Vault" ("vaultId")
);
CREATE TABLE "Question_questionAuthoredByOrg" (
	"Question_questionId" TEXT, 
	"questionAuthoredByOrg_organizationId" TEXT, 
	PRIMARY KEY ("Question_questionId", "questionAuthoredByOrg_organizationId"), 
	FOREIGN KEY("Question_questionId") REFERENCES "Question" ("questionId"), 
	FOREIGN KEY("questionAuthoredByOrg_organizationId") REFERENCES "Organization" ("organizationId")
);
CREATE TABLE "Question_questionUsedInScoreDefinition" (
	"Question_questionId" TEXT, 
	"questionUsedInScoreDefinition_scoreDefinitionId" TEXT, 
	PRIMARY KEY ("Question_questionId", "questionUsedInScoreDefinition_scoreDefinitionId"), 
	FOREIGN KEY("Question_questionId") REFERENCES "Question" ("questionId"), 
	FOREIGN KEY("questionUsedInScoreDefinition_scoreDefinitionId") REFERENCES "ScoreDefinition" ("scoreDefinitionId")
);
CREATE TABLE "Question_questionCodingParams" (
	"Question_questionId" TEXT, 
	"questionCodingParams_id" INTEGER, 
	PRIMARY KEY ("Question_questionId", "questionCodingParams_id"), 
	FOREIGN KEY("Question_questionId") REFERENCES "Question" ("questionId"), 
	FOREIGN KEY("questionCodingParams_id") REFERENCES "ValueCoding" (id)
);
CREATE TABLE "Section_sectionInOrderedSection" (
	"Section_sectionId" TEXT, 
	"sectionInOrderedSection_orderedSectionId" TEXT, 
	PRIMARY KEY ("Section_sectionId", "sectionInOrderedSection_orderedSectionId"), 
	FOREIGN KEY("Section_sectionId") REFERENCES "Section" ("sectionId"), 
	FOREIGN KEY("sectionInOrderedSection_orderedSectionId") REFERENCES "OrderedSection" ("orderedSectionId")
);
CREATE TABLE "ScoreDefinition_scoreDefinitionUsesQuestion" (
	"ScoreDefinition_scoreDefinitionId" TEXT, 
	"scoreDefinitionUsesQuestion_questionId" TEXT NOT NULL, 
	PRIMARY KEY ("ScoreDefinition_scoreDefinitionId", "scoreDefinitionUsesQuestion_questionId"), 
	FOREIGN KEY("ScoreDefinition_scoreDefinitionId") REFERENCES "ScoreDefinition" ("scoreDefinitionId"), 
	FOREIGN KEY("scoreDefinitionUsesQuestion_questionId") REFERENCES "Question" ("questionId")
);
CREATE TABLE "ScoreDefinition_scoreDefinitionAuthoredByOrg" (
	"ScoreDefinition_scoreDefinitionId" TEXT, 
	"scoreDefinitionAuthoredByOrg_organizationId" TEXT, 
	PRIMARY KEY ("ScoreDefinition_scoreDefinitionId", "scoreDefinitionAuthoredByOrg_organizationId"), 
	FOREIGN KEY("ScoreDefinition_scoreDefinitionId") REFERENCES "ScoreDefinition" ("scoreDefinitionId"), 
	FOREIGN KEY("scoreDefinitionAuthoredByOrg_organizationId") REFERENCES "Organization" ("organizationId")
);
CREATE TABLE "ScoreDefinition_scoreDefinitionCategories" (
	"ScoreDefinition_scoreDefinitionId" TEXT, 
	"scoreDefinitionCategories" TEXT, 
	PRIMARY KEY ("ScoreDefinition_scoreDefinitionId", "scoreDefinitionCategories"), 
	FOREIGN KEY("ScoreDefinition_scoreDefinitionId") REFERENCES "ScoreDefinition" ("scoreDefinitionId")
);
CREATE TABLE "Answer" (
	"answerInQuestionnaireResponse" TEXT NOT NULL, 
	"answerToQuestion" TEXT NOT NULL, 
	"questionType" VARCHAR(14) NOT NULL, 
	"answerId" TEXT NOT NULL, 
	"answerIsEmpty" BOOLEAN, 
	"answerTimeStamp" DATETIME NOT NULL, 
	"answerValueNumerical_id" INTEGER, 
	"answerValueDateTime_id" INTEGER, 
	PRIMARY KEY ("answerId"), 
	FOREIGN KEY("answerInQuestionnaireResponse") REFERENCES "QuestionnaireResponse" ("questionnaireResponseId"), 
	FOREIGN KEY("answerToQuestion") REFERENCES "Question" ("questionId"), 
	FOREIGN KEY("answerValueNumerical_id") REFERENCES "ValueNumerical" (id), 
	FOREIGN KEY("answerValueDateTime_id") REFERENCES "ValueDateTime" (id)
);
CREATE TABLE "Vault_hasQuestionnaireResponse" (
	"Vault_vaultId" TEXT, 
	"hasQuestionnaireResponse_questionnaireResponseId" TEXT, 
	PRIMARY KEY ("Vault_vaultId", "hasQuestionnaireResponse_questionnaireResponseId"), 
	FOREIGN KEY("Vault_vaultId") REFERENCES "Vault" ("vaultId"), 
	FOREIGN KEY("hasQuestionnaireResponse_questionnaireResponseId") REFERENCES "QuestionnaireResponse" ("questionnaireResponseId")
);
CREATE TABLE "QuestionnaireResponse_questionnaireResponseHasDerivedScoreValue" (
	"QuestionnaireResponse_questionnaireResponseId" TEXT, 
	"questionnaireResponseHasDerivedScoreValue_scoreValueId" TEXT, 
	PRIMARY KEY ("QuestionnaireResponse_questionnaireResponseId", "questionnaireResponseHasDerivedScoreValue_scoreValueId"), 
	FOREIGN KEY("QuestionnaireResponse_questionnaireResponseId") REFERENCES "QuestionnaireResponse" ("questionnaireResponseId"), 
	FOREIGN KEY("questionnaireResponseHasDerivedScoreValue_scoreValueId") REFERENCES "ScoreValue" ("scoreValueId")
);
CREATE TABLE "Question_questionInOrderedQuestion" (
	"Question_questionId" TEXT, 
	"questionInOrderedQuestion_orderedQuestionId" TEXT, 
	PRIMARY KEY ("Question_questionId", "questionInOrderedQuestion_orderedQuestionId"), 
	FOREIGN KEY("Question_questionId") REFERENCES "Question" ("questionId"), 
	FOREIGN KEY("questionInOrderedQuestion_orderedQuestionId") REFERENCES "OrderedQuestion" ("orderedQuestionId")
);
CREATE TABLE "Questionnaire_questionnaireHasQuestionnaireResponse" (
	"Questionnaire_questionnaireId" TEXT, 
	"questionnaireHasQuestionnaireResponse_questionnaireResponseId" TEXT, 
	PRIMARY KEY ("Questionnaire_questionnaireId", "questionnaireHasQuestionnaireResponse_questionnaireResponseId"), 
	FOREIGN KEY("Questionnaire_questionnaireId") REFERENCES "Questionnaire" ("questionnaireId"), 
	FOREIGN KEY("questionnaireHasQuestionnaireResponse_questionnaireResponseId") REFERENCES "QuestionnaireResponse" ("questionnaireResponseId")
);
CREATE TABLE "ScoreDefinition_scoreDefinitionHasScoreParameter" (
	"ScoreDefinition_scoreDefinitionId" TEXT, 
	"scoreDefinitionHasScoreParameter_scoreParameterId" TEXT, 
	PRIMARY KEY ("ScoreDefinition_scoreDefinitionId", "scoreDefinitionHasScoreParameter_scoreParameterId"), 
	FOREIGN KEY("ScoreDefinition_scoreDefinitionId") REFERENCES "ScoreDefinition" ("scoreDefinitionId"), 
	FOREIGN KEY("scoreDefinitionHasScoreParameter_scoreParameterId") REFERENCES "ScoreParameter" ("scoreParameterId")
);
CREATE TABLE "ScoreDefinition_scoreDefinitionHasScoreValue" (
	"ScoreDefinition_scoreDefinitionId" TEXT, 
	"scoreDefinitionHasScoreValue_scoreValueId" TEXT, 
	PRIMARY KEY ("ScoreDefinition_scoreDefinitionId", "scoreDefinitionHasScoreValue_scoreValueId"), 
	FOREIGN KEY("ScoreDefinition_scoreDefinitionId") REFERENCES "ScoreDefinition" ("scoreDefinitionId"), 
	FOREIGN KEY("scoreDefinitionHasScoreValue_scoreValueId") REFERENCES "ScoreValue" ("scoreValueId")
);
CREATE TABLE "ScoreValue_scoreValueDerivedFromQuestionnaireResponse" (
	"ScoreValue_scoreValueId" TEXT, 
	"scoreValueDerivedFromQuestionnaireResponse_questionnaireResponseId" TEXT NOT NULL, 
	PRIMARY KEY ("ScoreValue_scoreValueId", "scoreValueDerivedFromQuestionnaireResponse_questionnaireResponseId"), 
	FOREIGN KEY("ScoreValue_scoreValueId") REFERENCES "ScoreValue" ("scoreValueId"), 
	FOREIGN KEY("scoreValueDerivedFromQuestionnaireResponse_questionnaireResponseId") REFERENCES "QuestionnaireResponse" ("questionnaireResponseId")
);
CREATE TABLE "QuestionnaireResponse_questionnaireResponseHasAnswer" (
	"QuestionnaireResponse_questionnaireResponseId" TEXT, 
	"questionnaireResponseHasAnswer_answerId" TEXT NOT NULL, 
	PRIMARY KEY ("QuestionnaireResponse_questionnaireResponseId", "questionnaireResponseHasAnswer_answerId"), 
	FOREIGN KEY("QuestionnaireResponse_questionnaireResponseId") REFERENCES "QuestionnaireResponse" ("questionnaireResponseId"), 
	FOREIGN KEY("questionnaireResponseHasAnswer_answerId") REFERENCES "Answer" ("answerId")
);
CREATE TABLE "Answer_answerValueString" (
	"Answer_answerId" TEXT, 
	"answerValueString_id" INTEGER, 
	PRIMARY KEY ("Answer_answerId", "answerValueString_id"), 
	FOREIGN KEY("Answer_answerId") REFERENCES "Answer" ("answerId"), 
	FOREIGN KEY("answerValueString_id") REFERENCES "ValueString" (id)
);
CREATE TABLE "Question_questionHasAnswer" (
	"Question_questionId" TEXT, 
	"questionHasAnswer_answerId" TEXT, 
	PRIMARY KEY ("Question_questionId", "questionHasAnswer_answerId"), 
	FOREIGN KEY("Question_questionId") REFERENCES "Question" ("questionId"), 
	FOREIGN KEY("questionHasAnswer_answerId") REFERENCES "Answer" ("answerId")
);