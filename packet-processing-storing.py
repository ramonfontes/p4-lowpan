import logging
from collections import defaultdict, OrderedDict
from scapy.all import *
from scapy.fields import *
from functions import *
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
    # Sort by Key
    ordered_rank = OrderedDict(sorted(rank.items()))
    return jsonify(ordered_rank)

@app.route('/api/packet_size', methods=['GET'])
def api_packet_size():
    # Sort by Key
    ordered_packet_size = OrderedDict(sorted(packet_size.items()))
    return jsonify(ordered_packet_size)

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.json
    return jsonify({"received_data": data})

bind_layers(Ether, Lowpan, type=0x1000)
bind_layers(Lowpan, IPv6Custom)
bind_layers(IPv6Custom, Icmpv6_dis)

bind_layers(Ether, Lowpan1, type=0x1001)
bind_layers(Lowpan1, IPv6Custom1)
bind_layers(IPv6Custom1, Icmpv6_dio)

bind_layers(Ether, Lowpan2, type=0x1002)
bind_layers(Lowpan2, IPv6Custom2)
bind_layers(IPv6Custom2, Icmpv6_dao_repeated, payloadLength=66)
bind_layers(IPv6Custom2, Icmpv6_dao_repeated1, payloadLength=86)
bind_layers(IPv6Custom2, Icmpv6_dao_repeated2, payloadLength=106)
bind_layers(IPv6Custom2, Icmpv6_dao_repeated3, payloadLength=126)
bind_layers(IPv6Custom2, Icmpv6_dao_repeated4, payloadLength=146)

bind_layers(Ether, Lowpan3, type=0x1003)
bind_layers(Lowpan3, IPv6Custom3)
bind_layers(IPv6Custom3, Icmpv6_daoack)


def packet_handler(packet):
    global srcAddress
    global rank
    global packet_size

    if packet.haslayer(IPv6Custom):
        ipv6_layer = packet.getlayer(IPv6Custom)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, Icmpv6_dis(), packet_size)

    if packet.haslayer(IPv6Custom1):
        ipv6_layer = packet.getlayer(IPv6Custom1)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, Icmpv6_dio(), packet_size)

    if packet.haslayer(IPv6Custom2):
        ipv6_layer = packet.getlayer(IPv6Custom2)
        srcAddress = ipv6_layer.srcAddr

    if packet.haslayer(IPv6Custom3):
        ipv6_layer = packet.getlayer(IPv6Custom3)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, Icmpv6_daoack(), packet_size)

    if packet.haslayer(Icmpv6_dao_repeated):
        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated)

        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, Icmpv6_dao_repeated(), packet_size)
        rootNode = convert_to_ipv6(icmpv6_layer.DODAGID)
        item = [rootNode, convert_to_ipv6(icmpv6_layer.prefix)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)

    if packet.haslayer(Icmpv6_dao_repeated1):
        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated1)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, Icmpv6_dao_repeated1(), packet_size)
        rootNode = convert_to_ipv6(icmpv6_layer.DODAGID)
        item = [rootNode, convert_to_ipv6(icmpv6_layer.prefix1)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)
        item = [convert_to_ipv6(icmpv6_layer.prefix1), convert_to_ipv6(icmpv6_layer.prefix2)]
        if item not in rank[rootNode]:
            rank[rootNode].append(item)

    if packet.haslayer(Icmpv6_dao_repeated2):
        """if ipv6_layer.payloadLength == 84:
            icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated2)
            print(f"DODAGID: {convert_to_ipv6(icmpv6_layer.DODAGID)}")
            print(f"Prefix1: {convert_to_ipv6(icmpv6_layer.prefix1)}")
            print(f"Prefix2: {convert_to_ipv6(icmpv6_layer.prefix2)}")
            print(f"Prefix3: {convert_to_ipv6(icmpv6_layer.prefix3)}")
            print(f"Prefix Length1: {icmpv6_layer.prefixLength1}")
            print(f"Prefix Length1: {icmpv6_layer.prefixLength2}")
            print(f"Prefix Length1: {icmpv6_layer.prefixLength3}")
            print(icmpv6_layer.prefix3)"""

        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated2)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, Icmpv6_dao_repeated2(), packet_size)
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
        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated3)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, Icmpv6_dao_repeated3(), packet_size)
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
        icmpv6_layer = packet.getlayer(Icmpv6_dao_repeated4)
        srcAddress = ipv6_layer.srcAddr
        set_packet_size(srcAddress, Icmpv6_dao_repeated4(), packet_size)
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
    for n in range(1, 11):
        os.system("echo \"{},{}\" > /var/www/localhost/htdocs/data{}.csv".format("date","Sensor {}".format(n), n))
    sniffer_thread = threading.Thread(target=packet_sniffer)
    sniffer_thread.daemon = True  # Permite que a thread seja encerrada ao fechar o programa
    sniffer_thread.start()

    app.run(host='192.168.210.1', port=5000)