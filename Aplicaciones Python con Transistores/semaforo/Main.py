import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore, QtTest
import LogoU_rc
from PyQt5.QtCore import QPropertyAnimation
import Motor_rc
import math
import time
global msv1
global msv1
global msa1
global msr1
global msv2
global msa2
global msr2
global msv3
global msa3
global msr3
global msv4
global msa4
global msr4
global indi
indi=0
msv1=0
msa1=0
msr1=0
msv2=0
msa2=0
msr2=0
msv3=0
msa3=0
msr3=0
msv4=0
msa4=0
msr4=0

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
        otra_ventana = Ventanaapagado(self)
        otra_ventana.show()

class Ventanaapagado(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanaapagado, self).__init__(parent)
        loadUi('Generador.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.finalboton.clicked.connect(self.close)
        self.manualboton.clicked.connect(self.AbrirVentanaManual)
        self.autoboton.clicked.connect(self.AbrirVentanaAuto)
        self.semiboton.clicked.connect(self.AbrirVentanaSemi)
        self.semiboton2.clicked.connect(self.AbrirVentanaSemi2)
        
    def AbrirVentanaAuto(self):
        self.hide()
        otra_ventana = VentanaAuto(self)
        otra_ventana.show()
    def AbrirVentanaSemi(self):
        self.hide()
        otra_ventana = VentanaSemi(self)
        otra_ventana.show()
    def AbrirVentanaSemi2(self):
        self.hide()
        otra_ventana = VentanaSemi2(self)
        otra_ventana.show()
    def AbrirVentanaManual(self):
        self.hide()
        otra_ventana = VentanaManual(self)
        otra_ventana.show()

class VentanaAuto(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaAuto, self).__init__(parent)
        loadUi('Generador2.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.CICLOS.setMinimum(1)
        self.TEMCICLOS.setMinimum(1)
        self.finalboton.clicked.connect(self.close)
        self.manualboton.clicked.connect(self.AbrirVentanaManual)
        self.apagadoboton.clicked.connect(self.AbrirVentanaapagado)
        self.semiboton.clicked.connect(self.AbrirVentanaSemi)
        self.finalboton.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.procesoauto)
        self.semiboton2.clicked.connect(self.AbrirVentanaSemi2)
        self.individual.stateChanged.connect(self.estado)
        
    def estado(self):
        global indi
        if (indi==0):
            indi=1
        else:
            indi=0

    def procesoauto(self):
        global indi
        ciclosnum=self.CICLOS.value()
        tiempo=self.TEMCICLOS.value()
        contador=0
        if (indi==0):
            while contador<ciclosnum:
                print("semaforo 1 y 3 verde; 2 y 4 rojo")
                time.sleep(tiempo)
                print("semaforos en amarillo")
                time.sleep(tiempo)
                print("semaforo 2 y 4 verde; 1 y 3 rojo")
                time.sleep(tiempo)
                print("semaforos en amarillo")
                time.sleep(tiempo)
                contador=contador+1
        else:
            while contador<ciclosnum:
                print("semaforo 1 verde; 3,2 y 4 rojo")
                time.sleep(tiempo)
                print("semaforos en amarillo")
                time.sleep(tiempo)
                print("semaforo 2 verde; 1,3 y 4 rojo")
                time.sleep(tiempo)
                print("semaforos en amarillo")
                time.sleep(tiempo)
                print("semaforo 3 verde; 1,2 y 4 rojo")
                time.sleep(tiempo)
                print("semaforos en amarillo")
                time.sleep(tiempo)
                print("semaforo 4 verde; 1,2 y 3 rojo")
                time.sleep(tiempo)
                print("semaforos en amarillo")
                time.sleep(tiempo)
                contador=contador+1
        self.AbrirVentanaFindelproceso()

                


    def AbrirVentanaFindelproceso(self):
        self.hide()
        otra_ventana = VentanaFindelproceso(self)
        otra_ventana.show()


    def AbrirVentanaapagado(self):
        self.hide()
        otra_ventana = Ventanaapagado(self)
        otra_ventana.show()
    def AbrirVentanaSemi(self):
        self.hide()
        otra_ventana = VentanaSemi(self)
        otra_ventana.show()
    def AbrirVentanaManual(self):
        self.hide()
        otra_ventana = VentanaManual(self)
        otra_ventana.show()
    def AbrirVentanaSemi2(self):
        self.hide()
        otra_ventana = VentanaSemi2(self)
        otra_ventana.show()
class VentanaFindelproceso(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaFindelproceso, self).__init__(parent)
        loadUi('Generador3.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.volverboton.clicked.connect(self.AbrirVentanaAuto)
    def AbrirVentanaAuto(self):
        self.hide()
        otra_ventana = VentanaAuto(self)
        otra_ventana.show()

class VentanaSemi(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaSemi, self).__init__(parent)
        loadUi('Generador.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV1.clicked.connect(self.cambio1)
        self.SV3.clicked.connect(self.cambio1)

        self.SR1.clicked.connect(self.cambio3)
        self.SR3.clicked.connect(self.cambio3)


        self.SA2.clicked.connect(self.cambio2)
        self.SA3.clicked.connect(self.cambio2)
        self.SA4.clicked.connect(self.cambio2)
        self.SA1.clicked.connect(self.cambio2)

        self.SR2.clicked.connect(self.cambio1)
        self.SR4.clicked.connect(self.cambio1)
        self.SV2.clicked.connect(self.cambio3)
        self.SV4.clicked.connect(self.cambio3)
        self.finalboton.clicked.connect(self.close)
        self.manualboton.clicked.connect(self.AbrirVentanaManual)
        self.autoboton.clicked.connect(self.AbrirVentanaAuto)
        self.finalboton.clicked.connect(self.close)
        self.apagadoboton.clicked.connect(self.AbrirVentanaapagado)
        self.semiboton2.clicked.connect(self.AbrirVentanaSemi2)
 

    def cambio1(self):
        self.SV1.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(255, 0, 0);")
    def cambio2(self):
        self.SA1.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.SA2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.SA3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.SA4.setStyleSheet("background-color: rgb(255, 255, 0);")

        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
    def cambio3(self):
        self.SV2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV4.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(255, 0, 0);")

    def AbrirVentanaSemi2(self):
        self.hide()
        otra_ventana = VentanaSemi2(self)
        otra_ventana.show()
        
    def AbrirVentanaAuto(self):
        self.hide()
        otra_ventana = VentanaAuto(self)
        otra_ventana.show()
    def AbrirVentanaManual(self):
        self.hide()
        otra_ventana = VentanaManual(self)
        otra_ventana.show()
    def AbrirVentanaapagado(self):
        self.hide()
        otra_ventana = Ventanaapagado(self)
        otra_ventana.show()

class VentanaSemi2(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaSemi2, self).__init__(parent)
        loadUi('Generador.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
        
        self.SV1.clicked.connect(self.cambio1)
        self.SV3.clicked.connect(self.cambio4)
        self.SV2.clicked.connect(self.cambio3)
        self.SV4.clicked.connect(self.cambio5)

        self.SR1.clicked.connect(self.cambio6)
        self.SR3.clicked.connect(self.cambio6)
        self.SR2.clicked.connect(self.cambio6)
        self.SR4.clicked.connect(self.cambio6)


        self.SA2.clicked.connect(self.cambio2)
        self.SA3.clicked.connect(self.cambio2)
        self.SA4.clicked.connect(self.cambio2)
        self.SA1.clicked.connect(self.cambio2)

        
        
        self.finalboton.clicked.connect(self.close)
        self.manualboton.clicked.connect(self.AbrirVentanaManual)
        self.autoboton.clicked.connect(self.AbrirVentanaAuto)
        self.finalboton.clicked.connect(self.close)
        self.apagadoboton.clicked.connect(self.AbrirVentanaapagado)
        self.semiboton.clicked.connect(self.AbrirVentanaSemi)
        

    def cambio1(self):
        self.SV1.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(255, 0, 0);")
    def cambio2(self):
        self.SA1.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.SA2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.SA3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.SA4.setStyleSheet("background-color: rgb(255, 255, 0);")

        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
    def cambio3(self):
        self.SV2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(255, 0, 0);")
    def cambio4(self):
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
    def cambio5(self):
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV4.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(255, 0, 0);")
    def cambio6(self):
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(255, 0, 0);")

    def AbrirVentanaAuto(self):
        self.hide()
        otra_ventana = VentanaAuto(self)
        otra_ventana.show()
    def AbrirVentanaManual(self):
        self.hide()
        otra_ventana = VentanaManual(self)
        otra_ventana.show()
    def AbrirVentanaapagado(self):
        self.hide()
        otra_ventana = Ventanaapagado(self)
        otra_ventana.show()
    def AbrirVentanaSemi(self):
        self.hide()
        otra_ventana = VentanaSemi(self)
        otra_ventana.show()
class VentanaManual(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaManual, self).__init__(parent)
        loadUi('Generador.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV1.clicked.connect(self.ms1)
        self.SV3.clicked.connect(self.ms7)
        self.SR1.clicked.connect(self.ms3)
        self.SR3.clicked.connect(self.ms9)
        self.SA2.clicked.connect(self.ms5)
        self.SA3.clicked.connect(self.ms8)
        self.SA4.clicked.connect(self.ms11)
        self.SA1.clicked.connect(self.ms2)
        self.SV2.clicked.connect(self.ms4)
        self.SV4.clicked.connect(self.ms10)
        self.SR2.clicked.connect(self.ms6)
        self.SR4.clicked.connect(self.ms12)
        self.finalboton.clicked.connect(self.close)
        self.autoboton.clicked.connect(self.AbrirVentanaAuto)
        self.semiboton.clicked.connect(self.AbrirVentanaSemi)
        self.apagadoboton.clicked.connect(self.AbrirVentanaapagado)
        self.semiboton2.clicked.connect(self.AbrirVentanaSemi2)
        
        
    def AbrirVentanaSemi2(self):
        self.hide()
        otra_ventana = VentanaSemi2(self)
        otra_ventana.show()
    def ms1(self):
        global msv1
        msv1=msv1+1
        if msv1%2==0:
            self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SV1.setStyleSheet("background-color: rgb(0, 255, 0);")
    def ms2(self):
        global msa1
        msa1=msa1+1
        if msa1%2==0:
            self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SA1.setStyleSheet("background-color: rgb(255, 255, 0);")
    def ms3(self):
        global msr1
        msr1=msr1+1
        if msr1%2==0:
            self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SR1.setStyleSheet("background-color: rgb(255, 0, 0);")
    def ms4(self):
        global msv2
        msv2=msv2+1
        if msv2%2==0:
            self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SV2.setStyleSheet("background-color: rgb(0, 255, 0);")
    def ms5(self):
        global msa2
        msa2=msa2+1
        if msa2%2==0:
            self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SA2.setStyleSheet("background-color: rgb(255, 255, 0);")
    def ms6(self):
        global msr2
        msr2=msr2+1
        if msr2%2==0:
            self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SR2.setStyleSheet("background-color: rgb(255, 0, 0);")
    def ms7(self):
        global msv3
        msv3=msv3+1
        if msv3%2==0:
            self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SV3.setStyleSheet("background-color: rgb(0, 255, 0);")
    def ms8(self):
        global msa3
        msa3=msa3+1
        if msa3%2==0:
            self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SA3.setStyleSheet("background-color: rgb(255, 255, 0);")
    def ms9(self):
        global msr3
        msr3=msr3+1
        if msr3%2==0:
            self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SR3.setStyleSheet("background-color: rgb(255, 0, 0);")
    def ms10(self):
        global msv4
        msv4=msv4+1
        if msv4%2==0:
            self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SV4.setStyleSheet("background-color: rgb(0, 255, 0);")
    def ms11(self):
        global msa4
        msa4=msa4+1
        if msa4%2==0:
            self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SA4.setStyleSheet("background-color: rgb(255, 255, 0);")
    def ms12(self):
        global msr4
        msr4=msr4+1
        if msr4%2==0:
            self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
        else:
            self.SR4.setStyleSheet("background-color: rgb(255, 0, 0);")

    def AbrirVentanaAuto(self):
        self.hide()
        otra_ventana = VentanaAuto(self)
        otra_ventana.show()
    def AbrirVentanaSemi(self):
        self.hide()
        otra_ventana = VentanaSemi(self)
        otra_ventana.show()
    def AbrirVentanaapagado(self):
        self.hide()
        otra_ventana = Ventanaapagado(self)
        otra_ventana.show()



app = QApplication(sys.argv)
main = VentanaInicio()
main.show()
sys.exit(app.exec_())
