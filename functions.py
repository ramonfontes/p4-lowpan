from scapy.all import *

def decimal_to_binary(decimal_value):
    if decimal_value == 0:
        return "0"
    binary = ""

    while binary > 0:
        binary = str(decimal_value % 2) + binary
        decimal_value = decimal_value // 2

    return decimal_value

# Função auxiliar para converter bytes para o formato IPv6
def convert_to_ipv6(decimal_value):
    address_bytes = decimal_value.to_bytes(16, byteorder='big')
    return inet_ntop(socket.AF_INET6, address_bytes)

def set_packet_size(srcAddress, packet, packet_size):
    # if srcAddress != "::":
    if '::' in srcAddress and srcAddress != "::":
        if srcAddress in packet_size:
            packet_size[srcAddress] += len(packet)
            return packet_size
        else:
            packet_size[srcAddress] = len(packet)
            return packet_size