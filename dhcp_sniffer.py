#!/usr/bin/env python3

import socket
from struct import unpack
# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s.bind((HOST, 69))

# receive all packages
while True:
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    bytes, direccion=s.recvfrom(65565)
    
    ip_header = bytes[0:20]
     
    iph = unpack('!BBHHHBBH4s4s' , ip_header)
     
    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
     
    iph_length = ihl * 4
     
    ttl = iph[5]
    protocol = iph[6]
    s_addr = socket.inet_ntoa(iph[8]);
    d_addr = socket.inet_ntoa(iph[9]);
    
    # receive a package
    
    
    
    print("IP Origen:"+s_addr)
    print("IP_Destino:"+ d_addr)
    # disabled promiscuous mode
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)