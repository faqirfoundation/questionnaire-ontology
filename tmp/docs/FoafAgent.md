
# Class: foaf_Agent

An agent (eg. person, group, software or physical artifact).

URI: [qo:FoafAgent](https://ns.faqir.org/q-o#FoafAgent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[SarefPropertyValue],[SarefProperty],[ProvOrganization],[ProvEntity],[OwlThing],[FoafPerson],[SarefPropertyValue]<saref_hasPropertyValue%200..*-++[FoafAgent&#124;prov_type:uriorcurie%20*;prov_generatedAtTime:datetime%20*;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B],[SarefProperty]<saref_hasProperty%200..*-++[FoafAgent],[FoafAgent]<dcterms_creator%200..*-++[FoafAgent],[SarefPropertyValue]<fhir_status%200..*-++[FoafAgent],[OwlThing]<dcterms_isPartOf%200..*-++[FoafAgent],[OwlThing]<dcterms_hasPart%200..*-++[FoafAgent],[ProvEntity]++-%20prov_wasAttributedTo%200..*>[FoafAgent],[FoafAgent]^-[ProvOrganization],[FoafAgent]^-[FoafPerson],[OwlThing]^-[FoafAgent])](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[SarefPropertyValue],[SarefProperty],[ProvOrganization],[ProvEntity],[OwlThing],[FoafPerson],[SarefPropertyValue]<saref_hasPropertyValue%200..*-++[FoafAgent&#124;prov_type:uriorcurie%20*;prov_generatedAtTime:datetime%20*;owl_versionInfo(i):string%20%3F;rdfs_label(i):string%20%2B;rdfs_comment(i):string%20%2B],[SarefProperty]<saref_hasProperty%200..*-++[FoafAgent],[FoafAgent]<dcterms_creator%200..*-++[FoafAgent],[SarefPropertyValue]<fhir_status%200..*-++[FoafAgent],[OwlThing]<dcterms_isPartOf%200..*-++[FoafAgent],[OwlThing]<dcterms_hasPart%200..*-++[FoafAgent],[ProvEntity]++-%20prov_wasAttributedTo%200..*>[FoafAgent],[FoafAgent]^-[ProvOrganization],[FoafAgent]^-[FoafPerson],[OwlThing]^-[FoafAgent])

## Parents

 *  is_a: [OwlThing](OwlThing.md) - This defines IOT as the set of OWL individuals.

## Children

 * [FoafPerson](FoafPerson.md) - A person.
 * [ProvOrganization](ProvOrganization.md) - An organization is a social or legal institution such as a company, society, etc.

## Referenced by Class

 *  **[OwlThing](OwlThing.md)** *[dcterms_creator](dcterms_creator.md)*  <sub>0..\*</sub>  **[FoafAgent](FoafAgent.md)**
 *  **[ProvEntity](ProvEntity.md)** *[prov_wasAttributedTo](prov_wasAttributedTo.md)*  <sub>0..\*</sub>  **[FoafAgent](FoafAgent.md)**

## Attributes


### Own

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
| **Mappings:** | | foaf:Agent |
|  | | prov:Agent |