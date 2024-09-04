import logging
from collections import defaultdict
from scapy.all import *
from scapy.fields import *
from flask import Flask, jsonify, request
from flask_cors import CORS
from headers import *

app = Flask(__name__)
CORS(app)
rank = defaultdict(list)
packet_size = defaultdict(list)
srcAddress = ""
rootNode = ""

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/api', methods=['GET'])
def api_home():
    return jsonify(dict(rank))

@app.route('/api/packet_size', methods=['GET'])
def api_packet_size():
    return jsonify(dict(packet_size))

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.json
    return jsonify({"received_data": data})


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


def set_packet_size(srcAddress, packet):
    global packet_size
    if (srcAddress != "::"):
        if srcAddress in packet_size:
            packet_size[srcAddress] += len(packet)
        else:
            packet_size[srcAddress] = len(packet)


def packet_handler(packet):
    global srcAddress
    global rank

    if packet.haslayer(IPv6Custom):
        ipv6_layer = packet.getlayer(IPv6Custom)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, packet)

    if packet.haslayer(IPv6Custom1):
        ipv6_layer = packet.getlayer(IPv6Custom1)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, packet)

    if packet.haslayer(IPv6Custom2):
        ipv6_layer = packet.getlayer(IPv6Custom2)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, packet)

    if packet.haslayer(IPv6Custom3):
        ipv6_layer = packet.getlayer(IPv6Custom3)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, packet)

    if packet.haslayer(Icmpv6_dao_repeated):
        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated)
        print("::::::::::::::::::::Icmpv6 DAO Header::::::::::::::::::::")
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
        if ipv6_layer.payloadLength == 84:
            icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated2)
            print(f"DODAGID: {convert_to_ipv6(icmpv6_layer.DODAGID)}")
            print(f"Prefix1: {convert_to_ipv6(icmpv6_layer.prefix1)}")
            print(f"Prefix2: {convert_to_ipv6(icmpv6_layer.prefix2)}")
            print(f"Prefix3: {convert_to_ipv6(icmpv6_layer.prefix3)}")
            print(f"Prefix Length1: {icmpv6_layer.prefixLength1}")
            print(f"Prefix Length1: {icmpv6_layer.prefixLength2}")
            print(f"Prefix Length1: {icmpv6_layer.prefixLength3}")
            print(icmpv6_layer.prefix3)
        print(srcAddress)
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


# Função para sniffar pacotes
def packet_sniffer():
    # Inicia o sniffer
    sniff(iface="h1-eth1", filter="ether proto 0x1000 or ether proto 0x1001 or ether proto 0x1002 or ether proto 0x1003", prn=packet_handler)

if __name__ == '__main__':
    sniffer_thread = threading.Thread(target=packet_sniffer)
    sniffer_thread.daemon = True  # Permite que a thread seja encerrada ao fechar o programa
    sniffer_thread.start()

    app.run(host='192.168.210.1', port=5000)