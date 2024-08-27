from collections import defaultdict
from scapy.all import *
from scapy.fields import *

rank = defaultdict(list)

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
        ByteField("optionType", 0),
        ByteField("optionLength", 0),
        ByteField("rplReserved", 0),
        ByteField("prefixLength", 0),
        LongField("prefix", 0)
    ]

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

class Icmpv6_dis(Packet):
    name = "Icmpv6_dis"
    fields_desc = [
        ByteField("type", 0),
        ByteField("code", 0),
        ShortField("checksum", 0),
        ByteField("flags", 0),
        ByteField("reserved", 0),
    ]

# Define a classe para capturar o pacote completo
# Combine as camadas
class MyPacket(Packet):
    name = "MyPacket"
    fields_desc = [
        ShortField("len", 0),
        StrField("payload", b"")
    ]

bind_layers(Ether, Lowpan, type=0x1000)
bind_layers(Lowpan, IPv6Custom)
bind_layers(IPv6Custom, Icmpv6_dis)

bind_layers(Ether, Lowpan1, type=0x1001)
bind_layers(Lowpan1, IPv6Custom1)
bind_layers(IPv6Custom1, Icmpv6_dio)

bind_layers(Ether, Lowpan2, type=0x1002)
bind_layers(Lowpan2, IPv6Custom2)
bind_layers(IPv6Custom2, Icmpv6_dio)

bind_layers(Ether, Lowpan3, type=0x1003)
bind_layers(Lowpan3, IPv6Custom3)
bind_layers(IPv6Custom3, Icmpv6_daoack)


#bind_layers(IPv6Custom, Icmpv6_dio)
#bind_layers(IPv6Custom, Icmpv6_dao)
#bind_layers(IPv6Custom, Icmpv6_daoack)
#bind_layers(IPv6Custom, Icmpv6_dio, payloadLength=44)
#bind_layers(IPv6Custom, Icmpv6_dis, payloadLength=6)
#bind_layers(IPv6Custom, Icmpv6_dao, payloadLength=44)
#bind_layers(IPv6Custom, Icmpv6_daoack, payloadLength=24)

def decimal_para_binario(numero_decimal):
    # Verifica se o número é zero
    if numero_decimal == 0:
        return "0"

    # Variável para armazenar o resultado binário
    binario = ""

    # Loop para converter decimal em binário
    while numero_decimal > 0:
        binario = str(numero_decimal % 2) + binario
        numero_decimal = numero_decimal // 2

    return binario

# Função auxiliar para converter bytes para o formato IPv6
def convert_to_ipv6(decimal_value):
    # Converte o valor decimal em 16 bytes
    address_bytes = decimal_value.to_bytes(16, byteorder='big')
    # Converte para o formato IPv6 legível
    return inet_ntop(socket.AF_INET6, address_bytes)

def packet_handler(packet):
    """if packet.haslayer(Lowpan):
        lowpan_layer = packet.getlayer(Lowpan)
        print("Lowpan Header::::::::::::::::::::")
        print(f"Dispatch: {lowpan_layer.dispatch}")
        print(f"Identification: {lowpan_layer.identification}")
        print(f"HA Len: {lowpan_layer.ha_len}")
        print(f"Unused: {lowpan_layer.unused}")
        print(f"EthType: {hex(lowpan_layer.ethType)}")"""

    if packet.haslayer(IPv6Custom):
        ipv6_layer = packet.getlayer(IPv6Custom)
        print("::::::::::::::::::::IPv6 Header::::::::::::::::::::::")
        #print(f"Version: {ipv6_layer.version}")
        print(f"Traffic Class: {ipv6_layer.trafficClass}")
        #print(f"Flow Label: {ipv6_layer.flowLabel}")
        #print(f"Payload Length: {ipv6_layer.payloadLength}")
        #print(f"Next Header: {ipv6_layer.nextHeader}")
        print(f"Hop Limit: {ipv6_layer.hopLimit}")
        print(f"Src Addr: {ipv6_layer.srcAddr}")
        print(f"Dst Addr: {ipv6_layer.dstAddr}\n")

    if packet.haslayer(Icmpv6_dis):
        icmpv6_layer = packet.getlayer(Icmpv6_dis)
        print("::::::::::::::::::::Icmpv6 DIS Header::::::::::::::::::::")
        print(f"Type: {icmpv6_layer.type}")

    if packet.haslayer(Icmpv6_dio):
        icmpv6_layer = packet.getlayer(Icmpv6_dio)
        print("::::::::::::::::::::Icmpv6 DIO Header::::::::::::::::::::")
        print(f"RPLInstanceID: {icmpv6_layer.RPLInstanceID}")
        print(f"Version: {icmpv6_layer.version}")
        print(f"Rank: {icmpv6_layer.rank}")
        flags = decimal_para_binario(icmpv6_layer.flags)
        print(f"Flags: {flags}")
        if (flags[0]=="1"):
            print(f" -- Grounded")
        else:
            print(f" -- No Grounded")
        print(flags)
        if (flags[1]=="0"):
            print(f" -- Zero: False")
        else:
            print(f" -- Zero: True")
        if (flags[2:5]=="010"):
            print(f" -- Storing Mode with no muticast")
        else:
            print(f" -- xxxxxxxxxxxxxxx")
        if (flags[5:8]=="000"):
            print(f" -- Dodag Preference: 0")
        else:
            print(f" -- xxxxxxxxxxxxxxx")
        print(f"DTSN: {icmpv6_layer.DTSN}")
        dodagid_ipv6 = convert_to_ipv6(icmpv6_layer.DODAGID)
        print(f"DODAGID: {dodagid_ipv6}")
        print(f"Prefix Length: {icmpv6_layer.prefixLength}")
        print(f"Flag: {icmpv6_layer.flag}")
        print(f"Route Lifetime: Infinity({icmpv6_layer.routeLifetime})")
        prefix = convert_to_ipv6(icmpv6_layer.prefix)
        print(f"Prefix: {prefix}")
        print("=========================================\n")

        if (dodagid_ipv6 not in rank[icmpv6_layer.rank]):
            rank[icmpv6_layer.rank].append(dodagid_ipv6)
        print(rank)

    if packet.haslayer(Icmpv6_dao):
        icmpv6_layer = packet.getlayer(Icmpv6_dao)
        print("::::::::::::::::::::Icmpv6 DAO Header::::::::::::::::::::")
        print(f"RPLInstanceID: {icmpv6_layer.RPLInstanceID}")
        flags = decimal_para_binario(icmpv6_layer.flag)
        print(f"Flags: {flags}")
        print(f"Reserved: {icmpv6_layer.reserved}")
        dodagid_ipv6 = convert_to_ipv6(icmpv6_layer.DODAGID)
        print(f"DODAGID: {dodagid_ipv6}")
        print(f"Prefix Length: {icmpv6_layer.prefixLength}")
        print("=========================================\n")

    if packet.haslayer(Icmpv6_daoack):
        icmpv6_layer = packet.getlayer(Icmpv6_daoack)
        print("::::::::::::::::::::Icmpv6 DAOACK Header::::::::::::::::::::")
        print(f"RPLInstanceID: {icmpv6_layer.RPLInstanceID}")

sniff(iface="h1-eth0", filter="ether proto 0x1000 or ether proto 0x1001 or ether proto 0x1002 or ether proto 0x1003", prn=packet_handler)

