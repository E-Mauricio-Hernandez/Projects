import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore, QtTest

from PyQt5.QtCore import QPropertyAnimation
import math
import time

class VentanaInicio(QMainWindow):
    def __init__(self):
        super(VentanaInicio, self).__init__()
        loadUi('principaltransferencia.ui', self)
        self.title = 'servicio de pago'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icon_1.png"))
        self.tarjeta.clicked.connect(self.abrirVentanatarjeta)
        self.botonpago.clicked.connect(self.abrirVentanapago)
        

    def abrirVentanatarjeta(self):
        reader = SimpleMFRC522()
        id, text = reader.read()
        self.varsaldo.setText(text)
    def abrirVentanapago(self):
        reader = SimpleMFRC522()
        id, text = reader.read()
        text2=self.linea.text()
        text=str(int(text)+int(text2))
        reader.write(text)
        linea.setText("TRANSFERENCIA REALIZADA")

app = QApplication(sys.argv)
main = VentanaInicio()
main.show()
sys.exit(app.exec_())
