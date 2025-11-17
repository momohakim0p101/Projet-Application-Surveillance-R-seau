
from pysnmp.hlapi import *

def lire_uptime(ip, communaute="public"):
    try:
        resultat = getCmd(
            SnmpEngine(),
            CommunityData(communaute, mpModel=1),
            UdpTransportTarget((ip, 161), timeout=1, retries=1),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0'))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(resultat)

        if errorIndication:
            return None

        for nom, valeur in varBinds:
            return str(valeur)

    except Exception as e:
        print("Erreur SNMP :", e)
        return None
