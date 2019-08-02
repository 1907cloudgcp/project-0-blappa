#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Socket
#By Bertrick

import socket
from binascii import hexlify
import re, uuid 


# get IP address and port
def get_IPADDR():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("msn.com",80))

    return s.getsockname()[0]



# get mac address
def get_MACADDR(interface, p=0):
    
    # joins elements of getnode() after each 2 digits. 
    # using regex expression 
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

    return mac


def get_PORTS():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('0.0.0.0', 0))
    return sock.getsockname()[1]
