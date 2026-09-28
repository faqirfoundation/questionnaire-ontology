

# Class: FoafAgent 


_An agent (eg. person, group, software or physical artifact)._





URI: [foaf:Agent](http://xmlns.com/foaf/0.1/Agent)






```mermaid
 classDiagram
    class FoafAgent
    click FoafAgent href "../FoafAgent"
      OwlThing <|-- FoafAgent
        click OwlThing href "../OwlThing"
      

      FoafAgent <|-- FoafPerson
        click FoafPerson href "../FoafPerson"
      FoafAgent <|-- ProvOrganization
        click ProvOrganization href "../ProvOrganization"
      
      
      FoafAgent : dcterms_creator
        
          
    
        
        
        FoafAgent --> "*" FoafAgent : dcterms_creator
        click FoafAgent href "../FoafAgent"
    

        
      FoafAgent : dcterms_hasPart
        
          
    
        
        
        FoafAgent --> "*" OwlThing : dcterms_hasPart
        click OwlThing href "../OwlThing"
    

        
      FoafAgent : dcterms_isPartOf
        
          
    
        
        
        FoafAgent --> "*" OwlThing : dcterms_isPartOf
        click OwlThing href "../OwlThing"
    

        
      FoafAgent : fhir_status
        
          
    
        
        
        FoafAgent --> "*" SarefPropertyValue : fhir_status
        click SarefPropertyValue href "../SarefPropertyValue"
    

        
      FoafAgent : owl_versionInfo
        
      FoafAgent : prov_generatedAtTime
        
      FoafAgent : prov_hadPrimarySource
        
          
    
        
        
        FoafAgent --> "*" ProvEntity : prov_hadPrimarySource
        click ProvEntity href "../ProvEntity"
    

        
      FoafAgent : prov_type
        
      FoafAgent : prov_wasGeneratedBy
        
          
    
        
        
        FoafAgent --> "*" SuloProcess : prov_wasGeneratedBy
        click SuloProcess href "../SuloProcess"
    

        
      FoafAgent : rdfs_comment
        
      FoafAgent : rdfs_label
        
      FoafAgent : saref_hasProperty
        
          
    
        
        
        FoafAgent --> "*" SarefProperty : saref_hasProperty
        click SarefProperty href "../SarefProperty"
    

        
      FoafAgent : saref_hasPropertyValue
        
          
    
        
        
        FoafAgent --> "*" SarefPropertyValue : saref_hasPropertyValue
        click SarefPropertyValue href "../SarefPropertyValue"
    

        
      
```





## Inheritance
* [OwlThing](OwlThing.md)
    * **FoafAgent**
        * [FoafPerson](FoafPerson.md)
        * [ProvOrganization](ProvOrganization.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [prov_type](prov_type.md) | * <br/> [Uriorcurie](Uriorcurie.md) | The attribute prov:type provides further typing information for any construct... | direct |
| [dcterms_hasPart](dcterms_hasPart.md) | * <br/> [OwlThing](OwlThing.md) | A related resource that is included either physically or logically in the des... | direct |
| [dcterms_isPartOf](dcterms_isPartOf.md) | * <br/> [OwlThing](OwlThing.md) | A related resource in which the described resource is physically or logically... | direct |
| [prov_generatedAtTime](prov_generatedAtTime.md) | * <br/> [Datetime](Datetime.md) | The time at which an entity was completely created and is available for use | direct |
| [fhir_status](fhir_status.md) | * <br/> [SarefPropertyValue](SarefPropertyValue.md) | A code specifying the state of the observation/procedure/questionnaire | direct |
| [dcterms_creator](dcterms_creator.md) | * <br/> [FoafAgent](FoafAgent.md) | An entity responsible for making the resource | direct |
| [saref_hasProperty](saref_hasProperty.md) | * <br/> [SarefProperty](SarefProperty.md) | Links a feature kind or a feature of interest to one of its properties | direct |
| [saref_hasPropertyValue](saref_hasPropertyValue.md) | * <br/> [SarefPropertyValue](SarefPropertyValue.md) | Links a feature kind, a feature of interest, or a property of interest, to a ... | direct |
| [owl_versionInfo](owl_versionInfo.md) | 0..1 <br/> [String](String.md) | An owl:versionInfo statement generally has as its object a string giving info... | [OwlThing](OwlThing.md) |
| [rdfs_label](rdfs_label.md) | 1..* <br/> [String](String.md) | human-readable version of a resource's name | [OwlThing](OwlThing.md) |
| [rdfs_comment](rdfs_comment.md) | 1..* <br/> [String](String.md) | A textual comment helps clarify the meaning of RDF classes and properties | [OwlThing](OwlThing.md) |
| [prov_hadPrimarySource](prov_hadPrimarySource.md) | * <br/> [ProvEntity](ProvEntity.md) | A primary source for a topic refers to something produced by some agent with ... | [OwlThing](OwlThing.md) |
| [prov_wasGeneratedBy](prov_wasGeneratedBy.md) | * <br/> [SuloProcess](SuloProcess.md) | Generation is the completion of production of a new entity by an activity | [OwlThing](OwlThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [FoafAgent](FoafAgent.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [FoafPerson](FoafPerson.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [ProvOrganization](ProvOrganization.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [SuloProcess](SuloProcess.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [S4ehawActivity](S4ehawActivity.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [FhirProcedure](FhirProcedure.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [ProvEntity](ProvEntity.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [ProvEntity](ProvEntity.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [SarefProperty](SarefProperty.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [SarefProperty](SarefProperty.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [SarefPropertyValue](SarefPropertyValue.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [SarefPropertyValue](SarefPropertyValue.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [QoQuestionnaire](QoQuestionnaire.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [QoQuestionnaireStatus](QoQuestionnaireStatus.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [QoOrderedSection](QoOrderedSection.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [QoOrderedSection](QoOrderedSection.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [QoSection](QoSection.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [QoOrderedQuestion](QoOrderedQuestion.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [QoOrderedQuestion](QoOrderedQuestion.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [QoQuestion](QoQuestion.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [QoQuestionnaireResponseStatus](QoQuestionnaireResponseStatus.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |
| [QoAnswer](QoAnswer.md) | [prov_wasAttributedTo](prov_wasAttributedTo.md) | range | [FoafAgent](FoafAgent.md) |
| [QoAnswer](QoAnswer.md) | [dcterms_creator](dcterms_creator.md) | range | [FoafAgent](FoafAgent.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:Agent |
| native | qo:FoafAgent |
| undefined | prov:Agent |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: foaf_Agent
description: An agent (eg. person, group, software or physical artifact).
from_schema: https://ns.faqir.org/q-o
mappings:
- prov:Agent
is_a: owl_Thing
slots:
- prov_type
- dcterms_hasPart
- dcterms_isPartOf
- prov_generatedAtTime
- fhir_status
- dcterms_creator
- saref_hasProperty
- saref_hasPropertyValue
class_uri: foaf:Agent

```
</details>

### Induced

<details>
```yaml
name: foaf_Agent
description: An agent (eg. person, group, software or physical artifact).
from_schema: https://ns.faqir.org/q-o
mappings:
- prov:Agent
is_a: owl_Thing
attributes:
  prov_type:
    name: prov_type
    description: The attribute prov:type provides further typing information for any
      construct with an optional set of attribute-value pairs.
    from_schema: https://ns.faqir.org/q-o
    exact_mappings:
    - rdf:type
    - sphn:hasTypeCode
    narrow_mappings:
    - schema:procedureType
    rank: 1000
    domain: owl_Thing
    slot_uri: prov:type
    alias: prov_type
    owner: foaf_Agent
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: uriorcurie
    required: false
    multivalued: true
  dcterms_hasPart:
    name: dcterms_hasPart
    description: A related resource that is included either physically or logically
      in the described resource.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: dcterms:hasPart
    alias: dcterms_hasPart
    owner: foaf_Agent
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    inverse: dcterms_isPartOf
    range: owl_Thing
    required: false
    multivalued: true
  dcterms_isPartOf:
    name: dcterms_isPartOf
    description: A related resource in which the described resource is physically
      or logically included.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: dcterms:isPartOf
    alias: dcterms_isPartOf
    owner: foaf_Agent
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    inverse: dcterms_hasPart
    range: owl_Thing
    required: false
    multivalued: true
  prov_generatedAtTime:
    name: prov_generatedAtTime
    description: The time at which an entity was completely created and is available
      for use.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: prov:generatedAtTime
    alias: prov_generatedAtTime
    owner: foaf_Agent
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: datetime
    required: false
    multivalued: true
  fhir_status:
    name: fhir_status
    description: A code specifying the state of the observation/procedure/questionnaire...
      Generally, this will be the in-progress or completed state.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    is_a: saref_hasPropertyValue
    domain: owl_Thing
    slot_uri: fhir:resource-status
    alias: fhir_status
    owner: foaf_Agent
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: saref_PropertyValue
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  dcterms_creator:
    name: dcterms_creator
    description: An entity responsible for making the resource.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: dcterms:creator
    alias: dcterms_creator
    owner: foaf_Agent
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: foaf_Agent
    required: false
    multivalued: true
  saref_hasProperty:
    name: saref_hasProperty
    description: Links a feature kind or a feature of interest to one of its properties.
    from_schema: https://ns.faqir.org/q-o
    mappings:
    - ssn:hasProperty
    rank: 1000
    domain: owl_Thing
    slot_uri: saref:hasProperty
    alias: saref_hasProperty
    owner: foaf_Agent
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: saref_Property
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  saref_hasPropertyValue:
    name: saref_hasPropertyValue
    description: Links a feature kind, a feature of interest, or a property of interest,
      to a property value.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: saref:hasPropertyValue
    alias: saref_hasPropertyValue
    owner: foaf_Agent
    domain_of:
    - foaf_Agent
    - sulo_Process
    - prov_Entity
    range: saref_PropertyValue
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  owl_versionInfo:
    name: owl_versionInfo
    description: An owl:versionInfo statement generally has as its object a string
      giving information about this version, for example RCS/CVS keywords. This statement
      does not contribute to the logical meaning of the ontology other than that given
      by the RDF(S) model theory.
    from_schema: https://ns.faqir.org/q-o
    close_mappings:
    - saref:hasVersion
    rank: 1000
    domain: owl_Thing
    slot_uri: owl:versionInfo
    alias: owl_versionInfo
    owner: foaf_Agent
    domain_of:
    - owl_Thing
    range: string
    required: false
    multivalued: false
  rdfs_label:
    name: rdfs_label
    description: human-readable version of a resource's name. Multilingual labels
      are supported using the language tagging facility of RDF literals.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: rdfs:label
    alias: rdfs_label
    owner: foaf_Agent
    domain_of:
    - owl_Thing
    range: string
    required: true
    multivalued: true
  rdfs_comment:
    name: rdfs_comment
    description: A textual comment helps clarify the meaning of RDF classes and properties.
      Such in-line documentation complements the use of both formal techniques (Ontology
      and rule languages) and informal (prose documentation, examples, test cases).
      A variety of documentation forms can be combined to indicate the intended meaning
      of the classes and properties described in an RDF vocabulary. Since RDF vocabularies
      are expressed as RDF graphs, vocabularies defined in other namespaces may be
      used to provide richer documentation.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: rdfs:comment
    alias: rdfs_comment
    owner: foaf_Agent
    domain_of:
    - owl_Thing
    range: string
    required: true
    multivalued: true
  prov_hadPrimarySource:
    name: prov_hadPrimarySource
    description: A primary source for a topic refers to something produced by some
      agent with direct experience and knowledge about the topic, at the time of the
      topic's study, without benefit from hindsight. Because of the directness of
      primary sources, they 'speak for themselves' in ways that cannot be captured
      through the filter of secondary sources. As such, it is important for secondary
      sources to reference those primary sources from which they were derived, so
      that their reliability can be investigated. A primary source relation is a particular
      case of derivation of secondary materials from their primary sources. It is
      recognized that the determination of primary sources can be up to interpretation,
      and should be done according to conventions accepted within the application's
      domain.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: prov:hadPrimarySource
    alias: prov_hadPrimarySource
    owner: foaf_Agent
    domain_of:
    - owl_Thing
    range: prov_Entity
    required: false
    multivalued: true
  prov_wasGeneratedBy:
    name: prov_wasGeneratedBy
    description: Generation is the completion of production of a new entity by an
      activity. This entity did not exist before generation and becomes available
      for usage after this generation.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: owl_Thing
    slot_uri: prov:wasGeneratedBy
    alias: prov_wasGeneratedBy
    owner: foaf_Agent
    domain_of:
    - owl_Thing
    range: sulo_Process
    required: false
    multivalued: true
class_uri: foaf:Agent

```
</details>