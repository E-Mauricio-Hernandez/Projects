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
global LAB1
global LAB2
global LAB3
global DEP
global on_message
import paho.mqtt.client as mqtt
import time
LAB1=0
LAB2=0
LAB3=0
DEP=0
global client
client = mqtt.Client("P10")
class VentanaInicio(QMainWindow):
    
    def __init__(self):
        super(VentanaInicio, self).__init__()
        loadUi('principal.ui', self)
        broker_address="192.168.43.195"
        client.connect(broker_address)
        client.publish("electronica/labs/lab1","0")
        client.publish("electronica/labs/lab2","0")
        client.publish("electronica/labs/lab3","0")
        client.publish("electronica/deposito","0")
        self.dato.setText("---")
        self.AMARILLO.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.VERDE_CLARO.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.ROJO.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.VERDE.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.OFFALL.clicked.connect(self.apagartodo)
        self.ONALL.clicked.connect(self.encendertodo)
        self.AMARILLO.clicked.connect(self.AMARILLOVEN)
        self.VERDE_CLARO.clicked.connect(self.VERDECLAROVEN)
        self.ROJO.clicked.connect(self.ROJOVEN)
        self.VERDE.clicked.connect(self.VERDEVEN)
        self.tem1.clicked.connect(self.temperatura1)
        self.tem2.clicked.connect(self.temperatura2)
        self.tem3.clicked.connect(self.temperatura3)
        self.tem4.clicked.connect(self.temperatura4)
        client.subscribe("electronica/labs/lab1")

    
    def temperatura1(self):
        client.publish("electronica/labs/lab1","t")
        time.sleep(2)
        f = open ('datos.txt','r')
        mensaje = f.read()
        self.dato.setText(mensaje)
        self.datolab.setText("LAB1:")

        
    def temperatura2(self):
        client.publish("electronica/labs/lab2","t")
        time.sleep(2)
        f = open ('datos.txt','r')
        mensaje = f.read()
        self.dato.setText(mensaje)
        self.datolab.setText("LAB2:")

    def temperatura3(self):
        client.publish("electronica/labs/lab3","t")
        time.sleep(2)
        f = open ('datos.txt','r')
        mensaje = f.read()
        self.dato.setText(mensaje)
        self.datolab.setText("LAB3:")

    def temperatura4(self):
        client.publish("electronica/deposito","t")
        time.sleep(2)
        f = open ('datos.txt','r')
        mensaje = f.read()
        self.dato.setText(mensaje)
        self.datolab.setText("DEP:")


    def apagartodo(self):
        global LAB1
        global LAB2
        global LAB3
        global DEP
        LAB1=0
        LAB2=0
        LAB3=0
        DEP=0
        self.AMARILLO.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.VERDE_CLARO.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.ROJO.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.VERDE.setStyleSheet("background-color: rgb(130, 130, 130);")
        broker_address="192.168.43.195"
        client = mqtt.Client("P1")
        client.connect(broker_address)
        client.publish("electronica/labs/lab1","0")
        client.publish("electronica/labs/lab2","0")
        client.publish("electronica/labs/lab3","0")
        client.publish("electronica/deposito","0")
    def encendertodo(self):
        global LAB1
        global LAB2
        global LAB3
        global DEP
        LAB1=1
        LAB2=1
        LAB3=1
        DEP=1
        self.AMARILLO.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.VERDE_CLARO.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ROJO.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.VERDE.setStyleSheet("background-color: rgb(255, 255, 255);")
        broker_address="192.168.43.195"
        client = mqtt.Client("P1")
        client.connect(broker_address)
        client.publish("electronica/labs/lab1","1")
        client.publish("electronica/labs/lab2","1")
        client.publish("electronica/labs/lab3","1")
        client.publish("electronica/deposito","1")
    def AMARILLOVEN(self):
        broker_address="192.168.43.195"
        client = mqtt.Client("P36")
        client.connect(broker_address)
        global LAB1
        if(LAB1==0):
            LAB1=1
            self.AMARILLO.setStyleSheet("background-color: rgb(255, 255, 255);")
            client.publish("electronica/labs/lab1","1")
        elif(LAB1==1):
            LAB1=0
            self.AMARILLO.setStyleSheet("background-color: rgb(130, 130, 130);")
            client.publish("electronica/labs/lab1","0")
    def VERDEVEN(self):
        broker_address="192.168.43.195"
        client = mqtt.Client("P1")
        client.connect(broker_address)
        global DEP
        if(DEP==0):
            DEP=1
            client.publish("electronica/deposito","1")
            self.VERDE.setStyleSheet("background-color: rgb(255, 255, 255);")
        elif(DEP==1):
            DEP=0
            client.publish("electronica/deposito","0")
            self.VERDE.setStyleSheet("background-color: rgb(130, 130, 130);")
    def VERDECLAROVEN(self):
        broker_address="192.168.43.195"
        client = mqtt.Client("P1")
        client.connect(broker_address)
        global LAB3
        if(LAB3==0):
            LAB3=1
            client.publish("electronica/labs/lab3","1")
            self.VERDE_CLARO.setStyleSheet("background-color: rgb(255, 255, 255);")
        elif(LAB3==1):
            LAB3=0
            client.publish("electronica/labs/lab3","0")
            self.VERDE_CLARO.setStyleSheet("background-color: rgb(130, 130, 130);")
    def ROJOVEN(self):
        broker_address="192.168.43.195"
        client = mqtt.Client("P1")
        client.connect(broker_address)
        global LAB2
        if(LAB2==0):
            LAB2=1
            client.publish("electronica/labs/lab2","1")
            self.ROJO.setStyleSheet("background-color: rgb(255, 255, 255);")
        elif(LAB2==1):
            LAB2=0
            client.publish("electronica/labs/lab2","0")
            self.ROJO.setStyleSheet("background-color: rgb(130, 130, 130);")


#print("Publishing message to topic","house/bulbs/bulb1")
#client.publish("house/bulbs/bulb1","OFF")
app = QApplication(sys.argv)
main = VentanaInicio()
main.show()
sys.exit(app.exec_())

time.sleep(10) # wait
client.loop_stop() #stop the loop


