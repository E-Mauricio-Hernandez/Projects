import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore, QtTest
from PyQt5.QtCore import QPropertyAnimation
import time
global modo 
modo="1"
class VentanaInicio(QMainWindow):
    
	def __init__(self):
		
		super(VentanaInicio, self).__init__()
		loadUi('principal.ui', self)
		self.texto.setText("HI")
		self.texto.setMaxLength (10)
		self.op1.setChecked(True)
		self.title = 'Universidad de los llanos'
		self.setWindowTitle(self.title)
		self.ON.clicked.connect(self.convertir)
		self.op1.toggled.connect(self.nrz_l)
		self.op1_2.toggled.connect(self.nrz_m)
		self.op1_3.toggled.connect(self.nrz_s)
		self.op1_4.toggled.connect(self.bipolarrz)
		self.op1_5.toggled.connect(self.rz_ami)
		self.op1_6.toggled.connect(self.unipolarrz)
		self.op1_7.toggled.connect(self.bi_o_m)
		self.op1_8.toggled.connect(self.bi_o_s)
		self.op1_9.toggled.connect(self.bi_o_l)
		self.op1_10.toggled.connect(self.dicodenrz)
		self.op1_11.toggled.connect(self.dicoderz)
		self.op1_12.toggled.connect(self.delaymod)

	def nrz_l(self):
		global modo
		modo="1"
	def nrz_m(self):
		global modo
		modo="2"
	def nrz_s(self):
		global modo
		modo="3"
	def unipolarrz(self):
		global modo
		modo="4"
	def bipolarrz(self):
		global modo
		modo="5"
	def rz_ami(self):
		global modo
		modo="6"
	def bi_o_l(self):
		global modo
		modo="7"
	def bi_o_m(self):
		global modo
		modo="8"
	def bi_o_s(self):
		global modo
		modo="9"
	def delaymod(self):
		global modo
		modo="10"
	def dicodenrz(self):
		global modo
		modo="11"
	def dicoderz(self):
		global modo
		modo="12"


	def convertir(self):
		global modo
		def string2bits(s=''):
			return [bin(ord(x))[2:].zfill(8) for x in s]
		s = self.texto.text()
		self.texto.setText("OK")
		b = string2bits(s)
		c=modo+","
		for x in b:
		    c=c+x
		print(c)
		prueba=c.split(",")
		f = open ('datos.txt','w')
		f.write(c)
		f.close()


app = QApplication(sys.argv)
main = VentanaInicio()
main.show()
sys.exit(app.exec_())



