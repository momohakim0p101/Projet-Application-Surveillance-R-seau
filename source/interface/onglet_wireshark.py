
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from wireshark.module_wireshark import ModuleWireshark

class OngletWireshark(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.label = QLabel("Capture Wireshark")
        bouton = QPushButton("Démarrer Capture")
        bouton.clicked.connect(self.capturer)

        layout.addWidget(self.label)
        layout.addWidget(bouton)

        self.setLayout(layout)

    def capturer(self):
        module = ModuleWireshark("wlan0")
        capture = module.analyser()
        if len(capture) > 0:
            self.label.setText(str(capture[0]))
        else:
            self.label.setText("Aucun paquet capturé")
