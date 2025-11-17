
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
import sys

from .onglet_snmp import OngletSNMP
from .onglet_nagios import OngletNagios
from .onglet_wireshark import OngletWireshark

class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plateforme de Supervision Réseau")
        self.setGeometry(100, 100, 900, 600)

        onglets = QTabWidget()
        onglets.addTab(OngletSNMP(), "SNMP")
        onglets.addTab(OngletNagios(), "Nagios")
        onglets.addTab(OngletWireshark(), "Wireshark")

        self.setCentralWidget(onglets)

def lancer_application():
    app = QApplication(sys.argv)
    fenetre = FenetrePrincipale()
    fenetre.show()
    sys.exit(app.exec_())
