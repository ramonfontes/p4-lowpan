from scapy.all import *
from scapy.fields import *

class Lowpan(Packet):
    name = "Lowpan"
    fields_desc = [
        ShortField("dispatch", 0),
        ShortField("identification", 0),
        ShortField("ha_len", 0),
        LongField("unused", 0),
        ShortField("ethType", 0)
    ]

class Lowpan1(Packet):
    name = "Lowpan"
    fields_desc = [
        ShortField("dispatch", 0),
        ShortField("identification", 0),
        ShortField("ha_len", 0),
        LongField("unused", 0),
        ShortField("ethType", 0)
    ]

class Lowpan2(Packet):
    name = "Lowpan"
    fields_desc = [
        ShortField("dispatch", 0),
        ShortField("identification", 0),
        ShortField("ha_len", 0),
        LongField("unused", 0),
        ShortField("ethType", 0)
    ]

class Lowpan3(Packet):
    name = "Lowpan"
    fields_desc = [
        ShortField("dispatch", 0),
        ShortField("identification", 0),
        ShortField("ha_len", 0),
        LongField("unused", 0),
        ShortField("ethType", 0)
    ]


class IPv6Custom(Packet):
    name = "IPv6Custom"
    fields_desc = [
        BitField("version", 6, 4),
        BitField("trafficClass", 0, 8),
        BitField("flowLabel", 0, 20),
        ShortField("payloadLength", 0),
        ByteField("nextHeader", 0),
        ByteField("hopLimit", 0),
        IP6Field("srcAddr", "fe80::1"),
        IP6Field("dstAddr", "ff02::1a9b")
    ]

class IPv6Custom1(Packet):
    name = "IPv6Custom"
    fields_desc = [
        BitField("version", 6, 4),
        BitField("trafficClass", 0, 8),
        BitField("flowLabel", 0, 20),
        ShortField("payloadLength", 0),
        ByteField("nextHeader", 0),
        ByteField("hopLimit", 0),
        IP6Field("srcAddr", "fe80::1"),
        IP6Field("dstAddr", "ff02::1a9b")
    ]

class IPv6Custom2(Packet):
    name = "IPv6Custom"
    fields_desc = [
        BitField("version", 6, 4),
        BitField("trafficClass", 0, 8),
        BitField("flowLabel", 0, 20),
        ShortField("payloadLength", 0),
        ByteField("nextHeader", 0),
        ByteField("hopLimit", 0),
        IP6Field("srcAddr", "fe80::1"),
        IP6Field("dstAddr", "ff02::1a9b")
    ]

# dis header
class Icmpv6_dis(Packet):
    name = "Icmpv6_dis"
    fields_desc = [
        ByteField("type", 0),
        ByteField("code", 0),
        ShortField("checksum", 0),
        ByteField("flags", 0),
        ByteField("reserved", 0),
    ]

class IPv6Custom3(Packet):
    name = "IPv6Custom"
    fields_desc = [
        BitField("version", 6, 4),
        BitField("trafficClass", 0, 8),
        BitField("flowLabel", 0, 20),
        ShortField("payloadLength", 0),
        ByteField("nextHeader", 0),
        ByteField("hopLimit", 0),
        IP6Field("srcAddr", "fe80::1"),
        IP6Field("dstAddr", "ff02::1a9b")
    ]

# dio header
class Icmpv6_dio(Packet):
    name = "Icmpv6_dio"
    fields_desc = [
        ByteField("type", 0),
        ByteField("code", 0),
        ShortField("checksum", 0),
        ByteField("RPLInstanceID", 0),
        ByteField("version", 0),
        ShortField("rank", 0),
        ByteField("flags", 0),
        ByteField("DTSN", 0),
        ByteField("more_flags", 0),
        ByteField("reserved", 0),
        BitField("DODAGID", 0, 128),
        ByteField("optionType", 0),
        ByteField("optionLength", 0),
        ByteField("prefixLength", 0),
        ByteField("flag", 0),
        IntField("routeLifetime", 0),
        LongField("prefix", 0)
    ]

# dao header
class Icmpv6_dao(Packet):
    name = "Icmpv6_dao"
    fields_desc = [
        ByteField("type", 0),
        ByteField("code", 0),
        ShortField("checksum", 0),
        ByteField("RPLInstanceID", 0),
        ByteField("flag", 0),
        ByteField("reserved", 0),
        ByteField("seq", 0),
        BitField("DODAGID", 0, 128),
        ByteField("rplTarget", 0),
        ByteField("length", 0),
        ByteField("rplReserved", 0),
        ByteField("rplLength", 0),
        BitField("prefixTarget", 0, 128),
        ByteField("optType", 0),
        ByteField("optLength", 0),
        ByteField("optFlags", 0),
        ByteField("optPathControl", 0),
        ByteField("optPathSeq", 0),
        ByteField("optPathLifetime", 0),
        BitField("parent", 0, 128)
    ]

class Icmpv6_dao_repeated(Packet):
    name = "Icmpv6_dao_repeated"
    fields_desc = [
        ByteField("type", 0),
        ByteField("code", 0),
        ShortField("checksum", 0),
        ByteField("RPLInstanceID", 0),
        ByteField("flag", 0),
        ByteField("reserved", 0),
        ByteField("seq", 0),
        BitField("DODAGID", 0, 128),
        ByteField("optionType", 0),
        ByteField("optionLength", 0),
        ByteField("rplReserved", 0),
        ByteField("prefixLength", 0),
        BitField("prefix", 0, 128)
    ]

