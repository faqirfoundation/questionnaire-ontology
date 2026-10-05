# Auto generated from questionnaire_ontology.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-10-05T14:13:35
# Schema: Questionnaire-Ontology
#
# id: https://ns.faqir.org/q-o
# description: FAQIR Questionnaire Ontology
# license: Apache Software License 2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from . owl import OwlThing
from linkml_runtime.utils.metamodelcore import Bool, Curie, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = "2.0.0"

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
FHIR = CurieNamespace('fhir', 'http://hl7.org/fhir/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OMOP = CurieNamespace('omop', 'https://www.ohdsi.org/data-standardization/')
OPENEHR = CurieNamespace('openEHR', 'http://openehr.org/v1/StructureDefinition/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PHRO = CurieNamespace('phro', 'https://ns.faqir.org/phr-o#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QO = CurieNamespace('qo', 'https://ns.faqir.org/q-o#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
S4EHAW = CurieNamespace('s4ehaw', 'https://saref.etsi.org/saref4ehaw/')
SAREF = CurieNamespace('saref', 'https://saref.etsi.org/core/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
SNOMED = CurieNamespace('snomed', 'http://snomed.info/id/')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SPHN = CurieNamespace('sphn', 'https://biomedit.ch/rdf/sphn-schema/sphn#')
SSN = CurieNamespace('ssn', 'http://www.w3.org/ns/ssn/')
SULO = CurieNamespace('sulo', 'https://aidava-dev.github.io/sulo/ontospy/index.html')
TIME = CurieNamespace('time', 'http://www.w3.org/2006/time#')
UCUM = CurieNamespace('ucum', 'https://unitsofmeasure.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = QO


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = QO.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = QO.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD["boolean"]
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = QO.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = QO.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD["double"]
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = QO.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = QO.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD["time"]
    type_class_curie = "xsd:time"
    type_name = "time"
    type_model_uri = QO.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = QO.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = QO.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML["DateOrDatetime"]
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = QO.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = QO.Uriorcurie


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = QO.Curie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = QO.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = QO.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX["iri"]
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = QO.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX["nonLiteral"]
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = QO.Nodeidentifier


class Jsonpointer(str):
    """ A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "jsonpointer"
    type_model_uri = QO.Jsonpointer


class Jsonpath(str):
    """ A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "jsonpath"
    type_model_uri = QO.Jsonpath


class Sparqlpath(str):
    """ A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sparqlpath"
    type_model_uri = QO.Sparqlpath


# Class references



class ProvAttribution(YAMLRoot):
    """
    An instance of prov:Attribution provides additional descriptions about the binary prov:wasAttributedTo relation
    from an prov:Entity to some prov:Agent that had some responsible for it. For example, :cake prov:wasAttributedTo
    :baker; prov:qualifiedAttribution [ a prov:Attribution; prov:entity :baker; :foo :bar ].
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Attribution"]
    class_class_curie: ClassVar[str] = "prov:Attribution"
    class_name: ClassVar[str] = "prov_Attribution"
    class_model_uri: ClassVar[URIRef] = QO.ProvAttribution


@dataclass(repr=False)
class FoafAgent(OwlThing):
    """
    An agent (eg. person, group, software or physical artifact).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Agent"]
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "foaf_Agent"
    class_model_uri: ClassVar[URIRef] = QO.FoafAgent

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    prov_type: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    dcterms_hasPart: Optional[Union[Union[dict, OwlThing], list[Union[dict, OwlThing]]]] = empty_list()
    dcterms_isPartOf: Optional[Union[Union[dict, OwlThing], list[Union[dict, OwlThing]]]] = empty_list()
    prov_generatedAtTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    fhir_status: Optional[Union[Union[dict, "SarefPropertyValue"], list[Union[dict, "SarefPropertyValue"]]]] = empty_list()
    dcterms_creator: Optional[Union[Union[dict, "FoafAgent"], list[Union[dict, "FoafAgent"]]]] = empty_list()
    saref_hasProperty: Optional[Union[Union[dict, "SarefProperty"], list[Union[dict, "SarefProperty"]]]] = empty_list()
    saref_hasPropertyValue: Optional[Union[Union[dict, "SarefPropertyValue"], list[Union[dict, "SarefPropertyValue"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.prov_type, list):
            self.prov_type = [self.prov_type] if self.prov_type is not None else []
        self.prov_type = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.prov_type]

        if not isinstance(self.dcterms_hasPart, list):
            self.dcterms_hasPart = [self.dcterms_hasPart] if self.dcterms_hasPart is not None else []
        self.dcterms_hasPart = [v if isinstance(v, OwlThing) else OwlThing(**as_dict(v)) for v in self.dcterms_hasPart]

        if not isinstance(self.dcterms_isPartOf, list):
            self.dcterms_isPartOf = [self.dcterms_isPartOf] if self.dcterms_isPartOf is not None else []
        self.dcterms_isPartOf = [v if isinstance(v, OwlThing) else OwlThing(**as_dict(v)) for v in self.dcterms_isPartOf]

        if not isinstance(self.prov_generatedAtTime, list):
            self.prov_generatedAtTime = [self.prov_generatedAtTime] if self.prov_generatedAtTime is not None else []
        self.prov_generatedAtTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.prov_generatedAtTime]

        if not isinstance(self.fhir_status, list):
            self.fhir_status = [self.fhir_status] if self.fhir_status is not None else []
        self.fhir_status = [v if isinstance(v, SarefPropertyValue) else SarefPropertyValue(**as_dict(v)) for v in self.fhir_status]

        if not isinstance(self.dcterms_creator, list):
            self.dcterms_creator = [self.dcterms_creator] if self.dcterms_creator is not None else []
        self.dcterms_creator = [v if isinstance(v, FoafAgent) else FoafAgent(**as_dict(v)) for v in self.dcterms_creator]

        if not isinstance(self.saref_hasProperty, list):
            self.saref_hasProperty = [self.saref_hasProperty] if self.saref_hasProperty is not None else []
        self.saref_hasProperty = [v if isinstance(v, SarefProperty) else SarefProperty(**as_dict(v)) for v in self.saref_hasProperty]

        if not isinstance(self.saref_hasPropertyValue, list):
            self.saref_hasPropertyValue = [self.saref_hasPropertyValue] if self.saref_hasPropertyValue is not None else []
        self.saref_hasPropertyValue = [v if isinstance(v, SarefPropertyValue) else SarefPropertyValue(**as_dict(v)) for v in self.saref_hasPropertyValue]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FoafPerson(FoafAgent):
    """
    A person.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Person"]
    class_class_curie: ClassVar[str] = "foaf:Person"
    class_name: ClassVar[str] = "foaf_Person"
    class_model_uri: ClassVar[URIRef] = QO.FoafPerson

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None

@dataclass(repr=False)
class ProvOrganization(FoafAgent):
    """
    An organization is a social or legal institution such as a company, society, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Organization"]
    class_class_curie: ClassVar[str] = "prov:Organization"
    class_name: ClassVar[str] = "prov_Organization"
    class_model_uri: ClassVar[URIRef] = QO.ProvOrganization

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None

@dataclass(repr=False)
class SuloProcess(OwlThing):
    """
    a process is a entity that unfolds in time, has temporal parts, and has objects that participate in the process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SULO["Process"]
    class_class_curie: ClassVar[str] = "sulo:Process"
    class_name: ClassVar[str] = "sulo_Process"
    class_model_uri: ClassVar[URIRef] = QO.SuloProcess

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    prov_type: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    dcterms_hasPart: Optional[Union[Union[dict, OwlThing], list[Union[dict, OwlThing]]]] = empty_list()
    dcterms_isPartOf: Optional[Union[Union[dict, OwlThing], list[Union[dict, OwlThing]]]] = empty_list()
    fhir_status: Optional[Union[Union[dict, "SarefPropertyValue"], list[Union[dict, "SarefPropertyValue"]]]] = empty_list()
    dcterms_creator: Optional[Union[Union[dict, FoafAgent], list[Union[dict, FoafAgent]]]] = empty_list()
    saref_hasProperty: Optional[Union[Union[dict, "SarefProperty"], list[Union[dict, "SarefProperty"]]]] = empty_list()
    saref_hasPropertyValue: Optional[Union[Union[dict, "SarefPropertyValue"], list[Union[dict, "SarefPropertyValue"]]]] = empty_list()
    prov_startedAtTime: Optional[Union[str, XSDDateTime]] = None
    prov_endedAtTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.prov_type, list):
            self.prov_type = [self.prov_type] if self.prov_type is not None else []
        self.prov_type = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.prov_type]

        if not isinstance(self.dcterms_hasPart, list):
            self.dcterms_hasPart = [self.dcterms_hasPart] if self.dcterms_hasPart is not None else []
        self.dcterms_hasPart = [v if isinstance(v, OwlThing) else OwlThing(**as_dict(v)) for v in self.dcterms_hasPart]

        if not isinstance(self.dcterms_isPartOf, list):
            self.dcterms_isPartOf = [self.dcterms_isPartOf] if self.dcterms_isPartOf is not None else []
        self.dcterms_isPartOf = [v if isinstance(v, OwlThing) else OwlThing(**as_dict(v)) for v in self.dcterms_isPartOf]

        if not isinstance(self.fhir_status, list):
            self.fhir_status = [self.fhir_status] if self.fhir_status is not None else []
        self.fhir_status = [v if isinstance(v, SarefPropertyValue) else SarefPropertyValue(**as_dict(v)) for v in self.fhir_status]

        if not isinstance(self.dcterms_creator, list):
            self.dcterms_creator = [self.dcterms_creator] if self.dcterms_creator is not None else []
        self.dcterms_creator = [v if isinstance(v, FoafAgent) else FoafAgent(**as_dict(v)) for v in self.dcterms_creator]

        if not isinstance(self.saref_hasProperty, list):
            self.saref_hasProperty = [self.saref_hasProperty] if self.saref_hasProperty is not None else []
        self.saref_hasProperty = [v if isinstance(v, SarefProperty) else SarefProperty(**as_dict(v)) for v in self.saref_hasProperty]

        if not isinstance(self.saref_hasPropertyValue, list):
            self.saref_hasPropertyValue = [self.saref_hasPropertyValue] if self.saref_hasPropertyValue is not None else []
        self.saref_hasPropertyValue = [v if isinstance(v, SarefPropertyValue) else SarefPropertyValue(**as_dict(v)) for v in self.saref_hasPropertyValue]

        if self.prov_startedAtTime is not None and not isinstance(self.prov_startedAtTime, XSDDateTime):
            self.prov_startedAtTime = XSDDateTime(self.prov_startedAtTime)

        if self.prov_endedAtTime is not None and not isinstance(self.prov_endedAtTime, XSDDateTime):
            self.prov_endedAtTime = XSDDateTime(self.prov_endedAtTime)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class S4ehawActivity(SuloProcess):
    """
    The activity of a patient/user, i.e. daily and nocturnal activities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = S4EHAW["activity"]
    class_class_curie: ClassVar[str] = "s4ehaw:activity"
    class_name: ClassVar[str] = "s4ehaw_Activity"
    class_model_uri: ClassVar[URIRef] = QO.S4ehawActivity

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None

@dataclass(repr=False)
class FhirProcedure(SuloProcess):
    """
    An action that is being or was performed on an individual or entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Procedure"]
    class_class_curie: ClassVar[str] = "fhir:Procedure"
    class_name: ClassVar[str] = "fhir_Procedure"
    class_model_uri: ClassVar[URIRef] = QO.FhirProcedure

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None

@dataclass(repr=False)
class ProvEntity(OwlThing):
    """
    An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real
    or imaginary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "prov_Entity"
    class_model_uri: ClassVar[URIRef] = QO.ProvEntity

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    prov_wasAttributedTo: Optional[Union[Union[dict, FoafAgent], list[Union[dict, FoafAgent]]]] = empty_list()
    dcterms_created: Optional[Union[str, XSDDateTime]] = None
    dcterms_modified: Optional[Union[str, XSDDateTime]] = None
    prov_type: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    dcterms_hasPart: Optional[Union[Union[dict, OwlThing], list[Union[dict, OwlThing]]]] = empty_list()
    dcterms_isPartOf: Optional[Union[Union[dict, OwlThing], list[Union[dict, OwlThing]]]] = empty_list()
    prov_generatedAtTime: Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]] = empty_list()
    fhir_status: Optional[Union[Union[dict, "SarefPropertyValue"], list[Union[dict, "SarefPropertyValue"]]]] = empty_list()
    dcterms_creator: Optional[Union[Union[dict, FoafAgent], list[Union[dict, FoafAgent]]]] = empty_list()
    saref_hasProperty: Optional[Union[Union[dict, "SarefProperty"], list[Union[dict, "SarefProperty"]]]] = empty_list()
    saref_hasPropertyValue: Optional[Union[Union[dict, "SarefPropertyValue"], list[Union[dict, "SarefPropertyValue"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.prov_wasAttributedTo, list):
            self.prov_wasAttributedTo = [self.prov_wasAttributedTo] if self.prov_wasAttributedTo is not None else []
        self.prov_wasAttributedTo = [v if isinstance(v, FoafAgent) else FoafAgent(**as_dict(v)) for v in self.prov_wasAttributedTo]

        if self.dcterms_created is not None and not isinstance(self.dcterms_created, XSDDateTime):
            self.dcterms_created = XSDDateTime(self.dcterms_created)

        if self.dcterms_modified is not None and not isinstance(self.dcterms_modified, XSDDateTime):
            self.dcterms_modified = XSDDateTime(self.dcterms_modified)

        if not isinstance(self.prov_type, list):
            self.prov_type = [self.prov_type] if self.prov_type is not None else []
        self.prov_type = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.prov_type]

        if not isinstance(self.dcterms_hasPart, list):
            self.dcterms_hasPart = [self.dcterms_hasPart] if self.dcterms_hasPart is not None else []
        self.dcterms_hasPart = [v if isinstance(v, OwlThing) else OwlThing(**as_dict(v)) for v in self.dcterms_hasPart]

        if not isinstance(self.dcterms_isPartOf, list):
            self.dcterms_isPartOf = [self.dcterms_isPartOf] if self.dcterms_isPartOf is not None else []
        self.dcterms_isPartOf = [v if isinstance(v, OwlThing) else OwlThing(**as_dict(v)) for v in self.dcterms_isPartOf]

        if not isinstance(self.prov_generatedAtTime, list):
            self.prov_generatedAtTime = [self.prov_generatedAtTime] if self.prov_generatedAtTime is not None else []
        self.prov_generatedAtTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.prov_generatedAtTime]

        if not isinstance(self.fhir_status, list):
            self.fhir_status = [self.fhir_status] if self.fhir_status is not None else []
        self.fhir_status = [v if isinstance(v, SarefPropertyValue) else SarefPropertyValue(**as_dict(v)) for v in self.fhir_status]

        if not isinstance(self.dcterms_creator, list):
            self.dcterms_creator = [self.dcterms_creator] if self.dcterms_creator is not None else []
        self.dcterms_creator = [v if isinstance(v, FoafAgent) else FoafAgent(**as_dict(v)) for v in self.dcterms_creator]

        if not isinstance(self.saref_hasProperty, list):
            self.saref_hasProperty = [self.saref_hasProperty] if self.saref_hasProperty is not None else []
        self.saref_hasProperty = [v if isinstance(v, SarefProperty) else SarefProperty(**as_dict(v)) for v in self.saref_hasProperty]

        if not isinstance(self.saref_hasPropertyValue, list):
            self.saref_hasPropertyValue = [self.saref_hasPropertyValue] if self.saref_hasPropertyValue is not None else []
        self.saref_hasPropertyValue = [v if isinstance(v, SarefPropertyValue) else SarefPropertyValue(**as_dict(v)) for v in self.saref_hasPropertyValue]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SarefProperty(ProvEntity):
    """
    Identifiable qualities of features of interest that can be target of devices, such as observed or controlled. A
    property can apply to different features of interest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAREF["Property"]
    class_class_curie: ClassVar[str] = "saref:Property"
    class_name: ClassVar[str] = "saref_Property"
    class_model_uri: ClassVar[URIRef] = QO.SarefProperty

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    fhir_referenceRange: Optional[Union[dict, "FhirReferenceRange"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fhir_referenceRange is not None and not isinstance(self.fhir_referenceRange, FhirReferenceRange):
            self.fhir_referenceRange = FhirReferenceRange(**as_dict(self.fhir_referenceRange))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SarefPropertyValue(OwlThing):
    """
    Describes the value for a property. The property value is optionally linked to its value expressed as an RDF
    literal (DP saref:hasValue), optionally to the unit of measurement (OP saref:isMeasuredIn), and optionally to the
    properties or properties of interest it is a value of (OP saref:isValueOfProperty).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SAREF["PropertyValue"]
    class_class_curie: ClassVar[str] = "saref:PropertyValue"
    class_name: ClassVar[str] = "saref_PropertyValue"
    class_model_uri: ClassVar[URIRef] = QO.SarefPropertyValue

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    prov_atTime: Optional[Union[str, XSDDateTime]] = None
    saref_hasValue: Optional[str] = None
    saref_isValueOfProperty: Optional[Union[dict, SarefProperty]] = None
    fhir_valueReference: Optional[Union[str, URIorCURIE]] = None
    fhir_valueCodeableConcept: Optional[Union[dict, "ValueCoding"]] = None
    fhir_valueRange: Optional[Union[dict, "FhirReferenceRange"]] = None
    fhir_valueRatio: Optional[Union[dict, "FhirValueRatio"]] = None
    fhir_valuePeriod: Optional[Union[dict, "TimeInterval"]] = None
    fhir_valueAttachment: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.prov_atTime is not None and not isinstance(self.prov_atTime, XSDDateTime):
            self.prov_atTime = XSDDateTime(self.prov_atTime)

        if self.saref_hasValue is not None and not isinstance(self.saref_hasValue, str):
            self.saref_hasValue = str(self.saref_hasValue)

        if self.saref_isValueOfProperty is not None and not isinstance(self.saref_isValueOfProperty, SarefProperty):
            self.saref_isValueOfProperty = SarefProperty(**as_dict(self.saref_isValueOfProperty))

        if self.fhir_valueReference is not None and not isinstance(self.fhir_valueReference, URIorCURIE):
            self.fhir_valueReference = URIorCURIE(self.fhir_valueReference)

        if self.fhir_valueCodeableConcept is not None and not isinstance(self.fhir_valueCodeableConcept, ValueCoding):
            self.fhir_valueCodeableConcept = ValueCoding(**as_dict(self.fhir_valueCodeableConcept))

        if self.fhir_valueRange is not None and not isinstance(self.fhir_valueRange, FhirReferenceRange):
            self.fhir_valueRange = FhirReferenceRange(**as_dict(self.fhir_valueRange))

        if self.fhir_valueRatio is not None and not isinstance(self.fhir_valueRatio, FhirValueRatio):
            self.fhir_valueRatio = FhirValueRatio(**as_dict(self.fhir_valueRatio))

        if self.fhir_valuePeriod is not None and not isinstance(self.fhir_valuePeriod, TimeInterval):
            self.fhir_valuePeriod = TimeInterval(**as_dict(self.fhir_valuePeriod))

        if self.fhir_valueAttachment is not None and not isinstance(self.fhir_valueAttachment, URIorCURIE):
            self.fhir_valueAttachment = URIorCURIE(self.fhir_valueAttachment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(YAMLRoot):
    """
    A measured amount (or an amount that can potentially be measured).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Quantity"]
    class_class_curie: ClassVar[str] = "fhir:Quantity"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = QO.QuantityValue

    saref_isMeasuredIn: Optional[Union[str, URIorCURIE]] = None
    saref_hasValue: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.saref_isMeasuredIn is not None and not isinstance(self.saref_isMeasuredIn, URIorCURIE):
            self.saref_isMeasuredIn = URIorCURIE(self.saref_isMeasuredIn)

        if self.saref_hasValue is not None and not isinstance(self.saref_hasValue, str):
            self.saref_hasValue = str(self.saref_hasValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NumericalParams(YAMLRoot):
    """
    Parameters for quantitative values, including unit and precision.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PHRO["NumericalParams"]
    class_class_curie: ClassVar[str] = "phro:NumericalParams"
    class_name: ClassVar[str] = "NumericalParams"
    class_model_uri: ClassVar[URIRef] = QO.NumericalParams

    numericalUnit: Optional[Union[str, URIorCURIE]] = None
    numericalPrecision: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.numericalUnit is not None and not isinstance(self.numericalUnit, URIorCURIE):
            self.numericalUnit = URIorCURIE(self.numericalUnit)

        if self.numericalPrecision is not None and not isinstance(self.numericalPrecision, int):
            self.numericalPrecision = int(self.numericalPrecision)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValueCoding(YAMLRoot):
    """
    A coded value with a unique code for each display text, typically used for standardized questionnaires.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Coding"]
    class_class_curie: ClassVar[str] = "fhir:Coding"
    class_name: ClassVar[str] = "ValueCoding"
    class_model_uri: ClassVar[URIRef] = QO.ValueCoding

    code: str = None
    display: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, str):
            self.code = str(self.code)

        if self._is_empty(self.display):
            self.MissingRequiredField("display")
        if not isinstance(self.display, str):
            self.display = str(self.display)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FhirValueRatio(YAMLRoot):
    """
    A ratio of two Quantity values - a numerator and a denominator
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Ratio"]
    class_class_curie: ClassVar[str] = "fhir:Ratio"
    class_name: ClassVar[str] = "fhir_ValueRatio"
    class_model_uri: ClassVar[URIRef] = QO.FhirValueRatio

    numerator: Union[dict, QuantityValue] = None
    denominator: Union[dict, QuantityValue] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.numerator):
            self.MissingRequiredField("numerator")
        if not isinstance(self.numerator, QuantityValue):
            self.numerator = QuantityValue(**as_dict(self.numerator))

        if self._is_empty(self.denominator):
            self.MissingRequiredField("denominator")
        if not isinstance(self.denominator, QuantityValue):
            self.denominator = QuantityValue(**as_dict(self.denominator))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntervalParams(YAMLRoot):
    """
    Parameters for interval values, including minimum and maximum values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PHRO["IntervalParams"]
    class_class_curie: ClassVar[str] = "phro:IntervalParams"
    class_name: ClassVar[str] = "IntervalParams"
    class_model_uri: ClassVar[URIRef] = QO.IntervalParams

    minValue: Optional[float] = None
    minLabel: Optional[str] = None
    maxValue: Optional[float] = None
    maxLabel: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.minValue is not None and not isinstance(self.minValue, float):
            self.minValue = float(self.minValue)

        if self.minLabel is not None and not isinstance(self.minLabel, str):
            self.minLabel = str(self.minLabel)

        if self.maxValue is not None and not isinstance(self.maxValue, float):
            self.maxValue = float(self.maxValue)

        if self.maxLabel is not None and not isinstance(self.maxLabel, str):
            self.maxLabel = str(self.maxLabel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimeInterval(YAMLRoot):
    """
    A temporal entity with an extent or duration
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME["Interval"]
    class_class_curie: ClassVar[str] = "time:Interval"
    class_name: ClassVar[str] = "time_Interval"
    class_model_uri: ClassVar[URIRef] = QO.TimeInterval

    prov_startedAtTime: Optional[Union[str, XSDDateTime]] = None
    prov_endedAtTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.prov_startedAtTime is not None and not isinstance(self.prov_startedAtTime, XSDDateTime):
            self.prov_startedAtTime = XSDDateTime(self.prov_startedAtTime)

        if self.prov_endedAtTime is not None and not isinstance(self.prov_endedAtTime, XSDDateTime):
            self.prov_endedAtTime = XSDDateTime(self.prov_endedAtTime)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimeDuration(YAMLRoot):
    """
    Duration of a temporal extent expressed as a decimal number scaled by a temporal unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME["Duration"]
    class_class_curie: ClassVar[str] = "time:Duration"
    class_name: ClassVar[str] = "time_Duration"
    class_model_uri: ClassVar[URIRef] = QO.TimeDuration

    saref_hasValue: Optional[str] = None
    saref_isMeasuredIn: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.saref_hasValue is not None and not isinstance(self.saref_hasValue, str):
            self.saref_hasValue = str(self.saref_hasValue)

        if self.saref_isMeasuredIn is not None and not isinstance(self.saref_isMeasuredIn, URIorCURIE):
            self.saref_isMeasuredIn = URIorCURIE(self.saref_isMeasuredIn)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FhirReferenceRange(YAMLRoot):
    """
    Guidance on how to interpret the value by comparison to a normal or recommended range. Multiple reference ranges
    are interpreted as an 'OR'. In other words, to represent two distinct target populations, two referenceRange
    elements would be used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Observation.referenceRange"]
    class_class_curie: ClassVar[str] = "fhir:Observation.referenceRange"
    class_name: ClassVar[str] = "fhir_ReferenceRange"
    class_model_uri: ClassVar[URIRef] = QO.FhirReferenceRange

    lowRange: Optional[Union[dict, QuantityValue]] = None
    highRange: Optional[Union[dict, QuantityValue]] = None
    normalValue: Optional[Union[Union[dict, QuantityValue], list[Union[dict, QuantityValue]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.lowRange is not None and not isinstance(self.lowRange, QuantityValue):
            self.lowRange = QuantityValue(**as_dict(self.lowRange))

        if self.highRange is not None and not isinstance(self.highRange, QuantityValue):
            self.highRange = QuantityValue(**as_dict(self.highRange))

        if not isinstance(self.normalValue, list):
            self.normalValue = [self.normalValue] if self.normalValue is not None else []
        self.normalValue = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.normalValue]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QoQuestionnaire(ProvEntity):
    """
    A structured, reusable instrument or template composed of ordered items designed to collect standardized
    information from an individual or system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QO["Questionnaire"]
    class_class_curie: ClassVar[str] = "qo:Questionnaire"
    class_name: ClassVar[str] = "qo_Questionnaire"
    class_model_uri: ClassVar[URIRef] = QO.QoQuestionnaire

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    dcterms_created: Union[str, XSDDateTime] = None
    dcterms_modified: Union[str, XSDDateTime] = None
    dcterms_creator: Union[Union[dict, ProvOrganization], list[Union[dict, ProvOrganization]]] = None
    fhir_status: Union[Union[dict, "QoQuestionnaireStatus"], list[Union[dict, "QoQuestionnaireStatus"]]] = None
    qo_hasOrderedQuestion: Optional[Union[Union[dict, "QoOrderedQuestion"], list[Union[dict, "QoOrderedQuestion"]]]] = empty_list()
    qo_hasOrderedSection: Optional[Union[Union[dict, "QoOrderedSection"], list[Union[dict, "QoOrderedSection"]]]] = empty_list()
    dcterms_isPartOf: Optional[Union[Union[dict, SuloProcess], list[Union[dict, SuloProcess]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.dcterms_created):
            self.MissingRequiredField("dcterms_created")
        if not isinstance(self.dcterms_created, XSDDateTime):
            self.dcterms_created = XSDDateTime(self.dcterms_created)

        if self._is_empty(self.dcterms_modified):
            self.MissingRequiredField("dcterms_modified")
        if not isinstance(self.dcterms_modified, XSDDateTime):
            self.dcterms_modified = XSDDateTime(self.dcterms_modified)

        if self._is_empty(self.dcterms_creator):
            self.MissingRequiredField("dcterms_creator")
        if not isinstance(self.dcterms_creator, list):
            self.dcterms_creator = [self.dcterms_creator] if self.dcterms_creator is not None else []
        self.dcterms_creator = [v if isinstance(v, ProvOrganization) else ProvOrganization(**as_dict(v)) for v in self.dcterms_creator]

        if self._is_empty(self.fhir_status):
            self.MissingRequiredField("fhir_status")
        if not isinstance(self.fhir_status, list):
            self.fhir_status = [self.fhir_status] if self.fhir_status is not None else []
        self.fhir_status = [v if isinstance(v, QoQuestionnaireStatus) else QoQuestionnaireStatus(**as_dict(v)) for v in self.fhir_status]

        if not isinstance(self.qo_hasOrderedQuestion, list):
            self.qo_hasOrderedQuestion = [self.qo_hasOrderedQuestion] if self.qo_hasOrderedQuestion is not None else []
        self.qo_hasOrderedQuestion = [v if isinstance(v, QoOrderedQuestion) else QoOrderedQuestion(**as_dict(v)) for v in self.qo_hasOrderedQuestion]

        if not isinstance(self.qo_hasOrderedSection, list):
            self.qo_hasOrderedSection = [self.qo_hasOrderedSection] if self.qo_hasOrderedSection is not None else []
        self.qo_hasOrderedSection = [v if isinstance(v, QoOrderedSection) else QoOrderedSection(**as_dict(v)) for v in self.qo_hasOrderedSection]

        if not isinstance(self.dcterms_isPartOf, list):
            self.dcterms_isPartOf = [self.dcterms_isPartOf] if self.dcterms_isPartOf is not None else []
        self.dcterms_isPartOf = [v if isinstance(v, SuloProcess) else SuloProcess(**as_dict(v)) for v in self.dcterms_isPartOf]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QoQuestionnaireStatus(SarefPropertyValue):
    """
    Defines the lifecycle state governing the operational readiness and availability of a survey template.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QO["QuestionnaireStatus"]
    class_class_curie: ClassVar[str] = "qo:QuestionnaireStatus"
    class_name: ClassVar[str] = "qo_QuestionnaireStatus"
    class_model_uri: ClassVar[URIRef] = QO.QoQuestionnaireStatus

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    saref_hasValue: Union[str, "QoQuestionnaireStatusEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.saref_hasValue):
            self.MissingRequiredField("saref_hasValue")
        if not isinstance(self.saref_hasValue, QoQuestionnaireStatusEnum):
            self.saref_hasValue = QoQuestionnaireStatusEnum(self.saref_hasValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QoOrderedSection(ProvEntity):
    """
    A contextual wrapper that binds a thematic grouping of inquiry items to a specific sequence index within a survey
    template or parent group.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QO["OrderedSection"]
    class_class_curie: ClassVar[str] = "qo:OrderedSection"
    class_name: ClassVar[str] = "qo_OrderedSection"
    class_model_uri: ClassVar[URIRef] = QO.QoOrderedSection

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    qo_section: Union[dict, "QoSection"] = None
    qo_order: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.qo_section):
            self.MissingRequiredField("qo_section")
        if not isinstance(self.qo_section, QoSection):
            self.qo_section = QoSection(**as_dict(self.qo_section))

        if self._is_empty(self.qo_order):
            self.MissingRequiredField("qo_order")
        if not isinstance(self.qo_order, int):
            self.qo_order = int(self.qo_order)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QoSection(ProvEntity):
    """
    A logical grouping or thematic partition of items within a structured survey instrument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QO["Section"]
    class_class_curie: ClassVar[str] = "qo:Section"
    class_name: ClassVar[str] = "qo_Section"
    class_model_uri: ClassVar[URIRef] = QO.QoSection

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    dcterms_creator: Union[Union[dict, ProvOrganization], list[Union[dict, ProvOrganization]]] = None
    qo_hasOrderedQuestion: Optional[Union[Union[dict, "QoOrderedQuestion"], list[Union[dict, "QoOrderedQuestion"]]]] = empty_list()
    qo_hasOrderedSection: Optional[Union[Union[dict, QoOrderedSection], list[Union[dict, QoOrderedSection]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.dcterms_creator):
            self.MissingRequiredField("dcterms_creator")
        if not isinstance(self.dcterms_creator, list):
            self.dcterms_creator = [self.dcterms_creator] if self.dcterms_creator is not None else []
        self.dcterms_creator = [v if isinstance(v, ProvOrganization) else ProvOrganization(**as_dict(v)) for v in self.dcterms_creator]

        if not isinstance(self.qo_hasOrderedQuestion, list):
            self.qo_hasOrderedQuestion = [self.qo_hasOrderedQuestion] if self.qo_hasOrderedQuestion is not None else []
        self.qo_hasOrderedQuestion = [v if isinstance(v, QoOrderedQuestion) else QoOrderedQuestion(**as_dict(v)) for v in self.qo_hasOrderedQuestion]

        if not isinstance(self.qo_hasOrderedSection, list):
            self.qo_hasOrderedSection = [self.qo_hasOrderedSection] if self.qo_hasOrderedSection is not None else []
        self.qo_hasOrderedSection = [v if isinstance(v, QoOrderedSection) else QoOrderedSection(**as_dict(v)) for v in self.qo_hasOrderedSection]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QoOrderedQuestion(ProvEntity):
    """
    A contextual wrapper that binds an inquiry item to a specific sequence index within a survey template or parent
    group.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QO["OrderedQuestion"]
    class_class_curie: ClassVar[str] = "qo:OrderedQuestion"
    class_name: ClassVar[str] = "qo_OrderedQuestion"
    class_model_uri: ClassVar[URIRef] = QO.QoOrderedQuestion

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    qo_question: Union[dict, "QoQuestion"] = None
    qo_temporalValidity: Union[dict, TimeDuration] = None
    qo_order: int = None
    qo_required: Union[bool, Bool] = None
    qo_hardValidity: Optional[Union[bool, Bool]] = False
    qo_conditionalValidity: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.qo_question):
            self.MissingRequiredField("qo_question")
        if not isinstance(self.qo_question, QoQuestion):
            self.qo_question = QoQuestion(**as_dict(self.qo_question))

        if self._is_empty(self.qo_temporalValidity):
            self.MissingRequiredField("qo_temporalValidity")
        if not isinstance(self.qo_temporalValidity, TimeDuration):
            self.qo_temporalValidity = TimeDuration(**as_dict(self.qo_temporalValidity))

        if self._is_empty(self.qo_order):
            self.MissingRequiredField("qo_order")
        if not isinstance(self.qo_order, int):
            self.qo_order = int(self.qo_order)

        if self._is_empty(self.qo_required):
            self.MissingRequiredField("qo_required")
        if not isinstance(self.qo_required, Bool):
            self.qo_required = Bool(self.qo_required)

        if self.qo_hardValidity is not None and not isinstance(self.qo_hardValidity, Bool):
            self.qo_hardValidity = Bool(self.qo_hardValidity)

        if self.qo_conditionalValidity is not None and not isinstance(self.qo_conditionalValidity, str):
            self.qo_conditionalValidity = str(self.qo_conditionalValidity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QoQuestion(ProvEntity):
    """
    An individual inquiry item within an instrument that specifies an information requirement and constrains the
    acceptable response format.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QO["Question"]
    class_class_curie: ClassVar[str] = "qo:Question"
    class_name: ClassVar[str] = "qo_Question"
    class_model_uri: ClassVar[URIRef] = QO.QoQuestion

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    qo_tag: Union[str, list[str]] = None
    prov_type: Union[Union[str, "QoQuestionType"], list[Union[str, "QoQuestionType"]]] = None
    dcterms_creator: Union[Union[dict, ProvOrganization], list[Union[dict, ProvOrganization]]] = None
    qo_multivalued: Optional[Union[bool, Bool]] = False
    qo_numericalParams: Optional[Union[dict, NumericalParams]] = None
    qo_codingParams: Optional[Union[Union[dict, ValueCoding], list[Union[dict, ValueCoding]]]] = empty_list()
    qo_codingOrdinal: Optional[Union[bool, Bool]] = False
    qo_intervalParams: Optional[Union[dict, IntervalParams]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.qo_tag):
            self.MissingRequiredField("qo_tag")
        if not isinstance(self.qo_tag, list):
            self.qo_tag = [self.qo_tag] if self.qo_tag is not None else []
        self.qo_tag = [v if isinstance(v, str) else str(v) for v in self.qo_tag]

        if self._is_empty(self.prov_type):
            self.MissingRequiredField("prov_type")
        if not isinstance(self.prov_type, list):
            self.prov_type = [self.prov_type] if self.prov_type is not None else []
        self.prov_type = [v if isinstance(v, QoQuestionType) else QoQuestionType(v) for v in self.prov_type]

        if self._is_empty(self.dcterms_creator):
            self.MissingRequiredField("dcterms_creator")
        if not isinstance(self.dcterms_creator, list):
            self.dcterms_creator = [self.dcterms_creator] if self.dcterms_creator is not None else []
        self.dcterms_creator = [v if isinstance(v, ProvOrganization) else ProvOrganization(**as_dict(v)) for v in self.dcterms_creator]

        if self.qo_multivalued is not None and not isinstance(self.qo_multivalued, Bool):
            self.qo_multivalued = Bool(self.qo_multivalued)

        if self.qo_numericalParams is not None and not isinstance(self.qo_numericalParams, NumericalParams):
            self.qo_numericalParams = NumericalParams(**as_dict(self.qo_numericalParams))

        if not isinstance(self.qo_codingParams, list):
            self.qo_codingParams = [self.qo_codingParams] if self.qo_codingParams is not None else []
        self.qo_codingParams = [v if isinstance(v, ValueCoding) else ValueCoding(**as_dict(v)) for v in self.qo_codingParams]

        if self.qo_codingOrdinal is not None and not isinstance(self.qo_codingOrdinal, Bool):
            self.qo_codingOrdinal = Bool(self.qo_codingOrdinal)

        if self.qo_intervalParams is not None and not isinstance(self.qo_intervalParams, IntervalParams):
            self.qo_intervalParams = IntervalParams(**as_dict(self.qo_intervalParams))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QoQuestionnaireResponse(ProvEntity):
    """
    A completed or partially completed instance containing recorded values collected from a specific execution of a
    survey instrument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QO["QuestionnaireResponse"]
    class_class_curie: ClassVar[str] = "qo:QuestionnaireResponse"
    class_name: ClassVar[str] = "qo_QuestionnaireResponse"
    class_model_uri: ClassVar[URIRef] = QO.QoQuestionnaireResponse

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    qo_responds: Union[dict, QoQuestionnaire] = None
    qo_hasAnswer: Union[Union[dict, "QoAnswer"], list[Union[dict, "QoAnswer"]]] = None
    dcterms_created: Union[str, XSDDateTime] = None
    dcterms_modified: Union[str, XSDDateTime] = None
    prov_wasAttributedTo: Union[Union[dict, FoafPerson], list[Union[dict, FoafPerson]]] = None
    fhir_status: Union[Union[dict, "QoQuestionnaireResponseStatus"], list[Union[dict, "QoQuestionnaireResponseStatus"]]] = None
    dcterms_isPartOf: Optional[Union[Union[dict, SuloProcess], list[Union[dict, SuloProcess]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.qo_responds):
            self.MissingRequiredField("qo_responds")
        if not isinstance(self.qo_responds, QoQuestionnaire):
            self.qo_responds = QoQuestionnaire(**as_dict(self.qo_responds))

        if self._is_empty(self.qo_hasAnswer):
            self.MissingRequiredField("qo_hasAnswer")
        if not isinstance(self.qo_hasAnswer, list):
            self.qo_hasAnswer = [self.qo_hasAnswer] if self.qo_hasAnswer is not None else []
        self.qo_hasAnswer = [v if isinstance(v, QoAnswer) else QoAnswer(**as_dict(v)) for v in self.qo_hasAnswer]

        if self._is_empty(self.dcterms_created):
            self.MissingRequiredField("dcterms_created")
        if not isinstance(self.dcterms_created, XSDDateTime):
            self.dcterms_created = XSDDateTime(self.dcterms_created)

        if self._is_empty(self.dcterms_modified):
            self.MissingRequiredField("dcterms_modified")
        if not isinstance(self.dcterms_modified, XSDDateTime):
            self.dcterms_modified = XSDDateTime(self.dcterms_modified)

        if self._is_empty(self.prov_wasAttributedTo):
            self.MissingRequiredField("prov_wasAttributedTo")
        if not isinstance(self.prov_wasAttributedTo, list):
            self.prov_wasAttributedTo = [self.prov_wasAttributedTo] if self.prov_wasAttributedTo is not None else []
        self.prov_wasAttributedTo = [v if isinstance(v, FoafPerson) else FoafPerson(**as_dict(v)) for v in self.prov_wasAttributedTo]

        if self._is_empty(self.fhir_status):
            self.MissingRequiredField("fhir_status")
        if not isinstance(self.fhir_status, list):
            self.fhir_status = [self.fhir_status] if self.fhir_status is not None else []
        self.fhir_status = [v if isinstance(v, QoQuestionnaireResponseStatus) else QoQuestionnaireResponseStatus(**as_dict(v)) for v in self.fhir_status]

        if not isinstance(self.dcterms_isPartOf, list):
            self.dcterms_isPartOf = [self.dcterms_isPartOf] if self.dcterms_isPartOf is not None else []
        self.dcterms_isPartOf = [v if isinstance(v, SuloProcess) else SuloProcess(**as_dict(v)) for v in self.dcterms_isPartOf]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QoQuestionnaireResponseStatus(SarefPropertyValue):
    """
    Defines the lifecycle state governing the operational readiness and availability of a completed or partially
    completed instance containing recorded values collected from a specific execution of a survey instrument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QO["QuestionnaireResponseStatus"]
    class_class_curie: ClassVar[str] = "qo:QuestionnaireResponseStatus"
    class_name: ClassVar[str] = "qo_QuestionnaireResponseStatus"
    class_model_uri: ClassVar[URIRef] = QO.QoQuestionnaireResponseStatus

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    saref_hasValue: Union[str, "QoQuestionnaireResponseStatusEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.saref_hasValue):
            self.MissingRequiredField("saref_hasValue")
        if not isinstance(self.saref_hasValue, QoQuestionnaireResponseStatusEnum):
            self.saref_hasValue = QoQuestionnaireResponseStatusEnum(self.saref_hasValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QoAnswer(ProvEntity):
    """
    A recorded value, or selection provided in response to a specific inquiry item.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QO["Answer"]
    class_class_curie: ClassVar[str] = "qo:Answer"
    class_name: ClassVar[str] = "qo_Answer"
    class_model_uri: ClassVar[URIRef] = QO.QoAnswer

    rdfs_label: Union[str, list[str]] = None
    rdfs_comment: Union[str, list[str]] = None
    qo_toQuestion: Union[dict, QoQuestion] = None
    prov_generatedAtTime: Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]] = None
    qo_answerValue: Optional[str] = None
    qo_isEmpty: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.qo_toQuestion):
            self.MissingRequiredField("qo_toQuestion")
        if not isinstance(self.qo_toQuestion, QoQuestion):
            self.qo_toQuestion = QoQuestion(**as_dict(self.qo_toQuestion))

        if self._is_empty(self.prov_generatedAtTime):
            self.MissingRequiredField("prov_generatedAtTime")
        if not isinstance(self.prov_generatedAtTime, list):
            self.prov_generatedAtTime = [self.prov_generatedAtTime] if self.prov_generatedAtTime is not None else []
        self.prov_generatedAtTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.prov_generatedAtTime]

        if self.qo_answerValue is not None and not isinstance(self.qo_answerValue, str):
            self.qo_answerValue = str(self.qo_answerValue)

        if self.qo_isEmpty is not None and not isinstance(self.qo_isEmpty, Bool):
            self.qo_isEmpty = Bool(self.qo_isEmpty)

        super().__post_init__(**kwargs)


# Enumerations
class QoQuestionType(EnumDefinitionImpl):
    """
    Specifies the structural classification and data-type constraints governing acceptable inputs for an inquiry item.
    """
    choice = PermissibleValue(
        text="choice",
        description="An inquiry format offering a fixed set of standardized coded options for selection.",
        meaning=FHIR["item-type#coding"])
    openChoice = PermissibleValue(
        text="openChoice",
        description="""A question with predefined options to select from plus a last valueCoding: {'code': '-1', 'display': 'Other'} that allows text input. Multiple selection may be allowed.""",
        meaning=QO["open-choice"])
    numberInterval = PermissibleValue(
        text="numberInterval",
        description="A question that expects a numeric answer in between a minimum and maximum value.",
        meaning=QO["numberInterval"])
    decimal = PermissibleValue(
        text="decimal",
        description="A question that expects a numerical answer, either integer or float.",
        meaning=FHIR["item-type#decimal"])
    time = PermissibleValue(
        text="time",
        description="""An inquiry item constraining acceptable input strictly to a clock time (hour, minute, second) without a date component.""",
        meaning=FHIR["item-type#time"])
    dateTime = PermissibleValue(
        text="dateTime",
        description="""An inquiry item constraining acceptable input strictly to a date and time, formatted as YYYY-MM-DDThh:mm:ss+zz:zz.""",
        meaning=FHIR["item-type#dateTime"])
    text = PermissibleValue(
        text="text",
        description="An inquiry item that expects a free string answer.",
        meaning=FHIR["item-type#string"])

    _defn = EnumDefinition(
        name="QoQuestionType",
        description="""Specifies the structural classification and data-type constraints governing acceptable inputs for an inquiry item.""",
    )

class QoQuestionnaireStatusEnum(EnumDefinitionImpl):
    """
    Questionnaires must have one of the following status (FHIR inspired):
    """
    draft = PermissibleValue(
        text="draft",
        description="This resource is still under development and is not yet considered to be ready for normal use.",
        meaning=FHIR["resource-status-draft"])
    active = PermissibleValue(
        text="active",
        description="This resource is ready for normal use.",
        meaning=FHIR["resource-status-active"])
    retired = PermissibleValue(
        text="retired",
        description="This resource has been withdrawn or superseded and should no longer be used.",
        meaning=FHIR["resource-status-retired"])
    unknown = PermissibleValue(
        text="unknown",
        description="""The authoring system does not know which of the status values currently applies for this resource. Note: This concept is not to be used for 'other' - one of the listed statuses is presumed to apply, it's just not known which one.""",
        meaning=FHIR["resource-status-unknown"])

    _defn = EnumDefinition(
        name="QoQuestionnaireStatusEnum",
        description="Questionnaires must have one of the following status (FHIR inspired):",
    )

class QoQuestionnaireResponseStatusEnum(EnumDefinitionImpl):
    """
    The questionnaire response status must be one of the following: 'in-progress', 'completed', 'amended',
    'entered-in-error' or 'stopped'.
    """
    in_progress = PermissibleValue(
        text="in_progress",
        description="""This QuestionnaireResponse has been partially filled out with answers but changes or additions are still expected to be made to it.""",
        meaning=FHIR["questionnaire-answers-status-in-progress"])
    completed = PermissibleValue(
        text="completed",
        description="""This QuestionnaireResponse has been filled out with answers and the current content is regarded as definitive.""",
        meaning=FHIR["questionnaire-answers-status-completed"])
    amended = PermissibleValue(
        text="amended",
        description="""This QuestionnaireResponse has been filled out with answers, then marked as complete, yet changes or additions have been made to it afterwards.""",
        meaning=FHIR["questionnaire-answers-status-amended"])
    entered_in_error = PermissibleValue(
        text="entered_in_error",
        description="This QuestionnaireResponse was entered in error and voided.",
        meaning=FHIR["questionnaire-answers-status-entered-in-error"])
    stopped = PermissibleValue(
        text="stopped",
        description="""This QuestionnaireResponse has been partially filled out with answers but has been abandoned. No subsequent changes can be made.""",
        meaning=FHIR["questionnaire-answers-status-stopped"])

    _defn = EnumDefinition(
        name="QoQuestionnaireResponseStatusEnum",
        description="""The questionnaire response status must be one of the following: 'in-progress', 'completed', 'amended', 'entered-in-error' or 'stopped'.""",
    )

# Slots
class slots:
    pass

slots.rdfs_label = Slot(uri=RDFS.label, name="rdfs_label", curie=RDFS.curie('label'),
                   model_uri=QO.rdfs_label, domain=OwlThing, range=Union[str, list[str]])

slots.rdfs_comment = Slot(uri=RDFS.comment, name="rdfs_comment", curie=RDFS.curie('comment'),
                   model_uri=QO.rdfs_comment, domain=OwlThing, range=Union[str, list[str]])

slots.owl_versionInfo = Slot(uri=OWL.versionInfo, name="owl_versionInfo", curie=OWL.curie('versionInfo'),
                   model_uri=QO.owl_versionInfo, domain=OwlThing, range=Optional[str])

slots.dcterms_isPartOf = Slot(uri=DCTERMS.isPartOf, name="dcterms_isPartOf", curie=DCTERMS.curie('isPartOf'),
                   model_uri=QO.dcterms_isPartOf, domain=None, range=Optional[Union[Union[dict, OwlThing], list[Union[dict, OwlThing]]]])

slots.dcterms_hasPart = Slot(uri=DCTERMS.hasPart, name="dcterms_hasPart", curie=DCTERMS.curie('hasPart'),
                   model_uri=QO.dcterms_hasPart, domain=None, range=Optional[Union[Union[dict, OwlThing], list[Union[dict, OwlThing]]]])

slots.prov_type = Slot(uri=PROV.type, name="prov_type", curie=PROV.curie('type'),
                   model_uri=QO.prov_type, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.fhir_status = Slot(uri=FHIR['resource-status'], name="fhir_status", curie=FHIR.curie('resource-status'),
                   model_uri=QO.fhir_status, domain=None, range=Optional[Union[Union[dict, SarefPropertyValue], list[Union[dict, SarefPropertyValue]]]])

slots.dcterms_creator = Slot(uri=DCTERMS.creator, name="dcterms_creator", curie=DCTERMS.curie('creator'),
                   model_uri=QO.dcterms_creator, domain=None, range=Optional[Union[Union[dict, FoafAgent], list[Union[dict, FoafAgent]]]])

slots.saref_hasProperty = Slot(uri=SAREF.hasProperty, name="saref_hasProperty", curie=SAREF.curie('hasProperty'),
                   model_uri=QO.saref_hasProperty, domain=None, range=Optional[Union[Union[dict, SarefProperty], list[Union[dict, SarefProperty]]]], mappings = [SSN["hasProperty"]])

slots.saref_hasPropertyValue = Slot(uri=SAREF.hasPropertyValue, name="saref_hasPropertyValue", curie=SAREF.curie('hasPropertyValue'),
                   model_uri=QO.saref_hasPropertyValue, domain=None, range=Optional[Union[Union[dict, SarefPropertyValue], list[Union[dict, SarefPropertyValue]]]])

slots.prov_hadPrimarySource = Slot(uri=PROV.hadPrimarySource, name="prov_hadPrimarySource", curie=PROV.curie('hadPrimarySource'),
                   model_uri=QO.prov_hadPrimarySource, domain=OwlThing, range=Optional[Union[Union[dict, "ProvEntity"], list[Union[dict, "ProvEntity"]]]])

slots.prov_wasGeneratedBy = Slot(uri=PROV.wasGeneratedBy, name="prov_wasGeneratedBy", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=QO.prov_wasGeneratedBy, domain=OwlThing, range=Optional[Union[Union[dict, "SuloProcess"], list[Union[dict, "SuloProcess"]]]])

slots.prov_generatedAtTime = Slot(uri=PROV.generatedAtTime, name="prov_generatedAtTime", curie=PROV.curie('generatedAtTime'),
                   model_uri=QO.prov_generatedAtTime, domain=None, range=Optional[Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]]])

slots.prov_generated = Slot(uri=PROV.generated, name="prov_generated", curie=PROV.curie('generated'),
                   model_uri=QO.prov_generated, domain=SuloProcess, range=Optional[Union[Union[dict, OwlThing], list[Union[dict, OwlThing]]]])

slots.prov_wasAttributedTo = Slot(uri=PROV.wasAttributedTo, name="prov_wasAttributedTo", curie=PROV.curie('wasAttributedTo'),
                   model_uri=QO.prov_wasAttributedTo, domain=ProvEntity, range=Optional[Union[Union[dict, FoafAgent], list[Union[dict, FoafAgent]]]])

slots.prov_qualifiedAttribution = Slot(uri=PROV.qualifiedAttribution, name="prov_qualifiedAttribution", curie=PROV.curie('qualifiedAttribution'),
                   model_uri=QO.prov_qualifiedAttribution, domain=ProvEntity, range=Optional[Union[Union[dict, ProvAttribution], list[Union[dict, ProvAttribution]]]])

slots.prov_startedAtTime = Slot(uri=PROV.startedAtTime, name="prov_startedAtTime", curie=PROV.curie('startedAtTime'),
                   model_uri=QO.prov_startedAtTime, domain=SuloProcess, range=Optional[Union[str, XSDDateTime]])

slots.prov_endedAtTime = Slot(uri=PROV.endedAtTime, name="prov_endedAtTime", curie=PROV.curie('endedAtTime'),
                   model_uri=QO.prov_endedAtTime, domain=SuloProcess, range=Optional[Union[str, XSDDateTime]])

slots.prov_atTime = Slot(uri=PROV.atTime, name="prov_atTime", curie=PROV.curie('atTime'),
                   model_uri=QO.prov_atTime, domain=SuloProcess, range=Optional[Union[str, XSDDateTime]], mappings = [SAREF["hasTimestamp"], FHIR["DeviceMetric.calibration.time"], SOSA["phenomenonTime"]])

slots.time_hasDuration = Slot(uri=TIME.hasDuration, name="time_hasDuration", curie=TIME.curie('hasDuration'),
                   model_uri=QO.time_hasDuration, domain=None, range=Optional[Union[dict, TimeDuration]], mappings = [SPHN["hasDuration"]])

slots.dcterms_created = Slot(uri=DCTERMS.created, name="dcterms_created", curie=DCTERMS.curie('created'),
                   model_uri=QO.dcterms_created, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dcterms_modified = Slot(uri=DCTERMS.modified, name="dcterms_modified", curie=DCTERMS.curie('modified'),
                   model_uri=QO.dcterms_modified, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.saref_isValueOfProperty = Slot(uri=SAREF.isValueOfProperty, name="saref_isValueOfProperty", curie=SAREF.curie('isValueOfProperty'),
                   model_uri=QO.saref_isValueOfProperty, domain=SarefPropertyValue, range=Optional[Union[dict, SarefProperty]])

slots.saref_isMeasuredIn = Slot(uri=SAREF.isMeasuredIn, name="saref_isMeasuredIn", curie=SAREF.curie('isMeasuredIn'),
                   model_uri=QO.saref_isMeasuredIn, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^ucum:'))

slots.fhir_valueReference = Slot(uri=FHIR.valueReference, name="fhir_valueReference", curie=FHIR.curie('valueReference'),
                   model_uri=QO.fhir_valueReference, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.saref_hasValue = Slot(uri=SAREF.hasValue, name="saref_hasValue", curie=SAREF.curie('hasValue'),
                   model_uri=QO.saref_hasValue, domain=None, range=Optional[str])

slots.s4ehaw_minimumValue = Slot(uri=S4EHAW.minimumValue, name="s4ehaw_minimumValue", curie=S4EHAW.curie('minimumValue'),
                   model_uri=QO.s4ehaw_minimumValue, domain=None, range=Optional[float])

slots.s4ehaw_maximumValue = Slot(uri=S4EHAW.maximumValue, name="s4ehaw_maximumValue", curie=S4EHAW.curie('maximumValue'),
                   model_uri=QO.s4ehaw_maximumValue, domain=None, range=Optional[float])

slots.qo_multivalued = Slot(uri=QO.multivalued, name="qo_multivalued", curie=QO.curie('multivalued'),
                   model_uri=QO.qo_multivalued, domain=None, range=Optional[Union[bool, Bool]])

slots.qo_order = Slot(uri=QO.order, name="qo_order", curie=QO.curie('order'),
                   model_uri=QO.qo_order, domain=None, range=int)

slots.qo_hardValidity = Slot(uri=QO.hardValidity, name="qo_hardValidity", curie=QO.curie('hardValidity'),
                   model_uri=QO.qo_hardValidity, domain=None, range=Optional[Union[bool, Bool]])

slots.qo_temporalValidity = Slot(uri=QO.temporalValidity, name="qo_temporalValidity", curie=QO.curie('temporalValidity'),
                   model_uri=QO.qo_temporalValidity, domain=None, range=Union[dict, TimeDuration])

slots.qo_conditionalValidity = Slot(uri=QO.conditionalValidity, name="qo_conditionalValidity", curie=QO.curie('conditionalValidity'),
                   model_uri=QO.qo_conditionalValidity, domain=None, range=Optional[str])

slots.qo_question = Slot(uri=QO.question, name="qo_question", curie=QO.curie('question'),
                   model_uri=QO.qo_question, domain=QoOrderedQuestion, range=Union[dict, "QoQuestion"])

slots.qo_hasOrderedQuestion = Slot(uri=QO.hasOrderedQuestion, name="qo_hasOrderedQuestion", curie=QO.curie('hasOrderedQuestion'),
                   model_uri=QO.qo_hasOrderedQuestion, domain=None, range=Optional[Union[Union[dict, QoOrderedQuestion], list[Union[dict, QoOrderedQuestion]]]])

slots.qo_hasOrderedSection = Slot(uri=QO.hasOrderedSection, name="qo_hasOrderedSection", curie=QO.curie('hasOrderedSection'),
                   model_uri=QO.qo_hasOrderedSection, domain=None, range=Optional[Union[Union[dict, QoOrderedSection], list[Union[dict, QoOrderedSection]]]])

slots.qo_section = Slot(uri=QO.section, name="qo_section", curie=QO.curie('section'),
                   model_uri=QO.qo_section, domain=QoOrderedSection, range=Union[dict, "QoSection"])

slots.qo_responds = Slot(uri=QO.responds, name="qo_responds", curie=QO.curie('responds'),
                   model_uri=QO.qo_responds, domain=QoQuestionnaireResponse, range=Union[dict, QoQuestionnaire])

slots.qo_hasAnswer = Slot(uri=QO.hasAnswer, name="qo_hasAnswer", curie=QO.curie('hasAnswer'),
                   model_uri=QO.qo_hasAnswer, domain=QoQuestionnaireResponse, range=Union[Union[dict, "QoAnswer"], list[Union[dict, "QoAnswer"]]])

slots.qo_toQuestion = Slot(uri=QO.toQuestion, name="qo_toQuestion", curie=QO.curie('toQuestion'),
                   model_uri=QO.qo_toQuestion, domain=QoAnswer, range=Union[dict, QoQuestion])

slots.sarefProperty__fhir_referenceRange = Slot(uri=FHIR['Observation.referenceRange'], name="sarefProperty__fhir_referenceRange", curie=FHIR.curie('Observation.referenceRange'),
                   model_uri=QO.sarefProperty__fhir_referenceRange, domain=None, range=Optional[Union[dict, FhirReferenceRange]])

slots.sarefPropertyValue__fhir_valueCodeableConcept = Slot(uri=FHIR.valueCodeableConcept, name="sarefPropertyValue__fhir_valueCodeableConcept", curie=FHIR.curie('valueCodeableConcept'),
                   model_uri=QO.sarefPropertyValue__fhir_valueCodeableConcept, domain=None, range=Optional[Union[dict, ValueCoding]])

slots.sarefPropertyValue__fhir_valueRange = Slot(uri=FHIR.valueRange, name="sarefPropertyValue__fhir_valueRange", curie=FHIR.curie('valueRange'),
                   model_uri=QO.sarefPropertyValue__fhir_valueRange, domain=None, range=Optional[Union[dict, FhirReferenceRange]])

slots.sarefPropertyValue__fhir_valueRatio = Slot(uri=FHIR.valueRatio, name="sarefPropertyValue__fhir_valueRatio", curie=FHIR.curie('valueRatio'),
                   model_uri=QO.sarefPropertyValue__fhir_valueRatio, domain=None, range=Optional[Union[dict, FhirValueRatio]])

slots.sarefPropertyValue__fhir_valuePeriod = Slot(uri=FHIR.valuePeriod, name="sarefPropertyValue__fhir_valuePeriod", curie=FHIR.curie('valuePeriod'),
                   model_uri=QO.sarefPropertyValue__fhir_valuePeriod, domain=None, range=Optional[Union[dict, TimeInterval]])

slots.sarefPropertyValue__fhir_valueAttachment = Slot(uri=FHIR.valueAttachment, name="sarefPropertyValue__fhir_valueAttachment", curie=FHIR.curie('valueAttachment'),
                   model_uri=QO.sarefPropertyValue__fhir_valueAttachment, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.numericalParams__numericalUnit = Slot(uri=UCUM.units, name="numericalParams__numericalUnit", curie=UCUM.curie('units'),
                   model_uri=QO.numericalParams__numericalUnit, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^ucum:'))

slots.numericalParams__numericalPrecision = Slot(uri=PHRO.precision, name="numericalParams__numericalPrecision", curie=PHRO.curie('precision'),
                   model_uri=QO.numericalParams__numericalPrecision, domain=None, range=Optional[int])

slots.valueCoding__code = Slot(uri=FHIR.code, name="valueCoding__code", curie=FHIR.curie('code'),
                   model_uri=QO.valueCoding__code, domain=None, range=str)

slots.valueCoding__display = Slot(uri=FHIR.display, name="valueCoding__display", curie=FHIR.curie('display'),
                   model_uri=QO.valueCoding__display, domain=None, range=str)

slots.fhirValueRatio__numerator = Slot(uri=FHIR.numerator, name="fhirValueRatio__numerator", curie=FHIR.curie('numerator'),
                   model_uri=QO.fhirValueRatio__numerator, domain=None, range=Union[dict, QuantityValue])

slots.fhirValueRatio__denominator = Slot(uri=FHIR.denominator, name="fhirValueRatio__denominator", curie=FHIR.curie('denominator'),
                   model_uri=QO.fhirValueRatio__denominator, domain=None, range=Union[dict, QuantityValue])

slots.intervalParams__minValue = Slot(uri=PHRO.minValue, name="intervalParams__minValue", curie=PHRO.curie('minValue'),
                   model_uri=QO.intervalParams__minValue, domain=None, range=Optional[float])

slots.intervalParams__minLabel = Slot(uri=PHRO.minLabel, name="intervalParams__minLabel", curie=PHRO.curie('minLabel'),
                   model_uri=QO.intervalParams__minLabel, domain=None, range=Optional[str])

slots.intervalParams__maxValue = Slot(uri=PHRO.maxValue, name="intervalParams__maxValue", curie=PHRO.curie('maxValue'),
                   model_uri=QO.intervalParams__maxValue, domain=None, range=Optional[float])

slots.intervalParams__maxLabel = Slot(uri=PHRO.maxLabel, name="intervalParams__maxLabel", curie=PHRO.curie('maxLabel'),
                   model_uri=QO.intervalParams__maxLabel, domain=None, range=Optional[str])

slots.fhirReferenceRange__lowRange = Slot(uri=PHRO.lowRange, name="fhirReferenceRange__lowRange", curie=PHRO.curie('lowRange'),
                   model_uri=QO.fhirReferenceRange__lowRange, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fhirReferenceRange__highRange = Slot(uri=PHRO.highRange, name="fhirReferenceRange__highRange", curie=PHRO.curie('highRange'),
                   model_uri=QO.fhirReferenceRange__highRange, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fhirReferenceRange__normalValue = Slot(uri=PHRO.normalValue, name="fhirReferenceRange__normalValue", curie=PHRO.curie('normalValue'),
                   model_uri=QO.fhirReferenceRange__normalValue, domain=None, range=Optional[Union[Union[dict, QuantityValue], list[Union[dict, QuantityValue]]]])

slots.qoOrderedQuestion__qo_required = Slot(uri=QO.required, name="qoOrderedQuestion__qo_required", curie=QO.curie('required'),
                   model_uri=QO.qoOrderedQuestion__qo_required, domain=None, range=Union[bool, Bool])

slots.qoQuestion__qo_tag = Slot(uri=QO.tag, name="qoQuestion__qo_tag", curie=QO.curie('tag'),
                   model_uri=QO.qoQuestion__qo_tag, domain=None, range=Union[str, list[str]])

slots.qoQuestion__qo_numericalParams = Slot(uri=QO.numericalParams, name="qoQuestion__qo_numericalParams", curie=QO.curie('numericalParams'),
                   model_uri=QO.qoQuestion__qo_numericalParams, domain=None, range=Optional[Union[dict, NumericalParams]])

slots.qoQuestion__qo_codingParams = Slot(uri=QO.codingParams, name="qoQuestion__qo_codingParams", curie=QO.curie('codingParams'),
                   model_uri=QO.qoQuestion__qo_codingParams, domain=None, range=Optional[Union[Union[dict, ValueCoding], list[Union[dict, ValueCoding]]]])

slots.qoQuestion__qo_codingOrdinal = Slot(uri=QO.codingOrdinal, name="qoQuestion__qo_codingOrdinal", curie=QO.curie('codingOrdinal'),
                   model_uri=QO.qoQuestion__qo_codingOrdinal, domain=None, range=Optional[Union[bool, Bool]])

slots.qoQuestion__qo_intervalParams = Slot(uri=QO.intervalParams, name="qoQuestion__qo_intervalParams", curie=QO.curie('intervalParams'),
                   model_uri=QO.qoQuestion__qo_intervalParams, domain=None, range=Optional[Union[dict, IntervalParams]])

slots.qoAnswer__qo_answerValue = Slot(uri=QO.answerValue, name="qoAnswer__qo_answerValue", curie=QO.curie('answerValue'),
                   model_uri=QO.qoAnswer__qo_answerValue, domain=None, range=Optional[str])

slots.qoAnswer__qo_isEmpty = Slot(uri=QO.isEmpty, name="qoAnswer__qo_isEmpty", curie=QO.curie('isEmpty'),
                   model_uri=QO.qoAnswer__qo_isEmpty, domain=None, range=Optional[Union[bool, Bool]])

slots.qo_Questionnaire_dcterms_created = Slot(uri=DCTERMS.created, name="qo_Questionnaire_dcterms_created", curie=DCTERMS.curie('created'),
                   model_uri=QO.qo_Questionnaire_dcterms_created, domain=QoQuestionnaire, range=Union[str, XSDDateTime])

slots.qo_Questionnaire_dcterms_modified = Slot(uri=DCTERMS.modified, name="qo_Questionnaire_dcterms_modified", curie=DCTERMS.curie('modified'),
                   model_uri=QO.qo_Questionnaire_dcterms_modified, domain=QoQuestionnaire, range=Union[str, XSDDateTime], mappings = [PROV["endedAtTime"], FHIR["Questionnaire.date"]])

slots.qo_Questionnaire_dcterms_creator = Slot(uri=DCTERMS.creator, name="qo_Questionnaire_dcterms_creator", curie=DCTERMS.curie('creator'),
                   model_uri=QO.qo_Questionnaire_dcterms_creator, domain=QoQuestionnaire, range=Union[Union[dict, ProvOrganization], list[Union[dict, ProvOrganization]]], mappings = [FHIR["Questionnaire.author"]])

slots.qo_Questionnaire_dcterms_isPartOf = Slot(uri=DCTERMS.isPartOf, name="qo_Questionnaire_dcterms_isPartOf", curie=DCTERMS.curie('isPartOf'),
                   model_uri=QO.qo_Questionnaire_dcterms_isPartOf, domain=QoQuestionnaire, range=Optional[Union[Union[dict, SuloProcess], list[Union[dict, SuloProcess]]]])

slots.qo_Questionnaire_fhir_status = Slot(uri=FHIR['resource-status'], name="qo_Questionnaire_fhir_status", curie=FHIR.curie('resource-status'),
                   model_uri=QO.qo_Questionnaire_fhir_status, domain=QoQuestionnaire, range=Union[Union[dict, "QoQuestionnaireStatus"], list[Union[dict, "QoQuestionnaireStatus"]]])

slots.qo_Questionnaire_qo_hasOrderedQuestion = Slot(uri=QO.hasOrderedQuestion, name="qo_Questionnaire_qo_hasOrderedQuestion", curie=QO.curie('hasOrderedQuestion'),
                   model_uri=QO.qo_Questionnaire_qo_hasOrderedQuestion, domain=QoQuestionnaire, range=Optional[Union[Union[dict, "QoOrderedQuestion"], list[Union[dict, "QoOrderedQuestion"]]]])

slots.qo_Questionnaire_qo_hasOrderedSection = Slot(uri=QO.hasOrderedSection, name="qo_Questionnaire_qo_hasOrderedSection", curie=QO.curie('hasOrderedSection'),
                   model_uri=QO.qo_Questionnaire_qo_hasOrderedSection, domain=QoQuestionnaire, range=Optional[Union[Union[dict, "QoOrderedSection"], list[Union[dict, "QoOrderedSection"]]]])

slots.qo_QuestionnaireStatus_saref_hasValue = Slot(uri=SAREF.hasValue, name="qo_QuestionnaireStatus_saref_hasValue", curie=SAREF.curie('hasValue'),
                   model_uri=QO.qo_QuestionnaireStatus_saref_hasValue, domain=QoQuestionnaireStatus, range=Union[str, "QoQuestionnaireStatusEnum"])

slots.qo_OrderedSection_qo_order = Slot(uri=QO.order, name="qo_OrderedSection_qo_order", curie=QO.curie('order'),
                   model_uri=QO.qo_OrderedSection_qo_order, domain=QoOrderedSection, range=int)

slots.qo_Section_dcterms_creator = Slot(uri=DCTERMS.creator, name="qo_Section_dcterms_creator", curie=DCTERMS.curie('creator'),
                   model_uri=QO.qo_Section_dcterms_creator, domain=QoSection, range=Union[Union[dict, ProvOrganization], list[Union[dict, ProvOrganization]]], mappings = [FHIR["Questionnaire.author"]])

slots.qo_Section_qo_hasOrderedQuestion = Slot(uri=QO.hasOrderedQuestion, name="qo_Section_qo_hasOrderedQuestion", curie=QO.curie('hasOrderedQuestion'),
                   model_uri=QO.qo_Section_qo_hasOrderedQuestion, domain=QoSection, range=Optional[Union[Union[dict, "QoOrderedQuestion"], list[Union[dict, "QoOrderedQuestion"]]]])

slots.qo_Section_qo_hasOrderedSection = Slot(uri=QO.hasOrderedSection, name="qo_Section_qo_hasOrderedSection", curie=QO.curie('hasOrderedSection'),
                   model_uri=QO.qo_Section_qo_hasOrderedSection, domain=QoSection, range=Optional[Union[Union[dict, QoOrderedSection], list[Union[dict, QoOrderedSection]]]])

slots.qo_OrderedQuestion_qo_order = Slot(uri=QO.order, name="qo_OrderedQuestion_qo_order", curie=QO.curie('order'),
                   model_uri=QO.qo_OrderedQuestion_qo_order, domain=QoOrderedQuestion, range=int)

slots.qo_Question_prov_type = Slot(uri=PROV.type, name="qo_Question_prov_type", curie=PROV.curie('type'),
                   model_uri=QO.qo_Question_prov_type, domain=QoQuestion, range=Union[Union[str, "QoQuestionType"], list[Union[str, "QoQuestionType"]]])

slots.qo_Question_dcterms_creator = Slot(uri=DCTERMS.creator, name="qo_Question_dcterms_creator", curie=DCTERMS.curie('creator'),
                   model_uri=QO.qo_Question_dcterms_creator, domain=QoQuestion, range=Union[Union[dict, ProvOrganization], list[Union[dict, ProvOrganization]]])

slots.qo_QuestionnaireResponse_dcterms_created = Slot(uri=DCTERMS.created, name="qo_QuestionnaireResponse_dcterms_created", curie=DCTERMS.curie('created'),
                   model_uri=QO.qo_QuestionnaireResponse_dcterms_created, domain=QoQuestionnaireResponse, range=Union[str, XSDDateTime], mappings = [FHIR["QuestionnaireResponse.authored"]])

slots.qo_QuestionnaireResponse_dcterms_modified = Slot(uri=DCTERMS.modified, name="qo_QuestionnaireResponse_dcterms_modified", curie=DCTERMS.curie('modified'),
                   model_uri=QO.qo_QuestionnaireResponse_dcterms_modified, domain=QoQuestionnaireResponse, range=Union[str, XSDDateTime], mappings = [PROV["endedAtTime"]])

slots.qo_QuestionnaireResponse_dcterms_isPartOf = Slot(uri=DCTERMS.isPartOf, name="qo_QuestionnaireResponse_dcterms_isPartOf", curie=DCTERMS.curie('isPartOf'),
                   model_uri=QO.qo_QuestionnaireResponse_dcterms_isPartOf, domain=QoQuestionnaireResponse, range=Optional[Union[Union[dict, SuloProcess], list[Union[dict, SuloProcess]]]])

slots.qo_QuestionnaireResponse_prov_wasAttributedTo = Slot(uri=PROV.wasAttributedTo, name="qo_QuestionnaireResponse_prov_wasAttributedTo", curie=PROV.curie('wasAttributedTo'),
                   model_uri=QO.qo_QuestionnaireResponse_prov_wasAttributedTo, domain=QoQuestionnaireResponse, range=Union[Union[dict, FoafPerson], list[Union[dict, FoafPerson]]])

slots.qo_QuestionnaireResponse_fhir_status = Slot(uri=FHIR['resource-status'], name="qo_QuestionnaireResponse_fhir_status", curie=FHIR.curie('resource-status'),
                   model_uri=QO.qo_QuestionnaireResponse_fhir_status, domain=QoQuestionnaireResponse, range=Union[Union[dict, "QoQuestionnaireResponseStatus"], list[Union[dict, "QoQuestionnaireResponseStatus"]]])

slots.qo_QuestionnaireResponseStatus_saref_hasValue = Slot(uri=SAREF.hasValue, name="qo_QuestionnaireResponseStatus_saref_hasValue", curie=SAREF.curie('hasValue'),
                   model_uri=QO.qo_QuestionnaireResponseStatus_saref_hasValue, domain=QoQuestionnaireResponseStatus, range=Union[str, "QoQuestionnaireResponseStatusEnum"])

slots.qo_Answer_prov_generatedAtTime = Slot(uri=PROV.generatedAtTime, name="qo_Answer_prov_generatedAtTime", curie=PROV.curie('generatedAtTime'),
                   model_uri=QO.qo_Answer_prov_generatedAtTime, domain=QoAnswer, range=Union[Union[str, XSDDateTime], list[Union[str, XSDDateTime]]])

