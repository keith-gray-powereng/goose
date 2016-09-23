# coding: utf-8

from pyasn1.codec.ber import encoder
from pyasn1.type import char, namedtype, tag, univ, useful


class FloatingPoint(univ.OctetString):
    pass


class Data(univ.Choice):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('boolean', univ.Boolean().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                3
            )
        )),
        namedtype.NamedType('bit-string', univ.BitString().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                4
            )
        )),
        namedtype.NamedType('integer', univ.Integer().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                5
            )
        )),
        # TODO: Unsigned Should Never be Negative
        namedtype.NamedType('unsigned', univ.Integer().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                6
            )
        )),
        namedtype.NamedType('floating-point', FloatingPoint().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                7
            )
        )),
        namedtype.NamedType('octet-string', univ.OctetString().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                9
            )
        )),
        namedtype.NamedType('visible-string', char.VisibleString().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                10
            )
        )),
        namedtype.NamedType('generalized-time', useful.GeneralizedTime().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                11
            )
        )),
        # TODO: Binary Time should be of TimeOfDay type with size of 4 or 6
        namedtype.NamedType('binary-time', univ.OctetString().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                12
            )
        )),
        # TODO: BCD Should Never be Negative
        namedtype.NamedType('bcd', univ.Integer().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                13
            )
        )),
        namedtype.NamedType('booleanArray', univ.BitString().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                14
            )
        )),
        namedtype.NamedType('objId', univ.ObjectIdentifier().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                15
            )
        )),
        # TODO: MMS String should be its own type
        namedtype.NamedType('mMSString', char.UTF8String().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                16
            )
        )),
        # TODO: UTC Time should be its own type
        namedtype.NamedType('utc-time', univ.OctetString().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                17
            )
        ))
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
            univ.OctetString().subtype(
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
        namedtype.DefaultedNamedType(
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
        namedtype.DefaultedNamedType(
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
    g = IECGoosePDU()
    g.setComponentByName('gocbRef', 'PDC02_11_700G_G1CFG/LLN0$GO$GooseDset_BF')
    g.setComponentByName('timeAllowedtoLive', 2000)
    g.setComponentByName('datSet', 'PDC02_11_700G_G1CFG/LN0$Dset_BF')
    g.setComponentByName('goID', '11_700G_G1_Dset_BF')
    g.setComponentByName('t', 'some time')
    g.setComponentByName('stNum', 5)
    g.setComponentByName('sqNum', 1757)
    g.setComponentByName('test', False)
    g.setComponentByName('confRev', 3)
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
    d2.setComponentByName('bit-string', "'0000'B")
    d3 = Data()
    d3.setComponentByName('utc-time', '0000')
    d4 = Data()
    d4.setComponentByName('boolean', False)
    d5 = Data()
    d5.setComponentByName('bit-string', "'0000'B")
    d6 = Data()
    d6.setComponentByName('utc-time', '0000')
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
