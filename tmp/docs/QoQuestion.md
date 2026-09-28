
# Class: qo_Question

A question.

URI: [qo:QoQuestion](https://ns.faqir.org/q-o#QoQuestion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[SarefPropertyValue],[SarefProperty],[ProvOrganization]<dcterms_creator%201..*-++[QoQuestion&#124;qo_multivalued:boolean%20%3F;qo_tag:string%20%2B;qo_codingOrdinal:boolean%20%3F;prov_type:qo_QuestionType%20%2B;dcterms_created(i):datetime%20%3F;dcterms_modified(i):datetime%20%3F;prov_generatedAtTime(i):datetime%20*;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B],[IntervalParams]<qo_intervalParams%200..1-++[QoQuestion],[ValueCoding]<qo_codingParams%200..*-++[QoQuestion],[NumericalParams]<qo_numericalParams%200..1-++[QoQuestion],[QoOrderedQuestion]++-%20qo_question%201..1>[QoQuestion],[QoAnswer]++-%20qo_toQuestion%201..1>[QoQuestion],[ProvEntity]^-[QoQuestion],[QoOrderedQuestion],[QoAnswer],[ProvOrganization],[ProvEntity],[OwlThing],[FoafAgent],[ValueCoding],[NumericalParams],[IntervalParams])](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[SarefPropertyValue],[SarefProperty],[ProvOrganization]<dcterms_creator%201..*-++[QoQuestion&#124;qo_multivalued:boolean%20%3F;qo_tag:string%20%2B;qo_codingOrdinal:boolean%20%3F;prov_type:qo_QuestionType%20%2B;dcterms_created(i):datetime%20%3F;dcterms_modified(i):datetime%20%3F;prov_generatedAtTime(i):datetime%20*;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B],[IntervalParams]<qo_intervalParams%200..1-++[QoQuestion],[ValueCoding]<qo_codingParams%200..*-++[QoQuestion],[NumericalParams]<qo_numericalParams%200..1-++[QoQuestion],[QoOrderedQuestion]++-%20qo_question%201..1>[QoQuestion],[QoAnswer]++-%20qo_toQuestion%201..1>[QoQuestion],[ProvEntity]^-[QoQuestion],[QoOrderedQuestion],[QoAnswer],[ProvOrganization],[ProvEntity],[OwlThing],[FoafAgent],[ValueCoding],[NumericalParams],[IntervalParams])

## Parents

 *  is_a: [ProvEntity](ProvEntity.md) - An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.

## Referenced by Class

 *  **[QoOrderedQuestion](QoOrderedQuestion.md)** *[qo_question](qo_question.md)*  <sub>1..1</sub>  **[QoQuestion](QoQuestion.md)**
 *  **[QoAnswer](QoAnswer.md)** *[qo_toQuestion](qo_toQuestion.md)*  <sub>1..1</sub>  **[QoQuestion](QoQuestion.md)**

## Attributes


### Own

 * [qo_multivalued](qo_multivalued.md)  <sub>0..1</sub>
     * Description: Indicates whether this question allows multiple answers (true) or it's single answer (false).
     * Range: [Boolean](types/Boolean.md)
 * [➞qo_tag](qoQuestion__qo_tag.md)  <sub>1..\*</sub>
     * Description: Internal English identifier, e.g., 'q_pain_level'.
     * Range: [String](types/String.md)
 * [➞qo_numericalParams](qoQuestion__qo_numericalParams.md)  <sub>0..1</sub>
     * Description: Unit and Precision limiting the quantitative answer for the question.
     * Range: [NumericalParams](NumericalParams.md)
 * [➞qo_codingParams](qoQuestion__qo_codingParams.md)  <sub>0..\*</sub>
     * Description: Code and Display of each option offered as answer to the choice or open-choice question.
     * Range: [ValueCoding](ValueCoding.md)
 * [➞qo_codingOrdinal](qoQuestion__qo_codingOrdinal.md)  <sub>0..1</sub>
     * Description: Indicates if the choices in a choice or open-choice question are ordered (true) or unordered (false, categorical).
     * Range: [Boolean](types/Boolean.md)
 * [➞qo_intervalParams](qoQuestion__qo_intervalParams.md)  <sub>0..1</sub>
     * Description: Minimum and Maximum limiting the range the answer must be in for the question.
     * Range: [IntervalParams](IntervalParams.md)
 * [qo_Question➞prov_type](qo_Question_prov_type.md)  <sub>1..\*</sub>
     * Description: Type of the question (e.g., choice, openChoice, numberInterval, decimal, dateTime, text). Determines valid answers.
     * Range: [qo_QuestionType](qo_QuestionType.md)
 * [qo_Question➞dcterms_creator](qo_Question_dcterms_creator.md)  <sub>1..\*</sub>
     * Description: An entity responsible for making the resource.
     * Range: [ProvOrganization](ProvOrganization.md)

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
 * [dcterms_created](dcterms_created.md)  <sub>0..1</sub>
     * Description: The date and time when the entity was created.
     * Range: [Datetime](types/Datetime.md)
 * [dcterms_modified](dcterms_modified.md)  <sub>0..1</sub>
     * Description: The date and time when the entity was last updated.
     * Range: [Datetime](types/Datetime.md)
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
 * [saref_hasProperty](saref_hasProperty.md)  <sub>0..\*</sub>
     * Description: Links a feature kind or a feature of interest to one of its properties.
     * Range: [SarefProperty](SarefProperty.md)
 * [saref_hasPropertyValue](saref_hasPropertyValue.md)  <sub>0..\*</sub>
     * Description: Links a feature kind, a feature of interest, or a property of interest, to a property value.
     * Range: [SarefPropertyValue](SarefPropertyValue.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | qo:Question |
| **Narrow Mappings:** | | fhir:Questionnaire.item.where(type='question') |