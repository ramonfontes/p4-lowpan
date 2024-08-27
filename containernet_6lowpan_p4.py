#!/usr/bin/python
"""
This is the simplest example to showcase Containernet with enabled and containerized P4 AP.
"""
import os

from containernet.net import Containernet
from containernet.node import DockerP4Sensor
from containernet.cli import CLI
from mininet.log import info, setLogLevel
from mn_wifi.sixLoWPAN.link import LoWPAN


def topology():
    net = Containernet(iot_module='mac802154_hwsim')

    info('*** Adding docker containers\n')
    path = os.path.dirname(os.path.abspath(__file__))
    json_file = '/root/teste.json' # container directory
    config = path + '/p4_files/commands_lowpan.txt'
    args = {'json': json_file, 'switch_config': config}

    info('*** Adding P4 AP\n')
    # IPBASE: subnet from eth0 interface,
    ap1 = net.addAPSensor('ap1', cls=DockerP4Sensor, ip6='fe80::1/64', panid='0xbeef',
                           dodag_root=True, storing_mode=2, privileged=True,
                           volumes=[path + "/p4_files:/root", "/tmp/.X11-unix:/tmp/.X11-unix:rw"],
                           dimage="ramonfontes/bmv2:lowpan", cpu_shares=20,
                           client_isolation=True, netcfg=True,
                           environment={"DISPLAY": ":0"}, loglevel="debug",
                           thriftport=50001,  IPBASE="172.17.0.0/16", **args)
    sensor1 = net.addSensor('sensor1', ip6='fe80::2/64', panid='0xbeef',
                            dodag_root=True, storing_mode=2)
    h1 = net.addHost('h1',  ip6='fe80::3/64')

    net.configureWifiNodes()

    #ap1.cmd("tcpdump -i ap1-pan0 -w teste.pcap &")
    info('*** Creating links\n')
    net.addLink(ap1, sensor1, cls=LoWPAN)
    net.addLink(ap1, h1)

    info('*** Starting network\n')
    net.build()
    ap1.start([])
    net.staticArp()

    net.configRPLD(net.sensors + net.apsensors)

    #ap1.cmd('tcpdump -i ap1-pan0 -w teste.pcap &')

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
