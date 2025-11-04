
# Class: IntervalParams

Parameters for interval values, including minimum and maximum values.

URI: [datamodel:IntervalParams](https://w3id.org/faqir/datamodel/IntervalParams)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Question]++-%20questionIntervalParams%200..1>[IntervalParams&#124;minValue:float;minLabel:string%20%3F;maxValue:float;maxLabel:string%20%3F],[ScoreDefinition]++-%20scoreDefinitionIntervalParams%200..1>[IntervalParams],[ScoreDefinition],[Question])](https://yuml.me/diagram/nofunky;dir:TB/class/[Question]++-%20questionIntervalParams%200..1>[IntervalParams&#124;minValue:float;minLabel:string%20%3F;maxValue:float;maxLabel:string%20%3F],[ScoreDefinition]++-%20scoreDefinitionIntervalParams%200..1>[IntervalParams],[ScoreDefinition],[Question])

## Referenced by Class

 *  **None** *[➞questionIntervalParams](question__questionIntervalParams.md)*  <sub>0..1</sub>  **[IntervalParams](IntervalParams.md)**
 *  **None** *[➞scoreDefinitionIntervalParams](scoreDefinition__scoreDefinitionIntervalParams.md)*  <sub>0..1</sub>  **[IntervalParams](IntervalParams.md)**

## Attributes


### Own

 * [➞minValue](intervalParams__minValue.md)  <sub>1..1</sub>
     * Description: The minimum value of the interval.
     * Range: [Float](types/Float.md)
 * [➞minLabel](intervalParams__minLabel.md)  <sub>0..1</sub>
     * Description: The label for the minimum value of the interval.
     * Range: [String](types/String.md)
 * [➞maxValue](intervalParams__maxValue.md)  <sub>1..1</sub>
     * Description: The maximum value of the interval.
     * Range: [Float](types/Float.md)
 * [➞maxLabel](intervalParams__maxLabel.md)  <sub>0..1</sub>
     * Description: The label for the maximum value of the interval.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faqir:IntervalParams |