import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore, QtTest
from PyQt5.QtCore import QPropertyAnimation
import logo1
import logo2
import logo3
import logo4
import imjj
import paho.mqtt.client as mqtt
import time
import webbrowser

class VentanaInicio(QMainWindow):
    
	def __init__(self):
		
		super(VentanaInicio, self).__init__()
		loadUi('principal.ui', self)
		self.title = 'Universidad de los llanos'
		self.setWindowTitle(self.title)
		self.OFF.clicked.connect(self.procesooff)
		self.ON.clicked.connect(self.procesoon)
		self.low.clicked.connect(self.encenderbajo)
		self.medio.clicked.connect(self.encendermedio)
		self.high.clicked.connect(self.encenderalto)
		self.web.clicked.connect(self.openweb)


	def procesoon(self):
		broker_address="192.168.137.207"
		client = mqtt.Client("P51")
		client.connect(broker_address)
		client.publish("electronica/temperatura","d")
		print("on")
	def openweb(self):
 		webbrowser.open_new_tab("http://thingspeak.com/channels/850869")
    
	def procesooff(self):
		broker_address="192.168.43.44"
		client = mqtt.Client("P52")
		client.connect(broker_address)
		client.publish("electronica/temperatura","e")


    
	def encenderbajo(self):
		broker_address="192.168.43.44"
		client = mqtt.Client("P53")
		client.connect(broker_address)
		client.publish("electronica/temperatura","a")
	def encendermedio(self):
		broker_address="192.168.43.44"
		client = mqtt.Client("P67")
		client.connect(broker_address)
		client.publish("electronica/temperatura","b")
	def encenderalto(self):
		broker_address="192.168.43.44"
		client = mqtt.Client("P68")
		client.connect(broker_address)

		client.publish("electronica/temperatura","c")

#print("Publishing message to topic","house/bulbs/bulb1")
#client.publish("house/bulbs/bulb1","OFF")
app = QApplication(sys.argv)
main = VentanaInicio()
main.show()
sys.exit(app.exec_())

time.sleep(10) # wait
client.loop_stop() #stop the loop


