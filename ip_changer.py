#!/usr/bin/env python3
#coding=utf-8

import wmi #Imprescindible, si no lo tienes ejecuta "pip3 install wmi"

from ConfigManager import ConfigManager


def get_lista_tarjetas():
    c = wmi.WMI()
    qry = "select Name from Win32_NetworkAdapter where NetEnabled=True and NetConnectionStatus=2"
    
    lst = [o.Name for o in c.query(qry)]    
def cambiar_gateway(tarjeta, gateway):
    codigo_exito=tarjeta.SetGateways(DefaultIPGateway=[gateway])
    if codigo_exito[0]==0:
        print("\n\tCambiada puerta de enlace a:"+gateway)
        
                
def cambiar_ip ( tarjeta, ip, mascara):
    codigo_exito=tarjeta.EnableStatic(IPAddress=[ip],SubnetMask=[mascara])
    if codigo_exito[0]==0:
        mensaje="\n\tNueva IP: {0}    Nueva máscara:{1}".format(ip, mascara)
        print(mensaje)
    else:
        mensaje="\n\tNO SE HA CAMBIADO A LA IP {0} CON MÁSCARA {1}".format(ip, mascara)
        
def cambiar_dns(tarjeta, dns1, dns2):
    codigo_exito=tarjeta.SetDNSServerSearchOrder(DNSServerSearchOrder=[dns1, dns2])
    if codigo_exito[0]==0:
        mensaje="\n\tNuevo DNS1: {0}    Nueva DNS2:{1}".format(dns1, dns2)
        print(mensaje)
    else:
        mensaje="\n\tNO SE HA CAMBIADO A LA IP {0} CON MÁSCARA {1}".format(ip, mascara)
        
def cambiar_direccion(ip, mascara, gateway, dns1, dns2, nombre_tarjeta="Realtek"):
    tarjetas=get_lista_tarjetas()
    for tarjeta in tarjetas:
        print ("Comprobando tarjeta:"+tarjeta.caption)
        if tarjeta.caption.find(nombre_tarjeta)!=-1:
            cambiar_ip(tarjeta, ip, mascara)
            cambiar_gateway(tarjeta, gateway)
            cambiar_dns(tarjeta, dns1, dns2)
            
            
def get_lista_tarjetas():
    tarjetas = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
def establecer_configuracion(nombre_fichero_ini):
    configuracion=ConfigManager(nombre_fichero_ini)
    ip          =   config.get_ip_address()
    netmask     =   config.get_mask()
    gw          =   config.get_gw()
    dns1        =   config.get_dns1()
    dns2        =   config.get_dns2()
    cambiar_direccion(ip, netmask, gw, dns1, dns2)
    
    
if __name__ == '__main__':
    cambiar_direccion("10.15.0.200", "255.0.0.0", "10.15.0.220", "10.15.0.220", "8.8.4.4")