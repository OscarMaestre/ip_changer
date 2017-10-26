#!/usr/bin/env python3
#coding=utf-8

import wmi #Imprescindible, si no lo tienes ejecuta "pip3 install wmi"


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
    tarjetas = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    for tarjeta in tarjetas:
        print ("Comprobando tarjeta:"+tarjeta.caption)
        if tarjeta.caption.find(nombre_tarjeta)!=-1:
            cambiar_ip(tarjeta, ip, mascara)
            cambiar_gateway(tarjeta, gateway)
            cambiar_dns(tarjeta, dns1, dns2)
            
    
    
if __name__ == '__main__':
    cambiar_direccion("10.15.0.200", "255.0.0.0", "10.15.0.220", "10.15.0.220", "8.8.4.4")