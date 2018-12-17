from struct import pack

from scapy.packet import Packet
from scapy.fields import XShortField


class GOOSE(Packet):
    name = "GOOSE"
    fields_desc = [
        XShortField("appid", 0),
        XShortField("length", 8),
        XShortField("reserved1", 0),
        XShortField("reserved2", 0),
    ]

    def post_build(self, packet, payload):
        goose_pdu_length = len(packet) + len(payload)
        packet = packet[:2] + pack('!H', goose_pdu_length) + packet[4:]
        return packet + payload