class Icmpv6_dao_repeated1(Packet):
    name = "Icmpv6_dao_repeated1"
    fields_desc = [
        ByteField("type", 0),
        ByteField("code", 0),
        ShortField("checksum", 0),
        ByteField("RPLInstanceID", 0),
        ByteField("flag", 0),
        ByteField("reserved", 0),
        ByteField("seq", 0),
        BitField("DODAGID", 0, 128),
        ByteField("optionType1", 0),
        ByteField("optionLength1", 0),
        ByteField("rplReserved1", 0),
        ByteField("prefixLength1", 0),
        BitField("prefix1", 0, 128),
        ByteField("optionType2", 0),
        ByteField("optionLength2", 0),
        ByteField("rplReserved2", 0),
        ByteField("prefixLength2", 0),
        BitField("prefix2", 0, 128)
    ]

class Icmpv6_dao_repeated2(Packet):
    name = "Icmpv6_dao_repeated2"
    fields_desc = [
        ByteField("type", 0),
        ByteField("code", 0),
        ShortField("checksum", 0),
        ByteField("RPLInstanceID", 0),
        ByteField("flag", 0),
        ByteField("reserved", 0),
        ByteField("seq", 0),
        BitField("DODAGID", 0, 128),
        ByteField("optionType1", 0),
        ByteField("optionLength1", 0),
        ByteField("rplReserved1", 0),
        ByteField("prefixLength1", 0),
        BitField("prefix1", 0, 128),
        ByteField("optionType2", 0),
        ByteField("optionLength2", 0),
        ByteField("rplReserved2", 0),
        ByteField("prefixLength2", 0),
        BitField("prefix2", 0, 128),
        ByteField("optionType3", 0),
        ByteField("optionLength3", 0),
        ByteField("rplReserved3", 0),
        ByteField("prefixLength3", 0),
        BitField("prefix3", 0, 128)
    ]

class Icmpv6_dao_repeated3(Packet):
    name = "Icmpv6_dao_repeated3"
    fields_desc = [
        ByteField("type", 0),
        ByteField("code", 0),
        ShortField("checksum", 0),
        ByteField("RPLInstanceID", 0),
        ByteField("flag", 0),
        ByteField("reserved", 0),
        ByteField("seq", 0),
        BitField("DODAGID", 0, 128),
        ByteField("optionType1", 0),
        ByteField("optionLength1", 0),
        ByteField("rplReserved1", 0),
        ByteField("prefixLength1", 0),
        BitField("prefix1", 0, 128),
        ByteField("optionType2", 0),
        ByteField("optionLength2", 0),
        ByteField("rplReserved2", 0),
        ByteField("prefixLength2", 0),
        BitField("prefix2", 0, 128),
        ByteField("optionType3", 0),
        ByteField("optionLength3", 0),
        ByteField("rplReserved3", 0),
        ByteField("prefixLength3", 0),
        BitField("prefix3", 0, 128),
        ByteField("optionType4", 0),
        ByteField("optionLength4", 0),
        ByteField("rplReserved4", 0),
        ByteField("prefixLength4", 0),
        BitField("prefix4", 0, 128)
    ]

class Icmpv6_dao_repeated4(Packet):
    name = "Icmpv6_dao_repeated4"
    fields_desc = [
        ByteField("type", 0),
        ByteField("code", 0),
        ShortField("checksum", 0),
        ByteField("RPLInstanceID", 0),
        ByteField("flag", 0),
        ByteField("reserved", 0),
        ByteField("seq", 0),
        BitField("DODAGID", 0, 128),
        ByteField("optionType1", 0),
        ByteField("optionLength1", 0),
        ByteField("rplReserved1", 0),
        ByteField("prefixLength1", 0),
        BitField("prefix1", 0, 128),
        ByteField("optionType2", 0),
        ByteField("optionLength2", 0),
        ByteField("rplReserved2", 0),
        ByteField("prefixLength2", 0),
        BitField("prefix2", 0, 128),
        ByteField("optionType3", 0),
        ByteField("optionLength3", 0),
        ByteField("rplReserved3", 0),
        ByteField("prefixLength3", 0),
        BitField("prefix3", 0, 128),
        ByteField("optionType4", 0),
        ByteField("optionLength4", 0),
        ByteField("rplReserved4", 0),
        ByteField("prefixLength4", 0),
        BitField("prefix4", 0, 128),
        ByteField("optionType5", 0),
        ByteField("optionLength5", 0),
        ByteField("rplReserved5", 0),
        ByteField("prefixLength5", 0),
        BitField("prefix5", 0, 128)
    ]

# dao-ack header
class Icmpv6_daoack(Packet):
    name = "Icmpv6_daoack"
    fields_desc = [
        ByteField("type", 0),
        ByteField("code", 0),
        ShortField("checksum", 0),
        ByteField("RPLInstanceID", 0),
        ByteField("flag", 0),
        ByteField("seq", 0),
        ByteField("status", 0),
        BitField("DODAGID", 0, 128),
    ]