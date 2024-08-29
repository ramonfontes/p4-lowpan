import logging
from collections import defaultdict
from scapy.all import *
from scapy.fields import *
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
rank = defaultdict(list)
srcAddress = ""
rootNode = ""

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/api', methods=['GET'])
def api_home():
    return jsonify(dict(rank))

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.json
    return jsonify({"received_data": data})

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
bind_layers(IPv6Custom2, Icmpv6_dao_repeated, payloadLength=44)
bind_layers(IPv6Custom2, Icmpv6_dao_repeated1, payloadLength=64)
bind_layers(IPv6Custom2, Icmpv6_dao_repeated2, payloadLength=84)
bind_layers(IPv6Custom2, Icmpv6_dao_repeated3, payloadLength=104)
bind_layers(IPv6Custom2, Icmpv6_dao_repeated4, payloadLength=124)

bind_layers(Ether, Lowpan3, type=0x1003)
bind_layers(Lowpan3, IPv6Custom3)
bind_layers(IPv6Custom3, Icmpv6_daoack)


def decimal_para_binario(numero_decimal):
    if numero_decimal == 0:
        return "0"
    binario = ""

    while numero_decimal > 0:
        binario = str(numero_decimal % 2) + binario
        numero_decimal = numero_decimal // 2

    return binario


# Função auxiliar para converter bytes para o formato IPv6
def convert_to_ipv6(decimal_value):
    address_bytes = decimal_value.to_bytes(16, byteorder='big')
    return inet_ntop(socket.AF_INET6, address_bytes)


def remove_value_from_lists(d, value):
    for key in d:
        if value in d[key]:
            d[key] = [x for x in d[key] if x != value]


