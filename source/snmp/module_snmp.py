
from .collecteur_snmp import lire_uptime

class ModuleSNMP:
    def __init__(self, ip):
        self.ip = ip

    def obtenir_uptime(self):
        return lire_uptime(self.ip)
