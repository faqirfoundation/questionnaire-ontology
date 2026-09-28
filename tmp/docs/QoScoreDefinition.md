
# Class: qo_ScoreDefinition

A score calculated from questions.

URI: [qo:QoScoreDefinition](https://ns.faqir.org/q-o#QoScoreDefinition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[SarefPropertyValue],[SarefProperty],[QoSection],[QoScoreValue],[QoScoreParameter],[ProvOrganization]<dcterms_creator%201..*-++[QoScoreDefinition&#124;qo_formula:string;qo_categories:string%20*;qo_interpretationGuide:string%20%3F;prov_type:qo_ScoreType%20%2B;dcterms_created:datetime;dcterms_modified:datetime;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B],[IntervalParams]<qo_intervalParams%200..1-++[QoScoreDefinition],[QoQuestion]<qo_usesQuestion%201..*-++[QoScoreDefinition],[QoScoreParameter]<qo_parameter%200..*-++[QoScoreDefinition],[QoQuestionnaire]++-%20qo_usesScoreDefinition%200..*>[QoScoreDefinition],[QoSection]++-%20qo_usesScoreDefinition%200..*>[QoScoreDefinition],[QoScoreValue]++-%20qo_basedOn%201..1>[QoScoreDefinition],[QoQuestionnaire]++-%20qo_usesScoreDefinition(i)%200..*>[QoScoreDefinition],[QoSection]++-%20qo_usesScoreDefinition(i)%200..*>[QoScoreDefinition],[ProvEntity]^-[QoScoreDefinition],[QoQuestionnaire],[QoQuestion],[ProvOrganization],[ProvEntity],[OwlThing],[FoafAgent],[IntervalParams],[FlexibleDateTime])](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[SarefPropertyValue],[SarefProperty],[QoSection],[QoScoreValue],[QoScoreParameter],[ProvOrganization]<dcterms_creator%201..*-++[QoScoreDefinition&#124;qo_formula:string;qo_categories:string%20*;qo_interpretationGuide:string%20%3F;prov_type:qo_ScoreType%20%2B;dcterms_created:datetime;dcterms_modified:datetime;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B],[IntervalParams]<qo_intervalParams%200..1-++[QoScoreDefinition],[QoQuestion]<qo_usesQuestion%201..*-++[QoScoreDefinition],[QoScoreParameter]<qo_parameter%200..*-++[QoScoreDefinition],[QoQuestionnaire]++-%20qo_usesScoreDefinition%200..*>[QoScoreDefinition],[QoSection]++-%20qo_usesScoreDefinition%200..*>[QoScoreDefinition],[QoScoreValue]++-%20qo_basedOn%201..1>[QoScoreDefinition],[QoQuestionnaire]++-%20qo_usesScoreDefinition(i)%200..*>[QoScoreDefinition],[QoSection]++-%20qo_usesScoreDefinition(i)%200..*>[QoScoreDefinition],[ProvEntity]^-[QoScoreDefinition],[QoQuestionnaire],[QoQuestion],[ProvOrganization],[ProvEntity],[OwlThing],[FoafAgent],[IntervalParams],[FlexibleDateTime])

## Parents

 *  is_a: [ProvEntity](ProvEntity.md) - An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.

## Referenced by Class

 *  **[QoQuestionnaire](QoQuestionnaire.md)** *[qo_Questionnaire➞qo_usesScoreDefinition](qo_Questionnaire_qo_usesScoreDefinition.md)*  <sub>0..\*</sub>  **[QoScoreDefinition](QoScoreDefinition.md)**
 *  **[QoSection](QoSection.md)** *[qo_Section➞qo_usesScoreDefinition](qo_Section_qo_usesScoreDefinition.md)*  <sub>0..\*</sub>  **[QoScoreDefinition](QoScoreDefinition.md)**
 *  **[QoScoreValue](QoScoreValue.md)** *[qo_basedOn](qo_basedOn.md)*  <sub>1..1</sub>  **[QoScoreDefinition](QoScoreDefinition.md)**
 *  **None** *[qo_usesScoreDefinition](qo_usesScoreDefinition.md)*  <sub>0..\*</sub>  **[QoScoreDefinition](QoScoreDefinition.md)**

## Attributes


### Own

 * [qo_parameter](qo_parameter.md)  <sub>0..\*</sub>
     * Description: The ScoreParameter that is required for this ScoreDefinition.
     * Range: [QoScoreParameter](QoScoreParameter.md)
 * [qo_usesQuestion](qo_usesQuestion.md)  <sub>1..\*</sub>
     * Description: The Question(s) that this ScoreDefinition is based on.
     * Range: [QoQuestion](QoQuestion.md)
 * [➞qo_formula](qoScoreDefinition__qo_formula.md)  <sub>1..1</sub>
     * Description: The formula used to calculate the score.
     * Range: [String](types/String.md)
 * [➞qo_categories](qoScoreDefinition__qo_categories.md)  <sub>0..\*</sub>
     * Description: Categories for categorical scores.
     * Range: [String](types/String.md)
 * [➞qo_interpretationGuide](qoScoreDefinition__qo_interpretationGuide.md)  <sub>0..1</sub>
     * Description: How to interpret the score values. English explanation.
     * Range: [String](types/String.md)
 * [➞qo_intervalParams](qoScoreDefinition__qo_intervalParams.md)  <sub>0..1</sub>
     * Description: Minimum and maximum values for numerical_percentage and numerical_z_score scores.
     * Range: [IntervalParams](IntervalParams.md)
 * [qo_ScoreDefinition➞prov_type](qo_ScoreDefinition_prov_type.md)  <sub>1..\*</sub>
     * Description: Type of score: numerical_continuous, numerical_integer, numerical_percentage, numerical_z_score, numerical_t_score or categorical. Determines valid score values.
     * Range: [qo_ScoreType](qo_ScoreType.md)
 * [qo_ScoreDefinition➞dcterms_created](qo_ScoreDefinition_dcterms_created.md)  <sub>1..1</sub>
     * Description: The date and time when the score was defined.
     * Range: [Datetime](types/Datetime.md)
 * [qo_ScoreDefinition➞dcterms_modified](qo_ScoreDefinition_dcterms_modified.md)  <sub>1..1</sub>
     * Description: The date and time when the score definition was last updated.
     * Range: [Datetime](types/Datetime.md)
 * [qo_ScoreDefinition➞dcterms_creator](qo_ScoreDefinition_dcterms_creator.md)  <sub>1..\*</sub>
     * Description: The Organization that has created this Score Definition.
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
 * [dcterms_hasPart](dcterms_hasPart.md)  <sub>0..\*</sub>
     * Description: A related resource that is included either physically or logically in the described resource.
     * Range: [OwlThing](OwlThing.md)
 * [dcterms_isPartOf](dcterms_isPartOf.md)  <sub>0..\*</sub>
     * Description: A related resource in which the described resource is physically or logically included.
     * Range: [OwlThing](OwlThing.md)
 * [prov_generatedAtTime](prov_generatedAtTime.md)  <sub>0..\*</sub>
     * Description: The time at which an entity was completely created and is available for use.
     * Range: [FlexibleDateTime](FlexibleDateTime.md)
 * [fhir_status](fhir_status.md)  <sub>0..\*</sub>
     * Description: A code specifying the state of the observation/procedure/questionnaire... Generally, this will be the in-progress or completed state.
     * Range: [SarefPropertyValue](SarefPropertyValue.md)
 * [prov_hadPrimarySource](prov_hadPrimarySource.md)  <sub>0..\*</sub>
     * Description: A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources from which they were derived, so that their reliability can be investigated. A primary source relation is a particular case of derivation of secondary materials from their primary sources. It is recognized that the determination of primary sources can be up to interpretation, and should be done according to conventions accepted within the application's domain.
     * Range: [ProvEntity](ProvEntity.md)
 * [prov_wasGeneratedBy](prov_wasGeneratedBy.md)  <sub>0..\*</sub>
     * Description: Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.
     * Range: [SuloProcess](SuloProcess.md)
 * [saref_hasProperty](saref_hasProperty.md)  <sub>0..\*</sub>
     * Description: Links a feature kind or a feature of interest to one of its properties.
     * Range: [SarefProperty](SarefProperty.md)
 * [saref_hasPropertyValue](saref_hasPropertyValue.md)  <sub>0..\*</sub>
     * Description: Links a feature kind, a feature of interest, or a property of interest, to a property value.
     * Range: [SarefPropertyValue](SarefPropertyValue.md)
 * [prov_wasAttributedTo](prov_wasAttributedTo.md)  <sub>0..\*</sub>
     * Description: Attribution is the ascribing of an entity to an agent.
     * Range: [FoafAgent](FoafAgent.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | qo:ScoreDefinition |