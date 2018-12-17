from pyasn1.codec.ber import encoder
from pyasn1.type import tag
from scapy.layers.l2 import Ether
from scapy.layers.l2 import Dot1Q
from scapy.utils import hexdump

from goose import GOOSE
from goose_pdu import AllData
from goose_pdu import Data
from goose_pdu import IECGoosePDU

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
    g.setComponentByName('allData', d)

    hexdump(
        Ether(dst='01:0c:cd:01:00:14') /
        Dot1Q(vlan=10, type=0x88b8, prio=6) /
        GOOSE(appid=int(0x00b1)) /
        encoder.encode(g)
    )
