#!/usr/bin/env python3

from configparser import ConfigParser

class ConfigManager(object):
    def __init__(self, fichero):
        self.parser=ConfigParser()
        self.parser.read(fichero)
    
    def get_ip_address(self):
        ip=self.parser["IP"]["ip_address"]
        return ip
    
    def get_mask(self):
        mask=self.parser["IP"]["netmask"]
        return mask
    
    def get_gw(self):
        gateway=self.parser["IP"]["default_gateway"]
        return gateway
    
    def get_dns1(self):
        dns1=self.parser["DNS"]["dns1"]
        return dns1
    
    def get_dns2(self):
        dns1=self.parser["DNS"]["dns2"]
        return dns1
    
    
if __name__ == '__main__':
    config=ConfigManager("config1.ini")
    print (config.get_ip_address())
    print (config.get_mask())
    print (config.get_gw())
    print (config.get_dns1())
    print (config.get_dns2())