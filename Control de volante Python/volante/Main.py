import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore, QtTest
import LogoU_rc
from PyQt5.QtCore import QPropertyAnimation
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(29, gpio.OUT)
gpio.setup(31, gpio.OUT)
gpio.output(7, False)
gpio.output(11, False)
gpio.output(12, False)
gpio.output(13, False)
gpio.output(15, False)
gpio.output(16, False)
gpio.output(18, False)
gpio.output(22, False)
gpio.output(29, False)


class VentanaInicio(QMainWindow):
    def __init__(self):
        super(VentanaInicio, self).__init__()
        loadUi('Inicio.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icon_1.png"))
        self.pushButton_C.clicked.connect(self.abrirVentanaapagado)
        self.pushButton_S.clicked.connect(self.close)

    def abrirVentanaapagado(self):
        self.hide()
        otra_ventana = Ventanaprincipal(self)
        otra_ventana.show()

class Ventanaprincipal(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanaprincipal, self).__init__(parent)
        loadUi('principal.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.angulo.setMinimum(-360)
        self.angulo.setMaximum(360)
        self.masdiez.clicked.connect(self.mas)
        self.menosdiez.clicked.connect(self.menos)
        self.vamos.clicked.connect(self.proceso)
        
    def mas(self):
        aux=self.angulo.value()
        aux=aux+10
        if aux>360:
            aux=360
        self.angulo.setValue(aux)
    def menos(self):
        aux=self.angulo.value()
        aux=aux-10
        if aux<-360:
            aux=-360
        self.angulo.setValue(aux)
    def proceso(self):
        aux=0
        aux2=""
        aux3=0
        aux=self.angulo.value()
        aux=aux+360
        aux=int((aux*1024)/720)
        aux2=str(bin(aux)[2:])
        aux3=10-len(aux2)
        final=""
        for i in range (0, aux3):
            final=final+"0"
        final=final+aux2
        if final[0]=="0":
            gpio.output(7, False)
        else:
             gpio.output(7, True)
        if final[1]=="0":
            gpio.output(11, False)
        else:
             gpio.output(11, True)
        if final[2]=="0":
            gpio.output(12, False)
        else:
             gpio.output(12, True)
        if final[3]=="0":
            gpio.output(13, False)
        else:
             gpio.output(13, True)
        if final[4]=="0":
            gpio.output(15, False)
        else:
             gpio.output(15, True)
        if final[5]=="0":
            gpio.output(16, False)
        else:
             gpio.output(16, True)
        if final[6]=="0":
            gpio.output(18, False)
        else:
             gpio.output(18, True)
        if final[7]=="0":
            gpio.output(22, False)
        else:
             gpio.output(22, True)
        if final[8]=="0":
            gpio.output(29, False)
        else:
             gpio.output(29, True)
        if final[9]=="0":
            gpio.output(31, False)
        else:
             gpio.output(31, True)
        
        



app = QApplication(sys.argv)
main = VentanaInicio()
main.show()
sys.exit(app.exec_())
