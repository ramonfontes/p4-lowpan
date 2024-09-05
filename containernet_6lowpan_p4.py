#!/usr/bin/python
"""
This is the simplest example to showcase Containernet with enabled and containerized P4 AP.
"""
import os
import sys

from containernet.net import Containernet
from containernet.node import DockerP4Sensor
from containernet.cli import CLI
from mininet.log import info, setLogLevel
from mn_wifi.sixLoWPAN.link import LoWPAN
from mininet.term import makeTerm


def topology():
    net = Containernet(iot_module='mac802154_hwsim', ipBase='192.168.210.0/24')

    info('*** Adding docker containers\n')
    path = os.path.dirname(os.path.abspath(__file__))
    json_file = '/root/lowpan-non-storing.json' # container directory
    config = path + '/p4_commands.txt'
    args = {'json': json_file, 'switch_config': config}
    mode = 1
    dimage = 'ramonfontes/bmv2:lowpan'
    if '-s' in sys.argv:
        json_file = '/root/json/lowpan-storing.json'  # container directory
        config = path + '/p4_commands.txt'
        args = {'json': json_file, 'switch_config': config}
        mode = 2
        dimage = 'ramonfontes/bmv2:lowpan-storing'

    s1 = net.addSwitch("s1", failMode='standalone')

    info('*** Adding P4 AP\n')
    # IPBASE: subnet from eth0 interface,
    ap1 = net.addAPSensor('ap1', cls=DockerP4Sensor, ip6='fe80::1/64', panid='0xbeef',
                           dodag_root=True, storing_mode=mode, privileged=True,
                           volumes=[path + "/:/root", "/tmp/.X11-unix:/tmp/.X11-unix:rw"],
                           dimage=dimage, cpu_shares=20, netcfg=True,
                           environment={"DISPLAY": ":0"}, loglevel="info",
                           thriftport=50001,  IPBASE="172.17.0.0/24", **args)
    sensor1 = net.addSensor('sensor1', ip6='fe80::2/64', panid='0xbeef')
    sensor2 = net.addSensor('sensor2', ip6='fe80::3/64', panid='0xbeef')
    sensor3 = net.addSensor('sensor3', ip6='fe80::4/64', panid='0xbeef')
    sensor4 = net.addSensor('sensor4', ip6='fe80::5/64', panid='0xbeef')
    sensor5 = net.addSensor('sensor5', ip6='fe80::6/64', panid='0xbeef')
    sensor6 = net.addSensor('sensor6', ip6='fe80::7/64', panid='0xbeef')
    sensor7 = net.addSensor('sensor7', ip6='fe80::8/64', panid='0xbeef')
    sensor8 = net.addSensor('sensor8', ip6='fe80::9/64', panid='0xbeef')
    sensor9 = net.addSensor('sensor9', ip6='fe80::10/64', panid='0xbeef')

    h1 = net.addHost('h1',  ip6='fe80::3/64', ip='192.168.210.1')

    net.configureWifiNodes()

    #ap1.cmd("tcpdump -i ap1-pan0 -w teste.pcap &")
    info('*** Creating links\n')
    net.addLink(s1, h1)
    net.addLink(ap1, sensor1, cls=LoWPAN)
    net.addLink(ap1, sensor2, cls=LoWPAN)
    net.addLink(sensor2, sensor3, cls=LoWPAN)
    net.addLink(sensor3, sensor4, cls=LoWPAN)
    net.addLink(ap1, sensor5, cls=LoWPAN)
    net.addLink(sensor1, sensor6, cls=LoWPAN)
    net.addLink(sensor5, sensor7, cls=LoWPAN)
    net.addLink(sensor5, sensor8, cls=LoWPAN)
    net.addLink(sensor4, sensor9, cls=LoWPAN)
    net.addLink(ap1, h1)
    h1.cmd('ifconfig h1-eth1 192.168.0.1')

    info('*** Starting network\n')
    net.build()
    net.addNAT(name='nat0', linkTo='s1', ip='192.168.210.254').configDefault()
    ap1.start([])
    s1.start([])
    net.staticArp()

    if '-s' in sys.argv:
        makeTerm(h1, title='h1', cmd="bash -c 'python packet-processing-storing.py;'")
    else:
        makeTerm(h1, title='h1', cmd="bash -c 'python packet-processing-non-storing.py;'")
    net.configRPLD(net.sensors + net.apsensors)

    info('*** Running CLI\n')
    CLI(net)

    os.system('pkill -9 -f xterm')

    info('*** Stopping network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()