
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from snmp.module_snmp import ModuleSNMP

class OngletSNMP(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.label = QLabel("Cliquez pour lire l'uptime")
        bouton = QPushButton("Lire Uptime SNMP")
        bouton.clicked.connect(self.lire_uptime)

        layout.addWidget(self.label)
        layout.addWidget(bouton)

        self.setLayout(layout)

    def lire_uptime(self):
        module = ModuleSNMP("192.168.1.1")
        uptime = module.obtenir_uptime()
        self.label.setText(f"Uptime : {uptime}")
