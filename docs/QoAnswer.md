

# Class: QoAnswer 


_A recorded value, or selection provided in response to a specific inquiry item._





URI: [qo:Answer](https://ns.faqir.org/q-o#Answer)





```mermaid
 classDiagram
    class QoAnswer
    click QoAnswer href "../QoAnswer/"
      ProvEntity <|-- QoAnswer
        click ProvEntity href "../ProvEntity/"
      
      QoAnswer : dcterms_created
        
      QoAnswer : dcterms_creator
        
          
    
        
        
        QoAnswer --> "*" FoafAgent : dcterms_creator
        click FoafAgent href "../FoafAgent/"
    

        
      QoAnswer : dcterms_hasPart
        
          
    
        
        
        QoAnswer --> "*" OwlThing : dcterms_hasPart
        click OwlThing href "../OwlThing/"
    

        
      QoAnswer : dcterms_isPartOf
        
          
    
        
        
        QoAnswer --> "*" OwlThing : dcterms_isPartOf
        click OwlThing href "../OwlThing/"
    

        
      QoAnswer : dcterms_modified
        
      QoAnswer : fhir_status
        
          
    
        
        
        QoAnswer --> "*" SarefPropertyValue : fhir_status
        click SarefPropertyValue href "../SarefPropertyValue/"
    

        
      QoAnswer : owl_versionInfo
        
      QoAnswer : prov_generatedAtTime
        
      QoAnswer : prov_hadPrimarySource
        
          
    
        
        
        QoAnswer --> "*" ProvEntity : prov_hadPrimarySource
        click ProvEntity href "../ProvEntity/"
    

        
      QoAnswer : prov_type
        
      QoAnswer : prov_wasAttributedTo
        
          
    
        
        
        QoAnswer --> "*" FoafAgent : prov_wasAttributedTo
        click FoafAgent href "../FoafAgent/"
    

        
      QoAnswer : prov_wasGeneratedBy
        
          
    
        
        
        QoAnswer --> "*" SuloProcess : prov_wasGeneratedBy
        click SuloProcess href "../SuloProcess/"
    

        
      QoAnswer : qo_answerValue
        
      QoAnswer : qo_isEmpty
        
      QoAnswer : qo_toQuestion
        
          
    
        
        
        QoAnswer --> "1" QoQuestion : qo_toQuestion
        click QoQuestion href "../QoQuestion/"
    

        
      QoAnswer : rdfs_comment
        
      QoAnswer : rdfs_label
        
      QoAnswer : saref_hasProperty
        
          
    
        
        
        QoAnswer --> "*" SarefProperty : saref_hasProperty
        click SarefProperty href "../SarefProperty/"
    

        
      QoAnswer : saref_hasPropertyValue
        
          
    
        
        
        QoAnswer --> "*" SarefPropertyValue : saref_hasPropertyValue
        click SarefPropertyValue href "../SarefPropertyValue/"
    

        
      
```





## Inheritance
* [OwlThing](OwlThing.md)
    * [ProvEntity](ProvEntity.md)
        * **QoAnswer**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [qo_toQuestion](qo_toQuestion.md) | 1 <br/> [QoQuestion](QoQuestion.md) | Links a recorded response value back to its originating inquiry item definiti... | direct |
| [qo_answerValue](qo_answerValue.md) | 0..1 <br/> [String](String.md)&nbsp;or&nbsp;<br />[Float](Float.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[Datetime](Datetime.md) | The recorded literal payload (numeric scalar, textual/coded string, or timest... | direct |
| [qo_isEmpty](qo_isEmpty.md) | 0..1 <br/> [Boolean](Boolean.md) | Specifies an explicit assertion that an item was purposefully omitted or unpo... | direct |
| [prov_wasAttributedTo](prov_wasAttributedTo.md) | * <br/> [FoafAgent](FoafAgent.md) | Attribution is the ascribing of an entity to an agent | [ProvEntity](ProvEntity.md) |
| [dcterms_created](dcterms_created.md) | 0..1 <br/> [Datetime](Datetime.md) | The date and time when the entity was created | [ProvEntity](ProvEntity.md) |
| [dcterms_modified](dcterms_modified.md) | 0..1 <br/> [Datetime](Datetime.md) | The date and time when the entity was last updated | [ProvEntity](ProvEntity.md) |
| [prov_type](prov_type.md) | * <br/> [Uriorcurie](Uriorcurie.md) | The attribute prov:type provides further typing information for any construct... | [ProvEntity](ProvEntity.md) |
| [dcterms_hasPart](dcterms_hasPart.md) | * <br/> [OwlThing](OwlThing.md) | A related resource that is included either physically or logically in the des... | [ProvEntity](ProvEntity.md) |
| [dcterms_isPartOf](dcterms_isPartOf.md) | * <br/> [OwlThing](OwlThing.md) | A related resource in which the described resource is physically or logically... | [ProvEntity](ProvEntity.md) |
| [prov_generatedAtTime](prov_generatedAtTime.md) | 1 <br/> [Datetime](Datetime.md) | The time at which an entity was completely created and is available for use | [ProvEntity](ProvEntity.md) |
| [fhir_status](fhir_status.md) | * <br/> [SarefPropertyValue](SarefPropertyValue.md) | A code specifying the state of the observation/procedure/questionnaire | [ProvEntity](ProvEntity.md) |
| [dcterms_creator](dcterms_creator.md) | * <br/> [FoafAgent](FoafAgent.md) | An entity responsible for making the resource | [ProvEntity](ProvEntity.md) |
| [saref_hasProperty](saref_hasProperty.md) | * <br/> [SarefProperty](SarefProperty.md) | Links a feature kind or a feature of interest to one of its properties | [ProvEntity](ProvEntity.md) |
| [saref_hasPropertyValue](saref_hasPropertyValue.md) | * <br/> [SarefPropertyValue](SarefPropertyValue.md) | Links a feature kind, a feature of interest, or a property of interest, to a ... | [ProvEntity](ProvEntity.md) |
| [owl_versionInfo](owl_versionInfo.md) | 0..1 <br/> [String](String.md) | An owl:versionInfo statement generally has as its object a string giving info... | [OwlThing](OwlThing.md) |
| [rdfs_label](rdfs_label.md) | 1..* <br/> [String](String.md) | human-readable version of a resource's name | [OwlThing](OwlThing.md) |
| [rdfs_comment](rdfs_comment.md) | 1..* <br/> [String](String.md) | A textual comment helps clarify the meaning of RDF classes and properties | [OwlThing](OwlThing.md) |
| [prov_hadPrimarySource](prov_hadPrimarySource.md) | * <br/> [ProvEntity](ProvEntity.md) | A primary source for a topic refers to something produced by some agent with ... | [OwlThing](OwlThing.md) |
| [prov_wasGeneratedBy](prov_wasGeneratedBy.md) | * <br/> [SuloProcess](SuloProcess.md) | Generation is the completion of production of a new entity by an activity | [OwlThing](OwlThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [QoQuestionnaireResponse](QoQuestionnaireResponse.md) | [qo_hasAnswer](qo_hasAnswer.md) | range | [QoAnswer](QoAnswer.md) |
| [QoAnswer](QoAnswer.md) | [qo_toQuestion](qo_toQuestion.md) | domain | [QoAnswer](QoAnswer.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://ns.faqir.org/q-o




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qo:Answer |
| native | qo:QoAnswer |
| undefined | fhir:QuestionnaireResponse.item.answer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: qo_Answer
description: A recorded value, or selection provided in response to a specific inquiry
  item.
from_schema: https://ns.faqir.org/q-o
mappings:
- fhir:QuestionnaireResponse.item.answer
is_a: prov_Entity
slots:
- qo_toQuestion
slot_usage:
  prov_generatedAtTime:
    name: prov_generatedAtTime
    required: true
    multivalued: false
attributes:
  qo_answerValue:
    name: qo_answerValue
    description: The recorded literal payload (numeric scalar, textual/coded string,
      or timestamp) representing the output of a specific inquiry execution.
    from_schema: https://ns.faqir.org/q-o
    narrow_mappings:
    - fhir:QuestionnaireResponse.item.answer
    rank: 1000
    slot_uri: qo:answerValue
    domain_of:
    - qo_Answer
    required: false
    multivalued: false
    any_of:
    - range: float
    - range: string
    - range: datetime
  qo_isEmpty:
    name: qo_isEmpty
    description: Specifies an explicit assertion that an item was purposefully omitted
      or unpopulated by the respondent rather than skipped due to systemic error.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:isEmpty
    ifabsent: 'False'
    domain_of:
    - qo_Answer
    range: boolean
class_uri: qo:Answer

```
</details>

### Induced

<details>
```yaml
name: qo_Answer
description: A recorded value, or selection provided in response to a specific inquiry
  item.
from_schema: https://ns.faqir.org/q-o
mappings:
- fhir:QuestionnaireResponse.item.answer
is_a: prov_Entity
slot_usage:
  prov_generatedAtTime:
    name: prov_generatedAtTime
    required: true
    multivalued: false
attributes:
  qo_answerValue:
    name: qo_answerValue
    description: The recorded literal payload (numeric scalar, textual/coded string,
      or timestamp) representing the output of a specific inquiry execution.
    from_schema: https://ns.faqir.org/q-o
    narrow_mappings:
    - fhir:QuestionnaireResponse.item.answer
    rank: 1000
    slot_uri: qo:answerValue
    alias: qo_answerValue
    owner: qo_Answer
    domain_of:
    - qo_Answer
    range: string
    required: false
    multivalued: false
    any_of:
    - range: float
    - range: string
    - range: datetime
  qo_isEmpty:
    name: qo_isEmpty
    description: Specifies an explicit assertion that an item was purposefully omitted
      or unpopulated by the respondent rather than skipped due to systemic error.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: qo:isEmpty
    ifabsent: 'False'
    alias: qo_isEmpty
    owner: qo_Answer
    domain_of:
    - qo_Answer
    range: boolean
  qo_toQuestion:
    name: qo_toQuestion
    description: Links a recorded response value back to its originating inquiry item
      definition.
    from_schema: https://ns.faqir.org/q-o
    narrow_mappings:
    - fhir:QuestionnaireResponse.item.answer.question
    rank: 1000
    domain: qo_Answer
    slot_uri: qo:toQuestion
    alias: qo_toQuestion
    owner: qo_Answer
    domain_of:
    - qo_Answer
    range: qo_Question
    required: true
    multivalued: false
  prov_wasAttributedTo:
    name: prov_wasAttributedTo
    description: Attribution is the ascribing of an entity to an agent.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    domain: prov_Entity
    slot_uri: prov:wasAttributedTo
    alias: prov_wasAttributedTo
    owner: qo_Answer
    domain_of:
    - prov_Entity
    range: foaf_Agent
    required: false
    multivalued: true
  dcterms_created:
    name: dcterms_created
    description: The date and time when the entity was created.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: dcterms:created
    alias: dcterms_created
    owner: qo_Answer
    domain_of:
    - prov_Entity
    range: datetime
    required: false
  dcterms_modified:
    name: dcterms_modified
    description: The date and time when the entity was last updated.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    slot_uri: dcterms:modified
    alias: dcterms_modified
    owner: qo_Answer
    domain_of:
    - prov_Entity
    range: datetime
    required: false
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
    slot_uri: prov:type
    alias: prov_type
    owner: qo_Answer
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
    slot_uri: dcterms:hasPart
    alias: dcterms_hasPart
    owner: qo_Answer
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
    slot_uri: dcterms:isPartOf
    alias: dcterms_isPartOf
    owner: qo_Answer
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
    slot_uri: prov:generatedAtTime
    alias: prov_generatedAtTime
    owner: qo_Answer
    domain_of:
    - foaf_Agent
    - prov_Entity
    range: datetime
    required: true
    multivalued: false
  fhir_status:
    name: fhir_status
    description: A code specifying the state of the observation/procedure/questionnaire...
      Generally, this will be the in-progress or completed state.
    from_schema: https://ns.faqir.org/q-o
    rank: 1000
    is_a: saref_hasPropertyValue
    slot_uri: fhir:resource-status
    alias: fhir_status
    owner: qo_Answer
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
    slot_uri: dcterms:creator
    alias: dcterms_creator
    owner: qo_Answer
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
    slot_uri: saref:hasProperty
    alias: saref_hasProperty
    owner: qo_Answer
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
    slot_uri: saref:hasPropertyValue
    alias: saref_hasPropertyValue
    owner: qo_Answer
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
    owner: qo_Answer
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
    owner: qo_Answer
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
    owner: qo_Answer
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
    owner: qo_Answer
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
    owner: qo_Answer
    domain_of:
    - owl_Thing
    range: sulo_Process
    required: false
    multivalued: true
class_uri: qo:Answer

```
</details>