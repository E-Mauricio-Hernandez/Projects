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
gpio.setup(32, gpio.OUT)
gpio.setup(33, gpio.OUT)
gpio.setup(36, gpio.OUT)
gpio.output(36, True)
time.sleep(0.5)
gpio.output(36, False)
time.sleep(0.5)
gpio.output(7, False)
gpio.output(11, False)
gpio.output(12, False)
gpio.output(13, False)
gpio.output(15, False)
gpio.output(16, False)
gpio.output(18, False)
gpio.output(22, False)
gpio.output(29, False)
gpio.output(31, False)
gpio.output(32, False)
gpio.output(33, False)

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
        gpio.output(36, True)
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False)
        gpio.output(11, False)
        gpio.output(12, False)
        gpio.output(13, False)
        gpio.output(15, False)
        gpio.output(16, False)
        gpio.output(18, False)
        gpio.output(22, False)
        gpio.output(29, False)
        gpio.output(31, False)
        gpio.output(32, False)
        gpio.output(33, False)

        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.finalboton.clicked.connect(self.close)
        self.boton_texto.clicked.connect(self.AbrirVentanaAuto)
        self.boton_a.clicked.connect(self.AbrirVentanaa)
        self.boton_b.clicked.connect(self.AbrirVentanab)
        self.boton_c.clicked.connect(self.AbrirVentanac)
        self.boton_d.clicked.connect(self.AbrirVentanad)
        self.boton_e.clicked.connect(self.AbrirVentanae)
        self.boton_f.clicked.connect(self.AbrirVentanaf)
        self.boton_g.clicked.connect(self.AbrirVentanag)
        self.boton_h.clicked.connect(self.AbrirVentanah)
        self.boton_i.clicked.connect(self.AbrirVentanai)
        self.boton_j.clicked.connect(self.AbrirVentanaj)
        self.boton_k.clicked.connect(self.AbrirVentanak)
        self.boton_l.clicked.connect(self.AbrirVentanal)
        self.boton_m.clicked.connect(self.AbrirVentanam)
        self.boton_n.clicked.connect(self.AbrirVentanan)
        self.boton_o.clicked.connect(self.AbrirVentanao)
        self.boton_p.clicked.connect(self.AbrirVentanap)
        self.boton_q.clicked.connect(self.AbrirVentanaq)
        self.boton_r.clicked.connect(self.AbrirVentanar)
        self.boton_s.clicked.connect(self.AbrirVentanas)
        self.boton_t.clicked.connect(self.AbrirVentanat)
        self.boton_u.clicked.connect(self.AbrirVentanau)
        self.boton_v.clicked.connect(self.AbrirVentanav)
        self.boton_w.clicked.connect(self.AbrirVentanaw)
        self.boton_x.clicked.connect(self.AbrirVentanax)
        self.boton_y.clicked.connect(self.AbrirVentanay)
        self.boton_z.clicked.connect(self.AbrirVentanaz)
        self.boton_off.clicked.connect(self.AbrirVentanaoff)
        self.boton_punto.clicked.connect(self.AbrirVentanapunto)
        self.AbrirVentanaoff()

        
    def AbrirVentanaAuto(self):
        self.hide()
        otra_ventana = VentanaFindelproceso(self)
        otra_ventana.show()
    def AbrirVentanaa(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanab(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanac(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanad(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanae(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaf(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
    def AbrirVentanag(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanah(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanai(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaj(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanak(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanal(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanam(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanan(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanao(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3nap(self):
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanap(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)  
    def AbrirVentanaq(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanar(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, True)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanas(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanat(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanau(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanav(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, False)#d1
        gpio.output(32, True)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaw(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanax(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, True)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanay(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, True)#b2
        gpio.output(16, False)#b3
        gpio.output(18, False)#c1
        gpio.output(22, True)#c2
        gpio.output(29, False)#c3
        gpio.output(31, False)#d1
        gpio.output(32, True)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaz(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, False)#c1
        gpio.output(22, True)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanapunto(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaoff(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
    def AbrirVentanaerror(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)


class VentanaFindelproceso(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaFindelproceso, self).__init__(parent)
        loadUi('Generador3.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.volverboton.clicked.connect(self.AbrirVentanaAuto)
        self.pushButton.clicked.connect(self.proceso)
    def proceso(self):
        linea=self.lineEdit.text()
        cantidad=len(linea)
        for x in range (0,cantidad):
            letra=linea[x]
            if letra=='a':
                self.AbrirVentanaa()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='b':
                self.AbrirVentanab()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='c':
                self.AbrirVentanac()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='d':
                self.AbrirVentanad()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='e':
                self.AbrirVentanae()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='f':
                self.AbrirVentanaf()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='g':
                self.AbrirVentanag()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='h':
                self.AbrirVentanah()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='i':
                self.AbrirVentanai()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='j':
                self.AbrirVentanaj()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='k':
                self.AbrirVentanak()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='l':
                self.AbrirVentanal()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='m':
                self.AbrirVentanam()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='n':
                self.AbrirVentanan()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='o':
                self.AbrirVentanao()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='p':
                self.AbrirVentanap()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='q':
                self.AbrirVentanaq()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='r':
                self.AbrirVentanar()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='s':
                self.AbrirVentanas()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='t':
                self.AbrirVentanat()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='u':
                self.AbrirVentanau()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='v':
                self.AbrirVentanav()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='x':
                self.AbrirVentanax()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='y':
                self.AbrirVentanay()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='z':
                self.AbrirVentanaz()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra=='.':
                self.AbrirVentanapunto()
                time.sleep(2)
                self.AbrirVentanaerror()
            elif letra==' ':
                self.AbrirVentanaerror()
            else:
                self.AbrirVentanaoff()
            time.sleep(1)
        self.lineEdit.clear()
    def AbrirVentanaa(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanab(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanac(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanad(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanae(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaf(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
    def AbrirVentanag(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanah(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanai(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaj(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanak(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanal(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanam(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanan(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanao(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3nap(self):
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanap(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)  
    def AbrirVentanaq(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanar(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, True)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanas(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanat(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, True)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanau(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanav(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, False)#c2
        gpio.output(29, True)#c3
        gpio.output(31, False)#d1
        gpio.output(32, True)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaw(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanax(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, True)#b3
        gpio.output(18, False)#c1
        gpio.output(22, True)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanay(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, False)#a2
        gpio.output(12, True)#a3
        gpio.output(13, False)#b1
        gpio.output(15, True)#b2
        gpio.output(16, False)#b3
        gpio.output(18, False)#c1
        gpio.output(22, True)#c2
        gpio.output(29, False)#c3
        gpio.output(31, False)#d1
        gpio.output(32, True)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaz(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, True) #a1
        gpio.output(11, True)#a2
        gpio.output(12, True)#a3
        gpio.output(13, True)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, False)#c1
        gpio.output(22, True)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, True)#d2
        gpio.output(33, True)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanapunto(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, True)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaerror(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, False)#c1
        gpio.output(22, False)#c2
        gpio.output(29, False)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
    def AbrirVentanaoff(self):
        gpio.output(36, True)#desenclave
        time.sleep(0.5)
        gpio.output(36, False)
        time.sleep(0.5)
        gpio.output(7, False) #a1
        gpio.output(11, False)#a2
        gpio.output(12, False)#a3
        gpio.output(13, False)#b1
        gpio.output(15, False)#b2
        gpio.output(16, False)#b3
        gpio.output(18, True)#c1
        gpio.output(22, True)#c2
        gpio.output(29, True)#c3
        gpio.output(31, False)#d1
        gpio.output(32, False)#d2
        gpio.output(33, False)#d3
        time.sleep(0.5)
		gpio.output(7, False)
		gpio.output(11, False)
		gpio.output(12, False)
		gpio.output(13, False)
		gpio.output(15, False)
		gpio.output(16, False)
		gpio.output(18, False)
		gpio.output(22, False)
		gpio.output(29, False)
		gpio.output(31, False)
		gpio.output(32, False)
		gpio.output(33, False)
    def AbrirVentanaAuto(self):
        self.hide()
        otra_ventana = Ventanaapagado(self)
        otra_ventana.show()

app = QApplication(sys.argv)
main = VentanaInicio()
main.show()
sys.exit(app.exec_())
