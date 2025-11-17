
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from nagios.module_nagios import ModuleNagios

class OngletNagios(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.label = QLabel("État des hôtes Nagios")
        bouton = QPushButton("Rafraîchir")
        bouton.clicked.connect(self.lire_nagios)

        layout.addWidget(self.label)
        layout.addWidget(bouton)

        self.setLayout(layout)

    def lire_nagios(self):
        module = ModuleNagios(
            "http://192168.1.10",
            "nagiosadmin",
            "password"
        )
        info = module.obtenir_etat()
        self.label.setText(str(info))
