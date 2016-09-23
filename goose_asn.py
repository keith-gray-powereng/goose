# coding: utf-8

from pyasn1.codec.ber import encoder
from pyasn1.type import univ, namedtype, tag, char


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
        namedtype.DefaultedNamedType(
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
        namedtype.DefaultedNamedType(
            'numDatSetEntries',
            univ.Integer().subtype(
                implicitTag=tag.Tag(
                    tag.tagClassContext,
                    tag.tagFormatSimple,
                    10
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
    g.setComponentByName('gocbRef', 'ABCDE')
    g.setComponentByName('timeAllowedtoLive', 2)
    g.setComponentByName('datSet', 'Dset_TT')
    g.setComponentByName('t', 'some time')
    g.setComponentByName('stNum', 0)
    g.setComponentByName('sqNum', 0)
    g.setComponentByName('confRev', 0)
    g.setComponentByName('numDatSetEntries', 0)

    print(encoder.encode(g))
