# Enum: OrganizationType 




_Type of organization: hospital, government, professional, research or serviceProvider._



URI: [OrganizationType](OrganizationType.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| hospital | fhir:organization-type#prov |  |
| government | fhir:organization-type#gov |  |
| professional | fhir:organization-type#ind |  |
| research | fhir:organization-type#edu |  |
| serviceProvider | fhir:organization-type#bus |  |




## Slots

| Name | Description |
| ---  | --- |
| [organizationType](organizationType.md) | Type of organization |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/faqir/datamodel






## LinkML Source

<details>
```yaml
name: OrganizationType
description: 'Type of organization: hospital, government, professional, research or
  serviceProvider.'
from_schema: https://w3id.org/faqir/datamodel
rank: 1000
enum_uri: faqir:OrganizationType
permissible_values:
  hospital:
    text: hospital
    meaning: fhir:organization-type#prov
  government:
    text: government
    meaning: fhir:organization-type#gov
  professional:
    text: professional
    meaning: fhir:organization-type#ind
  research:
    text: research
    meaning: fhir:organization-type#edu
  serviceProvider:
    text: serviceProvider
    meaning: fhir:organization-type#bus

```
</details>
