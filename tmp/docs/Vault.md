
# Class: Vault

The FAQIR healthdata vault.

URI: [datamodel:Vault](https://w3id.org/faqir/datamodel/Vault)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Weight],[FullName]<full_name%200..1-++[Vault&#124;vaultId:uriorcurie;birthdate:datetime%20%3F;lastUpdated(i):datetime],[Weight]<weight%200..1-++[Vault],[Organization]<vaultManagedByOrg%201..1-%20[Vault],[QuestionnaireResponse]<hasQuestionnaireResponse%200..*-%20[Vault],[Organization]-%20organizationManagesVault%200..*>[Vault],[QuestionnaireResponse]-%20questionnaireResponseBySubject%201..1>[Vault],[Metadata]^-[Vault],[QuestionnaireResponse],[Organization],[Metadata],[FullName])](https://yuml.me/diagram/nofunky;dir:TB/class/[Weight],[FullName]<full_name%200..1-++[Vault&#124;vaultId:uriorcurie;birthdate:datetime%20%3F;lastUpdated(i):datetime],[Weight]<weight%200..1-++[Vault],[Organization]<vaultManagedByOrg%201..1-%20[Vault],[QuestionnaireResponse]<hasQuestionnaireResponse%200..*-%20[Vault],[Organization]-%20organizationManagesVault%200..*>[Vault],[QuestionnaireResponse]-%20questionnaireResponseBySubject%201..1>[Vault],[Metadata]^-[Vault],[QuestionnaireResponse],[Organization],[Metadata],[FullName])

## Parents

 *  is_a: [Metadata](Metadata.md) - Base class for metadata tracking (e.g. schema versioning & last updated).

## Referenced by Class

 *  **[Organization](Organization.md)** *[organizationManagesVault](organizationManagesVault.md)*  <sub>0..\*</sub>  **[Vault](Vault.md)**
 *  **[QuestionnaireResponse](QuestionnaireResponse.md)** *[questionnaireResponseBySubject](questionnaireResponseBySubject.md)*  <sub>1..1</sub>  **[Vault](Vault.md)**

## Attributes


### Own

 * [hasQuestionnaireResponse](hasQuestionnaireResponse.md)  <sub>0..\*</sub>
     * Description: QuestionnaireResponse authored by this vault's user.
     * Range: [QuestionnaireResponse](QuestionnaireResponse.md)
 * [vaultManagedByOrg](vaultManagedByOrg.md)  <sub>1..1</sub>
     * Description: Organization managing this vault.
     * Range: [Organization](Organization.md)
 * [➞vaultId](vault__vaultId.md)  <sub>1..1</sub>
     * Description: The unique identifier for a vault.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞birthdate](vault__birthdate.md)  <sub>0..1</sub>
     * Description: The date of birth.
     * Range: [Datetime](types/Datetime.md)
 * [➞weight](vault__weight.md)  <sub>0..1</sub>
     * Description: The weight of the vault's user.
     * Range: [Weight](Weight.md)
 * [➞full_name](vault__full_name.md)  <sub>0..1</sub>
     * Description: The full name of the vault's user.
     * Range: [FullName](FullName.md)

### Inherited from Metadata:

 * [➞lastUpdated](metadata__lastUpdated.md)  <sub>1..1</sub>
     * Description: The date and time when the entity was last updated.
     * Range: [Datetime](types/Datetime.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:vault |