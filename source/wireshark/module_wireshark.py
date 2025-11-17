
from .capture_paquets import capturer

class ModuleWireshark:
    def __init__(self, interface="eth0"):
        self.interface = interface

    def analyser(self):
        return capturer(self.interface, 3)
