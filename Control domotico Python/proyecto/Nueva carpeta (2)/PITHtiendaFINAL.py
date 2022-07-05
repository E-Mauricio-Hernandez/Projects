from PITH_ui import *
import serial
import time
from flask import Flask, render_template
from PyQt5 import QtCore, QtTest
global aux
import os
import datetime
aux=0
#arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)

DATO = 0.0
vkwh = 400.0

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow): #
	
	def __init__(self, *args, **kwargs):
		global vkwh
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.pkwh.setText(str(vkwh))
		self.pushButton.clicked.connect(self.saldo)
		self.pushButton_2.clicked.connect(self.recarga)

	def saldo(self):
		global DATO
		global vkwh
		print("SALDO")
		arduino = serial.Serial('COM13', baudrate=9600, timeout = 1.0)
		'''
		arduino.setDTR(False)
		time.sleep(1)
		arduino.flushInput()
		arduino.setDTR(True)
		'''
		#time.sleep(2) #importantisimo esto
		QtTest.QTest.qWait(2000)

		arduino.write(b'2') #ingresa a funcion LEER arduino
		QtTest.QTest.qWait(700)

		line = arduino.readline()
		line3 = line.decode('ascii', 'strict')
		
		saldo = str(line3)
	
		posi = saldo.find(" ")
		
		saldo = saldo[0:posi]

		DATO = int(saldo)
		print(DATO)
		
		self.label.setText(saldo)
		arduino.close()

	def recarga(self):
		global DATO
		global vkwh
		print("RECARGAR")
		arduino = serial.Serial('COM13', baudrate=9600, timeout = 1.0)
		dato = int(self.lineEdit.text())
		dato = dato/vkwh
		estafaU = int((dato - int(dato))*vkwh)
		if estafaU < 50 :
			estafaU = 50
		dato = int(dato)
		dato2=str(dato)  


		self.label.setText(str(dato))
		#self.lineEdit.clear()
		
		#self.lineEdit.setText("LISTONES")
		'''
		arduino.setDTR(False)
		time.sleep(1)
		arduino.flushInput()
		arduino.setDTR(True)
		'''

		QtTest.QTest.qWait(2000)
		arduino.write(b'1') #ingresa a funcion escribir arduino
		QtTest.QTest.qWait(700)

		dato = DATO + dato

		#-----------------------------
		dato = str(dato)
		f = open ('datos.txt','r')
		mensaje = f.read()
		aux =mensaje.split(",")
		aux[9]=aux[8]
		aux[8]=aux[7]
		aux[7]=aux[6]
		aux[6]=aux[5]
		aux[5]=aux[4]
		aux[4]=aux[3]
		aux[3]=aux[2]
		aux[2]=aux[1]
		aux[1]=aux[0]
		aux[0]=dato2
		now = datetime.datetime.now()
		timeString = now.strftime("%Y-%m-%d %H:%M:%S")
		aux[19]=aux[18]
		aux[18]=aux[17]
		aux[17]=aux[16]
		aux[16]=aux[15]
		aux[15]=aux[14]
		aux[14]=aux[13]
		aux[13]=aux[12]
		aux[12]=aux[11]
		aux[11]=aux[10]
		aux[10]=timeString
		f.close()
		f = open ('datos.txt','w')
		f.write(aux[0]+","+aux[1]+","+aux[2]+","+aux[3]+","+aux[4]+","+aux[5]+","+aux[6]+","+aux[7]+","+aux[8]+","+aux[9]+","+aux[10]+","+aux[11]+","+aux[12]+","+aux[13]+","+aux[14]+","+aux[15]+","+aux[16]+","+aux[17]+","+aux[18]+","+aux[19]+","+aux[20])
		f.close()
		dato = bytes(dato, 'utf-8')
		arduino.write(dato)
		arduino.write(b'#')

		self.label.setText("listones")
		print("ya mi pez")
		self.vueltas.setText(str(estafaU))
		#------------------------------------------
		'''
		line = arduino.readline()
		line2 = line.decode('ascii', 'strict')
		print(line2)
		'''
		arduino.close()



if __name__ == "__main__":
	appp = QtWidgets.QApplication([])
	window = MainWindow()
	
	window.show()
	appp.exec_()		    

	
	




'''
ESTRUCTURA BASICA PARA EMPEZAR
from PITH_ui import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow): #
	
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()
'''