def packet_handler(packet):
    global srcAddress
    global rank

    #if Ether in packet:
    #    ethertype = packet[Ether].type
    #    print(hex(ethertype))

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
        #print("::::::::::::::::::::IPv6 Header::::::::::::::::::::::")
        #print(f"Version: {ipv6_layer.version}")
        #print(f"Traffic Class: {ipv6_layer.trafficClass}")
        #print(f"Flow Label: {ipv6_layer.flowLabel}")
        #print(f"Payload Length: {ipv6_layer.payloadLength}")
        #print(f"Next Header: {ipv6_layer.nextHeader}")
        #print(f"Hop Limit: {ipv6_layer.hopLimit}")
        #print(f"Src Addr: {ipv6_layer.srcAddr}")
        #print(f"Dst Addr: {ipv6_layer.dstAddr}\n")
        srcAddress = ipv6_layer.srcAddr

    if packet.haslayer(IPv6Custom1):
        ipv6_layer = packet.getlayer(IPv6Custom1)
        srcAddress = ipv6_layer.srcAddr

    if packet.haslayer(IPv6Custom2):
        ipv6_layer = packet.getlayer(IPv6Custom2)
        srcAddress = ipv6_layer.srcAddr

    if packet.haslayer(IPv6Custom3):
        ipv6_layer = packet.getlayer(IPv6Custom3)
        srcAddress = ipv6_layer.srcAddr

    if packet.haslayer(Icmpv6_dis):
        icmpv6_layer = packet.getlayer(Icmpv6_dis)
        print("::::::::::::::::::::Icmpv6 DIS Header::::::::::::::::::::")
        #print(f"Type: {icmpv6_layer.type}")
        print(srcAddress)

    if packet.haslayer(Icmpv6_dio):
        #icmpv6_layer = packet.getlayer(Icmpv6_dio)
        #print("::::::::::::::::::::Icmpv6 DIO Header::::::::::::::::::::")
        #print(f"RPLInstanceID: {icmpv6_layer.RPLInstanceID}")
        #print(f"Version: {icmpv6_layer.version}")
        #print(f"Rank: {icmpv6_layer.rank}")
        """flags = decimal_para_binario(icmpv6_layer.flags)
        print(f"Flags: {flags}")
        if (flags[0]=="1"):
            print(f" -- Grounded")
        else:
            print(f" -- No Grounded")
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
            print(f" -- xxxxxxxxxxxxxxx")"""
    #    print(f"DTSN: {icmpv6_layer.DTSN}")
    #    dodagid_ipv6 = convert_to_ipv6(icmpv6_layer.DODAGID)
        #print(f"DODAGID: {dodagid_ipv6}")
    #    print(f"Node: {srcAddress}")
        #print(f"Prefix Length: {icmpv6_layer.prefixLength}")
        #print(f"Flag: {icmpv6_layer.flag}")
        #print(f"Route Lifetime: Infinity({icmpv6_layer.routeLifetime})")
        #prefix = convert_to_ipv6(icmpv6_layer.prefix)
        #print(f"Prefix: {prefix}")
    #    print("=========================================\n")

     #   if icmpv6_layer.rank != 0 and srcAddress:
      #      remove_value_from_lists(rank, srcAddress)
       #     rank[icmpv6_layer.rank].append(srcAddress)
        #    srcAddress = ""

    if packet.haslayer(Icmpv6_dao_repeated):
        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated)
        print("::::::::::::::::::::Icmpv6 DAO Header::::::::::::::::::::")
        #print(f"RPLInstanceID: {icmpv6_layer.RPLInstanceID}")
        #flags = decimal_para_binario(icmpv6_layer.flag)
        #print(f"Flags: {flags}")
        #print(f"Reserved: {icmpv6_layer.reserved}")
        #dodagid_ipv6 = convert_to_ipv6(icmpv6_layer.DODAGID)
        #print(f"DODAGID: {dodagid_ipv6}")
        #print(f"Prefix Length: {icmpv6_layer.prefixLength}")
        #print("=========================================\n")
        rootNode = convert_to_ipv6(icmpv6_layer.DODAGID)
        item = [rootNode, convert_to_ipv6(icmpv6_layer.prefix)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)

    if packet.haslayer(Icmpv6_dao_repeated1):
        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated1)
        rootNode = convert_to_ipv6(icmpv6_layer.DODAGID)
        item = [rootNode, convert_to_ipv6(icmpv6_layer.prefix1)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix1), convert_to_ipv6(icmpv6_layer.prefix2)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)

    if packet.haslayer(Icmpv6_dao_repeated2):
        print("::::::::::::::::::::Icmpv6 DAO Header::::::::::::::::::::")
        """if ipv6_layer.payloadLength == 84:
            icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated2)
            print(f"DODAGID: {convert_to_ipv6(icmpv6_layer.DODAGID)}")
            print(f"Prefix1: {convert_to_ipv6(icmpv6_layer.prefix1)}")
            print(f"Prefix2: {convert_to_ipv6(icmpv6_layer.prefix2)}")
            print(f"Prefix3: {convert_to_ipv6(icmpv6_layer.prefix3)}")
            print(f"Prefix Length1: {icmpv6_layer.prefixLength1}")
            print(f"Prefix Length1: {icmpv6_layer.prefixLength2}")
            print(f"Prefix Length1: {icmpv6_layer.prefixLength3}")
            print(icmpv6_layer.prefix3)
        print(srcAddress)"""
        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated2)
        rootNode = convert_to_ipv6(icmpv6_layer.DODAGID)
        item = [rootNode, convert_to_ipv6(icmpv6_layer.prefix1)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix1), convert_to_ipv6(icmpv6_layer.prefix2)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix2), convert_to_ipv6(icmpv6_layer.prefix3)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)

    if packet.haslayer(Icmpv6_dao_repeated3):
        print("::::::::::::::::::::Icmpv6 DAO Header::::::::::::::::::::")
        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated3)
        rootNode = convert_to_ipv6(icmpv6_layer.DODAGID)
        item = [rootNode, convert_to_ipv6(icmpv6_layer.prefix1)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix1), convert_to_ipv6(icmpv6_layer.prefix2)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix2), convert_to_ipv6(icmpv6_layer.prefix3)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix3), convert_to_ipv6(icmpv6_layer.prefix4)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)

    if packet.haslayer(Icmpv6_dao_repeated4):
        print("::::::::::::::::::::Icmpv6 DAO Header::::::::::::::::::::")
        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated4)
        rootNode = convert_to_ipv6(icmpv6_layer.DODAGID)
        item = [rootNode, convert_to_ipv6(icmpv6_layer.prefix1)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix1), convert_to_ipv6(icmpv6_layer.prefix2)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix2), convert_to_ipv6(icmpv6_layer.prefix3)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix3), convert_to_ipv6(icmpv6_layer.prefix4)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix4), convert_to_ipv6(icmpv6_layer.prefix5)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)

    """if packet.haslayer(Icmpv6_daoack):
        #icmpv6_layer = packet.getlayer(Icmpv6_daoack)
        print("::::::::::::::::::::Icmpv6 DAOACK Header::::::::::::::::::::")
        #print(f"RPLInstanceID: {icmpv6_layer.RPLInstanceID}")
        print(srcAddress)"""


# Função para sniffar pacotes
def packet_sniffer():
    # Inicia o sniffer
    sniff(iface="h1-eth1", filter="ether proto 0x1000 or ether proto 0x1001 or ether proto 0x1002 or ether proto 0x1003", prn=packet_handler)

if __name__ == '__main__':
    sniffer_thread = threading.Thread(target=packet_sniffer)
    sniffer_thread.daemon = True  # Permite que a thread seja encerrada ao fechar o programa
    sniffer_thread.start()

    app.run(host='10.0.0.1', port=5000)

