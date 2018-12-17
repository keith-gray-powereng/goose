# coding: utf-8

from pyasn1.codec.ber import encoder
from pyasn1.type import char, constraint, namedtype, tag, univ, useful


class FloatingPoint(univ.OctetString):
    pass


class Unsigned(univ.Integer):
    subtypeSpec = constraint.ValueRangeConstraint(0, float('inf'))


class BCD(univ.Integer):
    subtypeSpec = constraint.ValueRangeConstraint(0, float('inf'))


class TimeOfDay(univ.OctetString):
    subtypeSpec = constraint.ConstraintsUnion(
        constraint.ValueSizeConstraint(4, 4),
        constraint.ValueSizeConstraint(6, 6)
    )


class MMSString(char.UTF8String):
    pass


class UtcTime(univ.OctetString):
    subtypeSpec = constraint.ValueSizeConstraint(8, 8)


class Data(univ.Choice):
    pass


Data.componentType = namedtype.NamedTypes(
    namedtype.NamedType('array', univ.SequenceOf(componentType=Data()).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('structure', univ.SequenceOf(componentType=Data()).subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('boolean', univ.Boolean().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
    namedtype.NamedType('bit-string', univ.BitString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
    namedtype.NamedType('integer', univ.Integer().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
    namedtype.NamedType('unsigned', univ.Integer().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
    namedtype.NamedType('floating-point', FloatingPoint().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
    namedtype.NamedType('real', univ.Real().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
    namedtype.NamedType('octet-string', univ.OctetString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
    namedtype.NamedType('visible-string', char.VisibleString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
    namedtype.NamedType('binary-time', TimeOfDay().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
    namedtype.NamedType('bcd', univ.Integer().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
    namedtype.NamedType('booleanArray', univ.BitString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
    namedtype.NamedType('objId', univ.ObjectIdentifier().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
    namedtype.NamedType('mMSString', MMSString().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
    namedtype.NamedType('utc-time', UtcTime().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17)))
)


class AllData(univ.SequenceOf):
    componentType = Data()


class IECGoosePDU(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType(
            'gocbRef',
            char.VisibleString().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    0
                )
            )
        ),
        namedtype.NamedType(
            'timeAllowedtoLive',
            univ.Integer().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    1
                )
            )
        ),
        namedtype.NamedType(
            'datSet',
            char.VisibleString().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    2
                )
            )
        ),
        namedtype.OptionalNamedType(
            'goID',
            char.VisibleString().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    3
                )
            )
        ),
        namedtype.NamedType(
            't',
            UtcTime().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    4
                )
            )
        ),
        namedtype.NamedType(
            'stNum',
            univ.Integer().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    5
                )
            )
        ),
        namedtype.NamedType(
            'sqNum',
            univ.Integer().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    6
                )
            )
        ),
        namedtype.NamedType(
            'test',
            univ.Boolean(False).subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    7
                )
            )
        ),
        namedtype.NamedType(
            'confRev',
            univ.Integer().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    8
                )
            )
        ),
        namedtype.NamedType(
            'ndsCom',
            univ.Boolean(False).subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    9
                )
            )
        ),
        namedtype.NamedType(
            'numDatSetEntries',
            univ.Integer().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    10
                )
            )
        ),
        namedtype.NamedType(
            'allData',
            AllData().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatConstructed,
                    11
                )
            )
        ),
        namedtype.OptionalNamedType(
            'security',
            univ.OctetString().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    12
                )
            )
        ),
    )


if __name__ == '__main__':
    g = IECGoosePDU().subtype(
        implicitTag=tag.Tag(
            tag.tagClassApplication,
            tag.tagFormatConstructed,
            1
        )
    )
    g.setComponentByName('gocbRef', 'PDC02_11_700G_G1CFG/LLN0$GO$GooseDset_BF')
    g.setComponentByName('timeAllowedtoLive', 2000)
    g.setComponentByName('datSet', 'PDC02_11_700G_G1CFG/LLN0$Dset_BF')
    g.setComponentByName('goID', '11_700G_G1_Dset_BF')
    g.setComponentByName('t', b'\x55\x15\x1b\x9b\x69\x37\x40\x92')
    g.setComponentByName('stNum', 5)
    g.setComponentByName('sqNum', 1757)
    g.setComponentByName('test', False)
    g.setComponentByName('confRev', 3)
    g.setComponentByName('ndsCom', False)
    g.setComponentByName('numDatSetEntries', 6)
    d = AllData().subtype(
        implicitTag=tag.Tag(
            tag.tagClassContext,
            tag.tagFormatConstructed,
            11
        )
    )
    d1 = Data()
    d1.setComponentByName('boolean', False)
    d2 = Data()
    d2.setComponentByName('bit-string', "'0000000000000'B")
    d3 = Data()
    d3.setComponentByName('utc-time', b'\x55\x15\x14\xc0\xc8\xf5\xc0\x92')
    d4 = Data()
    d4.setComponentByName('boolean', False)
    d5 = Data()
    d5.setComponentByName('bit-string', "'0000000000000'B")
    d6 = Data()
    d6.setComponentByName('utc-time', b'\x55\x15\x14\xaa\x3a\x9f\x80\x92')
    d.setComponentByPosition(0, d1)
    d.setComponentByPosition(1, d2)
    d.setComponentByPosition(2, d3)
    d.setComponentByPosition(3, d4)
    d.setComponentByPosition(4, d5)
    d.setComponentByPosition(5, d6)
    print(d)
    print(d.prettyPrint())
    g.setComponentByName('allData', d)
    print(g.prettyPrint())

    print(encoder.encode(g))
