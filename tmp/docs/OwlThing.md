
# Class: owl_Thing

This defines IOT as the set of OWL individuals.

URI: [qo:OwlThing](https://ns.faqir.org/q-o#OwlThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[ProvEntity],[SuloProcess]<prov_wasGeneratedBy%200..*-++[OwlThing&#124;owl_versionInfo:string%20%3F;rdfs_label:string%20%2B;rdfs_comment:string%20%2B],[ProvEntity]<prov_hadPrimarySource%200..*-++[OwlThing],[FoafAgent]++-%20dcterms_hasPart%200..*>[OwlThing],[SuloProcess]++-%20dcterms_hasPart%200..*>[OwlThing],[ProvEntity]++-%20dcterms_hasPart%200..*>[OwlThing],[FoafAgent]++-%20dcterms_isPartOf%200..*>[OwlThing],[SuloProcess]++-%20dcterms_isPartOf%200..*>[OwlThing],[ProvEntity]++-%20dcterms_isPartOf%200..*>[OwlThing],[OwlThing]^-[SuloProcess],[OwlThing]^-[ProvEntity],[OwlThing]^-[FoafAgent],[FoafAgent])](https://yuml.me/diagram/nofunky;dir:TB/class/[SuloProcess],[ProvEntity],[SuloProcess]<prov_wasGeneratedBy%200..*-++[OwlThing&#124;owl_versionInfo:string%20%3F;rdfs_label:string%20%2B;rdfs_comment:string%20%2B],[ProvEntity]<prov_hadPrimarySource%200..*-++[OwlThing],[FoafAgent]++-%20dcterms_hasPart%200..*>[OwlThing],[SuloProcess]++-%20dcterms_hasPart%200..*>[OwlThing],[ProvEntity]++-%20dcterms_hasPart%200..*>[OwlThing],[FoafAgent]++-%20dcterms_isPartOf%200..*>[OwlThing],[SuloProcess]++-%20dcterms_isPartOf%200..*>[OwlThing],[ProvEntity]++-%20dcterms_isPartOf%200..*>[OwlThing],[OwlThing]^-[SuloProcess],[OwlThing]^-[ProvEntity],[OwlThing]^-[FoafAgent],[FoafAgent])

## Children

 * [FoafAgent](FoafAgent.md) - An agent (eg. person, group, software or physical artifact).
 * [ProvEntity](ProvEntity.md) - An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
 * [SuloProcess](SuloProcess.md) - a process is a entity that unfolds in time, has temporal parts, and has objects that participate in the process.

## Referenced by Class

 *  **[OwlThing](OwlThing.md)** *[dcterms_hasPart](dcterms_hasPart.md)*  <sub>0..\*</sub>  **[OwlThing](OwlThing.md)**
 *  **[OwlThing](OwlThing.md)** *[dcterms_isPartOf](dcterms_isPartOf.md)*  <sub>0..\*</sub>  **[OwlThing](OwlThing.md)**
 *  **[SuloProcess](SuloProcess.md)** *[prov_generated](prov_generated.md)*  <sub>0..\*</sub>  **[OwlThing](OwlThing.md)**

## Attributes


### Own

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
| **Mappings:** | | owl:Thing |