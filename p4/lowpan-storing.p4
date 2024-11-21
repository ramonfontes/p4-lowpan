/* -*- P4_16 -*- */
#include <core.p4>
#include <v1model.p4>

/*************************************************************************
*********************** H E A D E R S  ***********************************
*************************************************************************/

typedef bit<9>  egressSpec_t;
typedef bit<48> macAddr_t;
typedef bit<32> ipv4Addr_t;
typedef bit<16> tcpPort_t;
typedef bit<128> ipv6Addr_t;


// Cabeçalho 6LoWPAN
header lowpan_t {
    bit<16>  dispatch; // Tipo de pacote (IPv6, Fragmentação, etc.)
    bit<16>  identification; // Identificação para fragmentação
    bit<16>  ha_len;
    bit<64>  unsed;
    bit<16>  ethType;
}

header ethernet_t {
    macAddr_t dstAddr;
    macAddr_t srcAddr;
    bit<16>   etherType;
}

header tcp_t {
    tcpPort_t srcPort;
    tcpPort_t dstPort;
    bit<32> seqNo;
    bit<32> ackNo;
    bit<4>  dataOffset;
    bit<4>  res;
    bit<8>  flags;
    bit<16> window;
    bit<16> checksum;
    bit<16> urgentPtr;
}

header ipv6_t {
    bit<4>    version;
    bit<8>    trafficClass;
    bit<20>   flowLabel;
    bit<16>   payloadLength;
    bit<8>    nextHeader;
    bit<8>    hopLimit;
    bit<128>  srcAddr;
    bit<128>  dstAddr;
}

header icmpv6_dio_t {
    bit<8>    type;
    bit<8>    code;
    bit<16>   checksum;
    // Campos adicionais específicos para RPL Control Message
    bit<8>    RPLInstanceID;
    bit<8>    version;
    bit<16>   rank;
    bit<8>    flags;
    bit<8>    DTSN;
    bit<8>   more_flags;
    bit<8>   reserved;
    bit<128>  DODAGID;
    // Opção de Roteamento
    bit<8>    optionType;
    bit<8>    optionLength;
    bit<8>    prefixLength;
    bit<8>    flag;
    bit<32>   routeLifetime;
    bit<64>  prefix;
}

header icmpv6_daoack_t {
    bit<8>    type;
    bit<8>    code;
    bit<16>   checksum;
    bit<8>    RPLInstanceID;
    bit<8>    flag;
    bit<8>    seq;
    bit<8>    status;
    bit<128>  DODAGID;
}

header icmpv6_dis_t {
    bit<8>    type;
    bit<8>    code;
    bit<16>   checksum;
    bit<8>    flags;
    bit<8>    reserved;
}

header icmpv6_dao_repeated_t {
bit<8>    type;
    bit<8>    code;
    bit<16>   checksum;
    bit<8>    RPLInstanceID;
    bit<8>    flag;
    bit<8>    reserved;
    bit<8>    seq;
    bit<128>  DODAGID;
    bit<8>    optionType;
    bit<8>    optionLength;
    bit<8>    rplReserved;
    bit<8>    prefixLength;
    bit<128>  prefix;
}

header icmpv6_dao_repeated1_t {
    bit<8>    type;
    bit<8>    code;
    bit<16>   checksum;
    bit<8>    RPLInstanceID;
    bit<8>    flag;
    bit<8>    reserved;
    bit<8>    seq;
    bit<128>  DODAGID;
    bit<8>    optionType1;
    bit<8>    optionLength1;
    bit<8>    rplReserved1;
    bit<8>    prefixLength1;
    bit<128>  prefix1;
    bit<8>    optionType2;
    bit<8>    optionLength2;
    bit<8>    rplReserved2;
    bit<8>    prefixLength2;
    bit<128>  prefix2;
}

header icmpv6_dao_repeated2_t {
bit<8>    type;
    bit<8>    code;
    bit<16>   checksum;
    bit<8>    RPLInstanceID;
    bit<8>    flag;
    bit<8>    reserved;
    bit<8>    seq;
    bit<128>  DODAGID;
    bit<8>    optionType1;
    bit<8>    optionLength1;
    bit<8>    rplReserved1;
    bit<8>    prefixLength1;
    bit<128>  prefix1;
    bit<8>    optionType2;
    bit<8>    optionLength2;
    bit<8>    rplReserved2;
    bit<8>    prefixLength2;
    bit<128>  prefix2;
    bit<8>    optionType3;
    bit<8>    optionLength3;
    bit<8>    rplReserved3;
    bit<8>    prefixLength3;
    bit<128>  prefix3;
}

