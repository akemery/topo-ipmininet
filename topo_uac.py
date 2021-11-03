
from mininet.log import lg

import ipmininet
from ipmininet.cli import IPCLI
from ipmininet.ipnet import IPNet

from ipmininet.iptopo import IPTopo

HOSTS_PER_ROUTER = 2


class UACNet(IPTopo):

    def build(self, *args, **kwargs):
        
        for i in range(1, 15, 1):
            self.addRouters('r%s'% i, use_v4=True, use_v6=True)
       
        for i in range(1, 6, 1):
            self.addLink('r%s'%i, 'r%s'%(i+1))

        for i in range(2, 10, 2):
            self.addLink('r%s'%i, 'r%s'%(i+2))
        
        for i in range(7, 9, 1):
            self.addLink('r%s'%i, 'r%s'%(i+1))

        super().build(*args, **kwargs)

# Start network
net = IPNet(topo=UACNet(), use_v4=True, allocate_IPs=True)
net.start()
IPCLI(net)
net.stop()


