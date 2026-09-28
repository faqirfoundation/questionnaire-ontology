
# Class: prov_Entity

An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.

URI: [qo:ProvEntity](https://ns.faqir.org/q-o#ProvEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[SarefPropertyValue],[SarefProperty],[QoSection],[QoQuestionnaireResponse],[QoQuestionnaire],[QoQuestion],[QoOrderedSection],[QoOrderedQuestion],[QoAnswer],[SarefPropertyValue]<saref_hasPropertyValue%200..*-++[ProvEntity&#124;dcterms_created:datetime%20%3F;dcterms_modified:datetime%20%3F;prov_type:uriorcurie%20*;prov_generatedAtTime:datetime%20*;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B],[SarefProperty]<saref_hasProperty%200..*-++[ProvEntity],[FoafAgent]<dcterms_creator%200..*-++[ProvEntity],[SarefPropertyValue]<fhir_status%200..*-++[ProvEntity],[OwlThing]<dcterms_isPartOf%200..*-++[ProvEntity],[OwlThing]<dcterms_hasPart%200..*-++[ProvEntity],[FoafAgent]<prov_wasAttributedTo%200..*-++[ProvEntity],[OwlThing]++-%20prov_hadPrimarySource%200..*>[ProvEntity],[ProvEntity]^-[SarefPropertyValue],[ProvEntity]^-[SarefProperty],[ProvEntity]^-[QoSection],[ProvEntity]^-[QoQuestionnaireResponse],[ProvEntity]^-[QoQuestionnaire],[ProvEntity]^-[QoQuestion],[ProvEntity]^-[QoOrderedSection],[ProvEntity]^-[QoOrderedQuestion],[ProvEntity]^-[QoAnswer],[OwlThing]^-[ProvEntity],[OwlThing],[FoafAgent])](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[SarefPropertyValue],[SarefProperty],[QoSection],[QoQuestionnaireResponse],[QoQuestionnaire],[QoQuestion],[QoOrderedSection],[QoOrderedQuestion],[QoAnswer],[SarefPropertyValue]<saref_hasPropertyValue%200..*-++[ProvEntity&#124;dcterms_created:datetime%20%3F;dcterms_modified:datetime%20%3F;prov_type:uriorcurie%20*;prov_generatedAtTime:datetime%20*;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B],[SarefProperty]<saref_hasProperty%200..*-++[ProvEntity],[FoafAgent]<dcterms_creator%200..*-++[ProvEntity],[SarefPropertyValue]<fhir_status%200..*-++[ProvEntity],[OwlThing]<dcterms_isPartOf%200..*-++[ProvEntity],[OwlThing]<dcterms_hasPart%200..*-++[ProvEntity],[FoafAgent]<prov_wasAttributedTo%200..*-++[ProvEntity],[OwlThing]++-%20prov_hadPrimarySource%200..*>[ProvEntity],[ProvEntity]^-[SarefPropertyValue],[ProvEntity]^-[SarefProperty],[ProvEntity]^-[QoSection],[ProvEntity]^-[QoQuestionnaireResponse],[ProvEntity]^-[QoQuestionnaire],[ProvEntity]^-[QoQuestion],[ProvEntity]^-[QoOrderedSection],[ProvEntity]^-[QoOrderedQuestion],[ProvEntity]^-[QoAnswer],[OwlThing]^-[ProvEntity],[OwlThing],[FoafAgent])

## Parents

 *  is_a: [OwlThing](OwlThing.md) - This defines IOT as the set of OWL individuals.

## Children

 * [QoAnswer](QoAnswer.md) - Answer in the questionnaire response.
 * [QoOrderedQuestion](QoOrderedQuestion.md) - Question's position within a specific questionnaire or section.
 * [QoOrderedSection](QoOrderedSection.md) - Section's position within a specific questionnaire or section.
 * [QoQuestion](QoQuestion.md) - A question.
 * [QoQuestionnaire](QoQuestionnaire.md) - A questionnaire that can be answered (collection of questions).
 * [QoQuestionnaireResponse](QoQuestionnaireResponse.md) - A response to a questionnaire (collection of answers).
 * [QoSection](QoSection.md) - A section of questions in the questionnaire.
 * [SarefProperty](SarefProperty.md) - Identifiable qualities of features of interest that can be target of devices, such as observed or controlled. A property can apply to different features of interest.
 * [SarefPropertyValue](SarefPropertyValue.md) - Describes the value for a property. The property value is optionally linked to its value expressed as an RDF literal (DP saref:hasValue), optionally to the unit of measurement (OP saref:isMeasuredIn), and optionally to the properties or properties of interest it is a value of (OP saref:isValueOfProperty).

## Referenced by Class

 *  **[OwlThing](OwlThing.md)** *[prov_hadPrimarySource](prov_hadPrimarySource.md)*  <sub>0..\*</sub>  **[ProvEntity](ProvEntity.md)**

## Attributes


### Own

 * [prov_wasAttributedTo](prov_wasAttributedTo.md)  <sub>0..\*</sub>
     * Description: Attribution is the ascribing of an entity to an agent.
     * Range: [FoafAgent](FoafAgent.md)
 * [dcterms_created](dcterms_created.md)  <sub>0..1</sub>
     * Description: The date and time when the entity was created.
     * Range: [Datetime](types/Datetime.md)
 * [dcterms_modified](dcterms_modified.md)  <sub>0..1</sub>
     * Description: The date and time when the entity was last updated.
     * Range: [Datetime](types/Datetime.md)
 * [prov_type](prov_type.md)  <sub>0..\*</sub>
     * Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [dcterms_hasPart](dcterms_hasPart.md)  <sub>0..\*</sub>
     * Description: A related resource that is included either physically or logically in the described resource.
     * Range: [OwlThing](OwlThing.md)
 * [dcterms_isPartOf](dcterms_isPartOf.md)  <sub>0..\*</sub>
     * Description: A related resource in which the described resource is physically or logically included.
     * Range: [OwlThing](OwlThing.md)
 * [prov_generatedAtTime](prov_generatedAtTime.md)  <sub>0..\*</sub>
     * Description: The time at which an entity was completely created and is available for use.
     * Range: [Datetime](types/Datetime.md)
 * [fhir_status](fhir_status.md)  <sub>0..\*</sub>
     * Description: A code specifying the state of the observation/procedure/questionnaire... Generally, this will be the in-progress or completed state.
     * Range: [SarefPropertyValue](SarefPropertyValue.md)
 * [dcterms_creator](dcterms_creator.md)  <sub>0..\*</sub>
     * Description: An entity responsible for making the resource.
     * Range: [FoafAgent](FoafAgent.md)
 * [saref_hasProperty](saref_hasProperty.md)  <sub>0..\*</sub>
     * Description: Links a feature kind or a feature of interest to one of its properties.
     * Range: [SarefProperty](SarefProperty.md)
 * [saref_hasPropertyValue](saref_hasPropertyValue.md)  <sub>0..\*</sub>
     * Description: Links a feature kind, a feature of interest, or a property of interest, to a property value.
     * Range: [SarefPropertyValue](SarefPropertyValue.md)

### Inherited from owl_Thing:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | prov:Entity |
|  | | sulo:Object |