header icmpv6_dao_repeated3_t {
bit<8>    type;
    bit<8>    code;
    bit<16>   checksum;
    bit<8>    RPLInstanceID;
    bit<8>    flag;
    bit<8>    reserved;
    bit<8>    seq;
    bit<128>  DODAGID;
    bit<8>    optionType1;
    bit<8>    optionLength1;
    bit<8>    rplReserved1;
    bit<8>    prefixLength1;
    bit<128>  prefix1;
    bit<8>    optionType2;
    bit<8>    optionLength2;
    bit<8>    rplReserved2;
    bit<8>    prefixLength2;
    bit<128>  prefix2;
    bit<8>    optionType3;
    bit<8>    optionLength3;
    bit<8>    rplReserved3;
    bit<8>    prefixLength3;
    bit<128>  prefix3;
    bit<8>    optionType4;
    bit<8>    optionLength4;
    bit<8>    rplReserved4;
    bit<8>    prefixLength4;
    bit<128>  prefix4;
}

header icmpv6_dao_repeated4_t {
bit<8>    type;
    bit<8>    code;
    bit<16>   checksum;
    bit<8>    RPLInstanceID;
    bit<8>    flag;
    bit<8>    reserved;
    bit<8>    seq;
    bit<128>  DODAGID;
    bit<8>    optionType1;
    bit<8>    optionLength1;
    bit<8>    rplReserved1;
    bit<8>    prefixLength1;
    bit<128>  prefix1;
    bit<8>    optionType2;
    bit<8>    optionLength2;
    bit<8>    rplReserved2;
    bit<8>    prefixLength2;
    bit<128>  prefix2;
    bit<8>    optionType3;
    bit<8>    optionLength3;
    bit<8>    rplReserved3;
    bit<8>    prefixLength3;
    bit<128>  prefix3;
    bit<8>    optionType4;
    bit<8>    optionLength4;
    bit<8>    rplReserved4;
    bit<8>    prefixLength4;
    bit<128>  prefix4;
    bit<8>    optionType5;
    bit<8>    optionLength5;
    bit<8>    rplReserved5;
    bit<8>    prefixLength5;
    bit<128>  prefix5;
}

header icmpv6_dao_t {
    bit<8>    type;
    bit<8>    code;
    bit<16>   checksum;
    bit<8>    RPLInstanceID;
    bit<8>    flag;
    bit<8>    reserved;
    bit<8>    seq;
    bit<128>  DODAGID;
}

header metadata_t {
    bit<8>  custom_value;
}

struct metadata {
    metadata_t meta;
}

struct headers {
    ethernet_t   ethernet;
    lowpan_t   lowpan;
    ipv6_t     ipv6;
    icmpv6_dio_t   icmpv6_dio;
    icmpv6_daoack_t icmpv6_daoack;
    icmpv6_dao_t icmpv6_dao;
    icmpv6_dao_repeated_t icmpv6_dao_repeated;
    icmpv6_dao_repeated1_t icmpv6_dao_repeated1;
    icmpv6_dao_repeated2_t icmpv6_dao_repeated2;
    icmpv6_dao_repeated3_t icmpv6_dao_repeated3;
    icmpv6_dao_repeated4_t icmpv6_dao_repeated4;
    icmpv6_dis_t icmpv6_dis;
}

/*************************************************************************
*********************** P A R S E R  ***********************************
*************************************************************************/

