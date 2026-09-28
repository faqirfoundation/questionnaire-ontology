
# Class: sphn_TimePattern

sequence or regularity in the occurrence of events over time

URI: [qo:SphnTimePattern](https://ns.faqir.org/q-o#SphnTimePattern)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<sphn_hasOffset%200..1-++[SphnTimePattern&#124;prov_type:uriorcurie%20*;sphn_hasTimeOfDayCode:uriorcurie%20%3F],[QuantityValue]<sphn_hasFrequency%200..1-++[SphnTimePattern],[QuantityValue])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<sphn_hasOffset%200..1-++[SphnTimePattern&#124;prov_type:uriorcurie%20*;sphn_hasTimeOfDayCode:uriorcurie%20%3F],[QuantityValue]<sphn_hasFrequency%200..1-++[SphnTimePattern],[QuantityValue])

## Attributes


### Own

 * [prov_type](prov_type.md)  <sub>0..\*</sub>
     * Description: The attribute prov:type provides further typing information for any construct with an optional set of attribute-value pairs.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞sphn_hasFrequency](sphnTimePattern__sphn_hasFrequency.md)  <sub>0..1</sub>
     * Description: number of events per unit of time
     * Range: [QuantityValue](QuantityValue.md)
 * [➞sphn_hasOffset](sphnTimePattern__sphn_hasOffset.md)  <sub>0..1</sub>
     * Description: time between events associated to the concept
     * Range: [QuantityValue](QuantityValue.md)
 * [➞sphn_hasTimeOfDayCode](sphnTimePattern__sphn_hasTimeOfDayCode.md)  <sub>0..1</sub>
     * Description: coded information specifying the temporal period of the day associated to the concept
     * Range: [Uriorcurie](types/Uriorcurie.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | sphn:TimePattern |
|  | | snomed:272103003 |