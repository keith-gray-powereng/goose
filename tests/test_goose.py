from pyasn1.codec.ber import encoder
from pyasn1.type import tag
from pyasn1.type import univ
from scapy.layers.l2 import Ether
from scapy.layers.l2 import Dot1Q
from scapy.compat import raw

from goose.goose import GOOSE
from goose.goose_pdu import AllData
from goose.goose_pdu import Data
from goose.goose_pdu import IECGoosePDU


def test_goose_message():
    g = IECGoosePDU().subtype(
        implicitTag=tag.Tag(
            tag.tagClassApplication,
            tag.tagFormatConstructed,
            1
        )
    )
    g.setComponentByName(
        'gocbRef',
        'DENNY_11F_13_100CFG/LLN0$GO$Dset_SubnetCtrl'
    )
    g.setComponentByName('timeAllowedtoLive', 2000)
    g.setComponentByName('datSet', 'DENNY_11F_13_100CFG/LLN0$G_NetCtrl')
    g.setComponentByName('goID', '11F_13_100Dset_SubnetCtrl')
    g.setComponentByName('t', b'\x5a\xaa\xe0\xa4\x6f\xf3\x5e\x92')
    g.setComponentByName('stNum', 96)
    g.setComponentByName('sqNum', 16192)
    g.setComponentByName('test', False)
    g.setComponentByName('confRev', 2)
    g.setComponentByName('ndsCom', False)
    g.setComponentByName('numDatSetEntries', 5)
    all_data = AllData().subtype(
        implicitTag=tag.Tag(
            tag.tagClassContext,
            tag.tagFormatConstructed,
            11
        )
    )
    inner1 = univ.SequenceOf(componentType=Data()).subtype(
        implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
    )
    inner1.setComponentByPosition(0, Data().setComponentByName("boolean", False))
    inner1.setComponentByPosition(1, Data().setComponentByName("bit-string", "'0000000000000'B"))
    inner1.setComponentByPosition(2, Data().setComponentByName('utc-time', b'\x5a\xaa\xe0\xa4\x6f\xf3\x5e\x92'))
    data1 = Data()
    data1.setComponentByName('structure', inner1)
    inner2 = univ.SequenceOf(componentType=Data()).subtype(
        implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
    )
    inner2.setComponentByPosition(0, Data().setComponentByName("boolean", False))
    inner2.setComponentByPosition(1, Data().setComponentByName("bit-string", "'0000000000000'B"))
    inner2.setComponentByPosition(2, Data().setComponentByName('utc-time', b'\x5a\xa9\x39\x5a\x03\xea\x4a\x92'))
    data2 = Data()
    data2.setComponentByName('structure', inner2)
    inner3 = univ.SequenceOf(componentType=Data()).subtype(
        implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
    )
    inner3.setComponentByPosition(0, Data().setComponentByName("boolean", False))
    inner3.setComponentByPosition(1, Data().setComponentByName("bit-string", "'0000000000000'B"))
    inner3.setComponentByPosition(2, Data().setComponentByName('utc-time', b'\x5a\xa9\x39\x5a\x03\xea\x4a\x92'))
    data3 = Data()
    data3.setComponentByName('structure', inner3)
    inner4 = univ.SequenceOf(componentType=Data()).subtype(
        implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
    )
    inner4.setComponentByPosition(0, Data().setComponentByName("boolean", False))
    inner4.setComponentByPosition(1, Data().setComponentByName("bit-string", "'0000000000000'B"))
    inner4.setComponentByPosition(2, Data().setComponentByName('utc-time', b'\x5a\xa9\x39\x5a\x03\xea\x4a\x92'))
    data4 = Data()
    data4.setComponentByName('structure', inner4)
    inner5 = univ.SequenceOf(componentType=Data()).subtype(
        implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
    )
    inner5.setComponentByPosition(0, Data().setComponentByName("boolean", False))
    inner5.setComponentByPosition(1, Data().setComponentByName("bit-string", "'0000000000000'B"))
    inner5.setComponentByPosition(2, Data().setComponentByName('utc-time', b'\x5a\xaa\xd1\x7d\xd2\x48\x21\x92'))
    data5 = Data()
    data5.setComponentByName('structure', inner5)
    all_data.setComponentByPosition(0, data1)
    all_data.setComponentByPosition(1, data2)
    all_data.setComponentByPosition(2, data3)
    all_data.setComponentByPosition(3, data4)
    all_data.setComponentByPosition(4, data5)
    g.setComponentByName('allData', all_data)
    calculated = raw(
        Ether(dst='01:0c:cd:01:00:00', src='00:30:a7:13:2e:92') /
        Dot1Q(vlan=10, type=0x88b8, prio=6) /
        GOOSE(appid=int(0x0000)) /
        encoder.encode(g),
    )
    expected = (
        b"\x01\x0c\xcd\x01\x00\x00\x00\x30\xa7\x13\x2e\x92\x81\x00\xc0\x0a"
        b"\x88\xb8\x00\x00\x00\xfe\x00\x00\x00\x00\x61\x81\xf3\x80\x2b\x44"
        b"\x45\x4e\x4e\x59\x5f\x31\x31\x46\x5f\x31\x33\x5f\x31\x30\x30\x43"
        b"\x46\x47\x2f\x4c\x4c\x4e\x30\x24\x47\x4f\x24\x44\x73\x65\x74\x5f"
        b"\x53\x75\x62\x6e\x65\x74\x43\x74\x72\x6c\x81\x02\x07\xd0\x82\x22"
        b"\x44\x45\x4e\x4e\x59\x5f\x31\x31\x46\x5f\x31\x33\x5f\x31\x30\x30"
        b"\x43\x46\x47\x2f\x4c\x4c\x4e\x30\x24\x47\x5f\x4e\x65\x74\x43\x74"
        b"\x72\x6c\x83\x19\x31\x31\x46\x5f\x31\x33\x5f\x31\x30\x30\x44\x73"
        b"\x65\x74\x5f\x53\x75\x62\x6e\x65\x74\x43\x74\x72\x6c\x84\x08\x5a"
        b"\xaa\xe0\xa4\x6f\xf3\x5e\x92\x85\x01\x60\x86\x02\x3f\x40\x87\x01"
        b"\x00\x88\x01\x02\x89\x01\x00\x8a\x01\x05\xab\x64\xa2\x12\x83\x01"
        b"\x00\x84\x03\x03\x00\x00\x91\x08\x5a\xaa\xe0\xa4\x6f\xf3\x5e\x92"
        b"\xa2\x12\x83\x01\x00\x84\x03\x03\x00\x00\x91\x08\x5a\xa9\x39\x5a"
        b"\x03\xea\x4a\x92\xa2\x12\x83\x01\x00\x84\x03\x03\x00\x00\x91\x08"
        b"\x5a\xa9\x39\x5a\x03\xea\x4a\x92\xa2\x12\x83\x01\x00\x84\x03\x03"
        b"\x00\x00\x91\x08\x5a\xa9\x39\x5a\x03\xea\x4a\x92\xa2\x12\x83\x01"
        b"\x00\x84\x03\x03\x00\x00\x91\x08\x5a\xaa\xd1\x7d\xd2\x48\x21\x92"
    )
    assert calculated[0:7] == expected[0:7]  # destination MAC
    assert calculated[7:12] == expected[7:12]  # source MAC
    assert calculated[12:14] == expected[12:14]  # type
    assert calculated[14:18] == expected[14:18]  # 802.1Q
    assert calculated[18:20] == expected[18:20]  # APPID
    assert calculated[20:22] == expected[20:22]  # Length
    assert calculated[22:26] == expected[22:26]  # Reserved1 and Reserved2
    assert calculated[26:28] == expected[26:28]  # goosePDU asn.1 tag
    assert calculated[28:74] == expected[28:74]  # gocbRef
    assert calculated[74:78] == expected[74:78]  # timeAllowedtoLive
    assert calculated[78:114] == expected[78:114]  # datSet
    assert calculated[114:141] == expected[114:141]  # goID
    assert calculated[141:151] == expected[141:151]  # t
    assert calculated[151:154] == expected[151:154]  # stNum
    assert calculated[154:158] == expected[154:158]  # sqNum
    assert calculated[158:161] == expected[158:161]  # test
    assert calculated[161:164] == expected[161:164]  # confRev
    assert calculated[164:167] == expected[164:167]  # ndsCom
    assert calculated[167:170] == expected[167:170]  # numDatSetEntries
    assert calculated[170:172] == expected[170:172]  # allData asn.1
    assert calculated[172:174] == expected[172:174]  # structure #1 asn.1
    assert calculated[174:192] == expected[174:192]  # structure #1
    assert calculated[192:194] == expected[192:194]  # structure #2 asn.1
    assert calculated[194:212] == expected[194:212]  # structure #2
    assert calculated[212:214] == expected[212:214]  # structure #3 asn.1
    assert calculated[214:232] == expected[214:232]  # structure #3
    assert calculated[232:234] == expected[232:234]  # structure #4 asn.1
    assert calculated[234:252] == expected[234:252]  # structure #4
    assert calculated[252:254] == expected[252:254]  # structure #5 asn.1
    assert calculated[254:272] == expected[254:272]  # structure #5 asn.1
    assert calculated == expected
