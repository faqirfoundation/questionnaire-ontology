
# Class: qo_Questionnaire

A questionnaire that can be answered (collection of questions).

URI: [qo:QoQuestionnaire](https://ns.faqir.org/q-o#QoQuestionnaire)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[SarefPropertyValue],[SarefProperty],[QoQuestionnaireStatus],[QoQuestionnaireResponse],[QoQuestionnaireStatus]<fhir_status%201..*-++[QoQuestionnaire&#124;dcterms_created:datetime;dcterms_modified:datetime;prov_type(i):uriorcurie%20*;prov_generatedAtTime(i):datetime%20*;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B],[SuloProcess]<dcterms_isPartOf%200..*-++[QoQuestionnaire],[ProvOrganization]<dcterms_creator%201..*-++[QoQuestionnaire],[QoOrderedSection]<qo_hasOrderedSection%200..*-++[QoQuestionnaire],[QoOrderedQuestion]<qo_hasOrderedQuestion%200..*-++[QoQuestionnaire],[QoQuestionnaireResponse]++-%20qo_responds%201..1>[QoQuestionnaire],[ProvEntity]^-[QoQuestionnaire],[QoOrderedSection],[QoOrderedQuestion],[ProvOrganization],[ProvEntity],[OwlThing],[FoafAgent])](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[SarefPropertyValue],[SarefProperty],[QoQuestionnaireStatus],[QoQuestionnaireResponse],[QoQuestionnaireStatus]<fhir_status%201..*-++[QoQuestionnaire&#124;dcterms_created:datetime;dcterms_modified:datetime;prov_type(i):uriorcurie%20*;prov_generatedAtTime(i):datetime%20*;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B],[SuloProcess]<dcterms_isPartOf%200..*-++[QoQuestionnaire],[ProvOrganization]<dcterms_creator%201..*-++[QoQuestionnaire],[QoOrderedSection]<qo_hasOrderedSection%200..*-++[QoQuestionnaire],[QoOrderedQuestion]<qo_hasOrderedQuestion%200..*-++[QoQuestionnaire],[QoQuestionnaireResponse]++-%20qo_responds%201..1>[QoQuestionnaire],[ProvEntity]^-[QoQuestionnaire],[QoOrderedSection],[QoOrderedQuestion],[ProvOrganization],[ProvEntity],[OwlThing],[FoafAgent])

## Parents

 *  is_a: [ProvEntity](ProvEntity.md) - An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.

## Referenced by Class

 *  **[QoQuestionnaireResponse](QoQuestionnaireResponse.md)** *[qo_responds](qo_responds.md)*  <sub>1..1</sub>  **[QoQuestionnaire](QoQuestionnaire.md)**

## Attributes


### Own

 * [qo_Questionnaire➞qo_hasOrderedQuestion](qo_Questionnaire_qo_hasOrderedQuestion.md)  <sub>0..\*</sub>
     * Description: The Question that is part of this Questionnaire or Section, with their display order.
     * Range: [QoOrderedQuestion](QoOrderedQuestion.md)
 * [qo_Questionnaire➞qo_hasOrderedSection](qo_Questionnaire_qo_hasOrderedSection.md)  <sub>0..\*</sub>
     * Description: The Section that is part of this Questionnaire or Section, with their display order.
     * Range: [QoOrderedSection](QoOrderedSection.md)
 * [qo_Questionnaire➞dcterms_created](qo_Questionnaire_dcterms_created.md)  <sub>1..1</sub>
     * Description: The date and time when the questionnaire was created.
     * Range: [Datetime](types/Datetime.md)
 * [qo_Questionnaire➞dcterms_modified](qo_Questionnaire_dcterms_modified.md)  <sub>1..1</sub>
     * Description: The date and time when the questionnaire was last updated.
     * Range: [Datetime](types/Datetime.md)
 * [qo_Questionnaire➞dcterms_creator](qo_Questionnaire_dcterms_creator.md)  <sub>1..\*</sub>
     * Description: The Organization that has created this Questionnaire.
     * Range: [ProvOrganization](ProvOrganization.md)
 * [qo_Questionnaire➞dcterms_isPartOf](qo_Questionnaire_dcterms_isPartOf.md)  <sub>0..\*</sub>
     * Description: Process this questionnaire is part of.
     * Range: [SuloProcess](SuloProcess.md)
 * [qo_Questionnaire➞fhir_status](qo_Questionnaire_fhir_status.md)  <sub>1..\*</sub>
     * Description: A code specifying the state of the observation/procedure/questionnaire... Generally, this will be the in-progress or completed state.
     * Range: [QoQuestionnaireStatus](QoQuestionnaireStatus.md)

### Inherited from prov_Entity:

 * [owl_versionInfo](owl_versionInfo.md)  <sub>0..1</sub>
     * Description: An owl:versionInfo statement generally has as its object a string giving information about this version, for example RCS/CVS keywords. This statement does not contribute to the logical meaning of the ontology other than that given by the RDF(S) model theory.
     * Range: [String](types/String.md)
 * [rdfs_label](rdfs_label.md)  <sub>1..\*</sub>
     * Description: human-readable version of a resource's name. Multilingual labels are supported using the language tagging facility of RDF literals.
     * Range: [String](types/String.md)
 * [rdfs_comment](rdfs_comment.md)  <sub>1..\*</sub>
     * Description: A textual comment helps clarify the meaning of RDF classes and properties. Such in-line documentation complements the use of both formal techniques (Ontology and rule languages) and informal (prose documentation, examples, test cases). A variety of documentation forms can be combined to indicate the intended meaning of the classes and properties described in an RDF vocabulary. Since RDF vocabularies are expressed as RDF graphs, vocabularies defined in other namespaces may be used to provide richer documentation.
     * Range: [String](types/String.md)
 * [prov_hadPrimarySource](prov_hadPrimarySource.md)  <sub>0..\*</sub>
     * Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
     * Range: [ProvEntity](ProvEntity.md)
 * [prov_wasGeneratedBy](prov_wasGeneratedBy.md)  <sub>0..\*</sub>
     * Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
     * Range: [SuloProcess](SuloProcess.md)
 * [prov_wasAttributedTo](prov_wasAttributedTo.md)  <sub>0..\*</sub>
     * Description: Attribution is the ascribing of an entity to an agent.
     * Range: [FoafAgent](FoafAgent.md)
 * [prov_type](prov_type.md)  <sub>0..\*</sub>
     * Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [dcterms_hasPart](dcterms_hasPart.md)  <sub>0..\*</sub>
     * Description: A related resource that is included either physically or logically in the described resource.
     * Range: [OwlThing](OwlThing.md)
 * [prov_generatedAtTime](prov_generatedAtTime.md)  <sub>0..\*</sub>
     * Description: The time at which an entity was completely created and is available for use.
     * Range: [Datetime](types/Datetime.md)
 * [saref_hasProperty](saref_hasProperty.md)  <sub>0..\*</sub>
     * Description: Links a feature kind or a feature of interest to one of its properties.
     * Range: [SarefProperty](SarefProperty.md)
 * [saref_hasPropertyValue](saref_hasPropertyValue.md)  <sub>0..\*</sub>
     * Description: Links a feature kind, a feature of interest, or a property of interest, to a property value.
     * Range: [SarefPropertyValue](SarefPropertyValue.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | qo:Questionnaire |
| **Narrow Mappings:** | | fhir:Questionnaire |