parser MyParser(packet_in packet,
                out headers hdr,
                inout metadata meta,
                inout standard_metadata_t standard_metadata) {

    state start {
        packet.extract(hdr.lowpan);
        transition select(hdr.lowpan.ethType) {
            0x86dd: parse_ipv6; 
            default: accept;
        }
    }
   
    state parse_ipv6 {
        packet.extract(hdr.ipv6);
        transition select(hdr.ipv6.payloadLength, hdr.ipv6.srcAddr) {
            (0x2C, 0xff02_0000_0000_0000_0000_0000_0000_001a): parse_icmpv6_dio;
            (0x06, _): parse_icmpv6_dis; //6
            (0x2C, _): parse_icmpv6_dao_repeated; //44
            (0x40, _): parse_icmpv6_dao_repeated1; //64
            (0x54, _): parse_icmpv6_dao_repeated2; //84
            (0x68, _): parse_icmpv6_dao_repeated3; //104
            (0x7c, _): parse_icmpv6_dao_repeated4; //124
            (0x18, _): parse_icmpv6_daoack; //24
            #default: accept;
        }
    }

    state parse_icmpv6_dio {
        packet.extract(hdr.icmpv6_dio);
        meta.meta.custom_value = hdr.icmpv6_dio.code;
        transition accept;
    }

    state parse_icmpv6_dis {
        packet.extract(hdr.icmpv6_dis);
        meta.meta.custom_value = hdr.icmpv6_dis.code;
        transition accept;
    }

    state parse_icmpv6_dao_repeated {
        packet.extract(hdr.icmpv6_dao_repeated);
        meta.meta.custom_value = hdr.icmpv6_dao_repeated.code;
        transition accept;
    }

    state parse_icmpv6_dao_repeated1 {
        packet.extract(hdr.icmpv6_dao_repeated1);
        meta.meta.custom_value = hdr.icmpv6_dao_repeated1.code;
        transition accept;
    }

    state parse_icmpv6_dao_repeated2 {
        packet.extract(hdr.icmpv6_dao_repeated2);
        meta.meta.custom_value = hdr.icmpv6_dao_repeated2.code;
        transition accept;
    }

    state parse_icmpv6_dao_repeated3 {
        packet.extract(hdr.icmpv6_dao_repeated3);
        meta.meta.custom_value = hdr.icmpv6_dao_repeated3.code;
        transition accept;
    }

    state parse_icmpv6_dao_repeated4 {
        packet.extract(hdr.icmpv6_dao_repeated4);
        meta.meta.custom_value = hdr.icmpv6_dao_repeated4.code;
        transition accept;
    }

    state parse_icmpv6_daoack {
        packet.extract(hdr.icmpv6_daoack);
        meta.meta.custom_value = hdr.icmpv6_daoack.code;
        transition accept;
    }
}

/*************************************************************************
************   C H E C K S U M    V E R I F I C A T I O N   *************
*************************************************************************/

control MyVerifyChecksum(inout headers hdr, inout metadata meta) {
    apply {  }
}

/*************************************************************************
**************  I N G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyIngress(inout headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {

    action drop() {
        mark_to_drop(standard_metadata);
    }

    action set_egress_port(egressSpec_t port) {
        if (meta.meta.custom_value == 0x0 || meta.meta.custom_value == 0x1 || meta.meta.custom_value == 0x2 || meta.meta.custom_value == 0x3){
            if (meta.meta.custom_value == 0x0) {
                hdr.ethernet.etherType = 0x1000; //dis
            }
            else if (meta.meta.custom_value == 0x1) {
                hdr.ethernet.etherType = 0x1001; //dio
            }
            else if (meta.meta.custom_value == 0x2) {
                hdr.ethernet.etherType = 0x1002; //dao
            }
            else if (meta.meta.custom_value == 0x3) {
                hdr.ethernet.etherType = 0x1003; //daoack
            }             
            standard_metadata.egress_spec = port;
        }
        else{
            standard_metadata.egress_spec = 0;
        }
    }

    table port_table {
        key = {
            standard_metadata.ingress_port: exact;
        }
        actions = {
            set_egress_port;
            drop;
        }
        size = 256;
        default_action = drop();
    }

    apply {
        hdr.ethernet.setValid();
        #hdr.lowpan.unsed = 1111111111111111111111111111111;
        #hdr.ethernet.dstAddr = 0x112233445566;
        #hdr.ethernet.srcAddr = 0x665544332211;
        port_table.apply();
    }
}

/*************************************************************************
****************  E G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyEgress(inout headers hdr,
                 inout metadata meta,
                 inout standard_metadata_t standard_metadata) {
    apply { 
          }
}

/*************************************************************************
*************   C H E C K S U M    C O M P U T A T I O N   **************
*************************************************************************/

control MyComputeChecksum(inout headers hdr, inout metadata meta) {
     apply {
     }
}

/*************************************************************************
***********************  D E P A R S E R  *******************************
*************************************************************************/

control MyDeparser(packet_out packet, in headers hdr) {
    apply {
        packet.emit(hdr.ethernet);
        packet.emit(hdr.lowpan);
        packet.emit(hdr.ipv6);
        packet.emit(hdr.icmpv6_dio);
        packet.emit(hdr.icmpv6_dao);
        packet.emit(hdr.icmpv6_dao_repeated);
        packet.emit(hdr.icmpv6_dao_repeated1);
        packet.emit(hdr.icmpv6_dao_repeated2);
        packet.emit(hdr.icmpv6_dao_repeated3);
        packet.emit(hdr.icmpv6_dao_repeated4);
        packet.emit(hdr.icmpv6_daoack);
        packet.emit(hdr.icmpv6_dis);
    }
}

/*************************************************************************
***********************  S W I T C H  *******************************
*************************************************************************/

//switch architecture
V1Switch(
    MyParser(),
    MyVerifyChecksum(),
    MyIngress(),
    MyEgress(),
    MyComputeChecksum(),
    MyDeparser()
) main;
