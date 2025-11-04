
# Class: ScoreParameter

Parameters for score definitions, such as min/max values, categories or constants needed.

URI: [datamodel:ScoreParameter](https://w3id.org/faqir/datamodel/ScoreParameter)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ValueNumerical],[ValueDateTime],[ValueDateTime]<scoreParameterValueDateTime%200..1-++[ScoreParameter&#124;scoreParameterId:uriorcurie;scoreParameterLabel:string;scoreParameterType:ScoreParameterType],[ValueNumerical]<scoreParameterValueNumerical%200..1-++[ScoreParameter],[ScoreDefinition]<scoreParameterPartOfScoreDefinition%201..1-%20[ScoreParameter],[ScoreDefinition]-%20scoreDefinitionHasScoreParameter%200..*>[ScoreParameter],[ScoreDefinition])](https://yuml.me/diagram/nofunky;dir:TB/class/[ValueNumerical],[ValueDateTime],[ValueDateTime]<scoreParameterValueDateTime%200..1-++[ScoreParameter&#124;scoreParameterId:uriorcurie;scoreParameterLabel:string;scoreParameterType:ScoreParameterType],[ValueNumerical]<scoreParameterValueNumerical%200..1-++[ScoreParameter],[ScoreDefinition]<scoreParameterPartOfScoreDefinition%201..1-%20[ScoreParameter],[ScoreDefinition]-%20scoreDefinitionHasScoreParameter%200..*>[ScoreParameter],[ScoreDefinition])

## Referenced by Class

 *  **[ScoreDefinition](ScoreDefinition.md)** *[scoreDefinitionHasScoreParameter](scoreDefinitionHasScoreParameter.md)*  <sub>0..\*</sub>  **[ScoreParameter](ScoreParameter.md)**

## Attributes


### Own

 * [scoreParameterPartOfScoreDefinition](scoreParameterPartOfScoreDefinition.md)  <sub>1..1</sub>
     * Description: The ScoreDefinition(s) that this ScoreParameter is part of.
     * Range: [ScoreDefinition](ScoreDefinition.md)
 * [➞scoreParameterId](scoreParameter__scoreParameterId.md)  <sub>1..1</sub>
     * Description: Unique identifier for the score parameter.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞scoreParameterLabel](scoreParameter__scoreParameterLabel.md)  <sub>1..1</sub>
     * Description: Label or title of the parameter. Standard English name.
     * Range: [String](types/String.md)
 * [➞scoreParameterType](scoreParameter__scoreParameterType.md)  <sub>1..1</sub>
     * Description: Type of parameter: numerical or dateTime.
     * Range: [ScoreParameterType](ScoreParameterType.md)
 * [➞scoreParameterValueNumerical](scoreParameter__scoreParameterValueNumerical.md)  <sub>0..1</sub>
     * Description: Numerical value parameter (e.g., 0.785, 82).
     * Range: [ValueNumerical](ValueNumerical.md)
 * [➞scoreParameterValueDateTime](scoreParameter__scoreParameterValueDateTime.md)  <sub>0..1</sub>
     * Description: DateTime value parameter formatted as YYYY-MM-DDThh:mm:ss+zz:zz.
     * Range: [ValueDateTime](ValueDateTime.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:ScoreParameter |