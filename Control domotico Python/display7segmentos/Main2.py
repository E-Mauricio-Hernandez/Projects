import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.uic import loadUi
import logo1
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(12,gpio.OUT)
gpio.setup(11,gpio.OUT)
gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.OUT)
gpio.setup(19,gpio.OUT)
gpio.setup(21,gpio.OUT)
gpio.setup(23,gpio.OUT)

gpio.output(12,True)
gpio.output(11,True)
gpio.output(13,True)
gpio.output(15,True)
gpio.output(19,True)
gpio.output(21,True)
gpio.output(23,True)


class VentanaPrincipal(QMainWindow):
	global llamar
	def __init__(self):
		super(VentanaPrincipal, self).__init__()
		loadUi('interfaz_display.ui', self)

		self.num1.clicked.connect(self.numero1)
		self.num2.clicked.connect(self.numero2)
		self.num3.clicked.connect(self.numero3)
		self.num4.clicked.connect(self.numero4)
		self.num5.clicked.connect(self.numero5)
		self.num6.clicked.connect(self.numero6)
		self.num7.clicked.connect(self.numero7)
		self.num8.clicked.connect(self.numero8)
		self.num9.clicked.connect(self.numero9) 
		self.num0.clicked.connect(self.numero0)

	def llamar(self):
		self.numero_2.setProperty("value", 3)
		

	def numero1(self): 
			global numa 
			numa = 1 
			self.numero.setProperty("value", numa)
			gpio.output(12,True)	#a
			gpio.output(11,False)	#b
			gpio.output(13,False)	#c
			gpio.output(15,True)	#d
			gpio.output(19,True)	#e
			gpio.output(21,True)	#f
			gpio.output(23,True)	#g
	def numero2(self):
			global numa  
			numa = 2
			self.numero.setProperty("value", numa)
			gpio.output(12,False)
			gpio.output(11,False)
			gpio.output(13,True)
			gpio.output(15,False)
			gpio.output(19,False)
			gpio.output(21,True)
			gpio.output(23,False)
	def numero3(self):
			global numa  
			numa = 3
			self.numero.setProperty("value", numa)
			gpio.output(12,False)
			gpio.output(11,False)
			gpio.output(13,False)
			gpio.output(15,False)
			gpio.output(19,True)
			gpio.output(21,True)
			gpio.output(23,False)

	def numero4(self): 
			global numa 
			numa = 4
			self.numero.setProperty("value", numa)
			gpio.output(12,True)
			gpio.output(11,False)
			gpio.output(13,False)
			gpio.output(15,True)
			gpio.output(19,True)
			gpio.output(21,False)
			gpio.output(23,False)

	def numero5(self): 
			global numa 
			numa = 5
			self.numero.setProperty("value", numa)
			gpio.output(12,False)
			gpio.output(11,True)
			gpio.output(13,False)
			gpio.output(15,False)
			gpio.output(19,True)
			gpio.output(21,False)
			gpio.output(23,False)
	def numero6(self): 
			global numa 
			numa = 6
			self.numero.setProperty("value", numa)
			gpio.output(12,False)
			gpio.output(11,True)
			gpio.output(13,False)
			gpio.output(15,False)
			gpio.output(19,False)
			gpio.output(21,False)
			gpio.output(23,False)
	def numero7(self): 
			global numa 
			numa = 7
			self.numero.setProperty("value", numa)
			gpio.output(12,False)
			gpio.output(11,False)
			gpio.output(13,False)
			gpio.output(15,True)
			gpio.output(19,True)
			gpio.output(21,True)
			gpio.output(23,True)
	def numero8(self): 
			global numa 
			numa = 8
			self.numero.setProperty("value", numa)
			gpio.output(12,False)
			gpio.output(11,False)
			gpio.output(13,False)
			gpio.output(15,False)
			gpio.output(19,False)
			gpio.output(21,False)
			gpio.output(23,False)
	def numero9(self): 
			global numa 
			numa = 9
			self.numero.setProperty("value", numa)
			gpio.output(12,False)
			gpio.output(11,False)
			gpio.output(13,False)
			gpio.output(15,False)
			gpio.output(19,True)
			gpio.output(21,False)
			gpio.output(23,False)
	def numero0(self): 
			global numa 
			numa = 0
			self.numero.setProperty("value", numa)
			gpio.output(12,False)
			gpio.output(11,False)
			gpio.output(13,False)
			gpio.output(15,False)
			gpio.output(19,False)
			gpio.output(21,False)
			gpio.output(23,True)

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())