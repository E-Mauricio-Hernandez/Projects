import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore, QtTest
import serial
import time

arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)

from PyQt5.QtCore import QPropertyAnimation
import math
import time
global contra1
global contra2
global contra3
global contra4
global contra5
global contra6
global contrador
global intento
global apartamento
global saldoapartamento101
global saldoapartamento102
global saldoapartamento103
global saldoapartamento104
global saldoapartamento105
global saldoapartamento106
global saldotarjeta
saldoapartamento101=0
saldoapartamento102=0
saldoapartamento103=0
saldoapartamento104=0
saldoapartamento105=0
saldoapartamento106=0
saldotarjeta=0

contra1="1234"
contra2="2341"
contra3="3412"
contra4="4123"
contra5="1111"
contra6="4444"
contrador=0
intento=""


class VentanaInicio(QMainWindow):
    def __init__(self):
        super(VentanaInicio, self).__init__()
        loadUi('principal.ui', self)
        self.title = 'servicio de pago'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icon_1.png"))
        self.tarjeta.clicked.connect(self.abrirVentanatarjeta)
        self.apartamento.clicked.connect(self.abrirVentanaapartamento)
        self.botonpago.clicked.connect(self.abrirVentanapago)
        

    def abrirVentanatarjeta(self):
        self.hide()
        otra_ventana = Ventanatarjeta(self)
        otra_ventana.show()
    def abrirVentanaapartamento(self):
        self.hide()
        otra_ventana = Ventanapartamento(self)
        otra_ventana.show()
    def abrirVentanapago(self):
        self.hide()
        otra_ventana = Ventanapago(self)
        otra_ventana.show()
class VentanaInicio2(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaInicio2, self).__init__(parent)
        loadUi('principal.ui', self)
        self.title = 'servicio de pago'
        self.setWindowTitle(self.title)
        self.tarjeta.clicked.connect(self.abrirVentanatarjeta)
        self.apartamento.clicked.connect(self.abrirVentanaapartamento)
        self.botonpago.clicked.connect(self.abrirVentanapago)
        

    def abrirVentanatarjeta(self):
        self.hide()
        otra_ventana = Ventanatarjeta(self)
        otra_ventana.show()
    def abrirVentanaapartamento(self):
        self.hide()
        otra_ventana = Ventanapartamento(self)
        otra_ventana.show()
    def abrirVentanapago(self):
        self.hide()
        otra_ventana = Ventanapago(self)
        otra_ventana.show()

class Ventanapago(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanapago, self).__init__(parent)
        loadUi('apartamentos.ui', self)
        self.title = 'Sistema de pago'
        self.setWindowTitle(self.title)
        self.linea.setText("SELECCIONE EL APARTAMENTO")
        self.uno.clicked.connect(self.abrirVentanapago101)
        self.dos.clicked.connect(self.abrirVentanapago102)
        self.tres.clicked.connect(self.abrirVentanapago103)
        self.cuatro.clicked.connect(self.abrirVentanapago104)
        self.cinco.clicked.connect(self.abrirVentanapago105)
        self.seis.clicked.connect(self.abrirVentanapago106)
        self.volver.clicked.connect(self.abrirVentanavolver)
    def abrirVentanapago101(self):
        global apartamento
        apartamento=101
        self.hide()
        otra_ventana = Ventanapago2(self)
        otra_ventana.show()
    def abrirVentanapago102(self):
        global apartamento
        apartamento=102
        self.hide()
        otra_ventana = Ventanapago2(self)
        otra_ventana.show()
    def abrirVentanapago103(self):
        global apartamento
        apartamento=103
        self.hide()
        otra_ventana = Ventanapago2(self)
        otra_ventana.show()
    def abrirVentanapago104(self):
        global apartamento
        apartamento=104
        self.hide()
        otra_ventana = Ventanapago2(self)
        otra_ventana.show()
    def abrirVentanapago105(self):
        global apartamento
        apartamento=105
        self.hide()
        otra_ventana = Ventanapago2(self)
        otra_ventana.show()
    def abrirVentanapago106(self):
        global apartamento
        apartamento=106
        self.hide()
        otra_ventana = Ventanapago2(self)
        otra_ventana.show()
    def abrirVentanavolver(self):
        self.hide()
        otra_ventana = VentanaInicio2(self)
        otra_ventana.show()

class Ventanapago2(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanapago2, self).__init__(parent)
        loadUi('pago.ui', self)
        global contrador
        global apartamento

        contrador=0
        self.title = 'Sistema de pago'
        self.setWindowTitle(self.title)
        self.linea.setText("INGRESE LA CONTRASEÑA")
        self.uno.clicked.connect(self.contrauno)
        self.dos.clicked.connect(self.contrados)
        self.tres.clicked.connect(self.contratres)
        self.cuatro.clicked.connect(self.contracuatro)
        self.volver.clicked.connect(self.abrirVentanavolver)
    def realizarpago(self):
        global arduino
        global apartamento
        global contra1
        global contra2
        global contra3
        global contra4
        global contra5
        global contra6
        global intento
        global saldoapartamento101
        global saldoapartamento102
        global saldoapartamento103
        global saldoapartamento104
        global saldoapartamento105
        global saldoapartamento106
        global saldotarjeta
        
        if apartamento==101:
            if intento==contra1:
                #LEER TARJETA Y BORRARLA
                #--------------------------------------
                #arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)
                
                QtTest.QTest.qWait(700)

                arduino.write(b'2') #ingresa a funcion leer arduino
                
                QtTest.QTest.qWait(700)

                line = arduino.readline()
                line3 = line.decode('ascii', 'strict')
                print(line3)
                print(type(line3))

                saldo = str(line3)
    
                posi = saldo.find(" ")
                
                saldo = saldo[0:posi]
                
                saldotarjeta = int(saldo)
                print(saldotarjeta)
                print("Retirar")
                QtTest.QTest.qWait(700)
                # aux=str(saldotarjeta)
                '''
                arduino.setDTR(False)
                time.sleep(1)
                arduino.flushInput()
                arduino.setDTR(True)
                '''
                arduino.write(b'1') #ingresa a funcion escribir arduino
                
                QtTest.QTest.qWait(700)
                print("poner")
                borrar = 0
                borrar = str(borrar)
                borrar = bytes(borrar, 'utf-8')
                arduino.write(borrar)
                arduino.write(b'#')
                
                QtTest.QTest.qWait(700)

                arduino.write(b'3') #ya entra en el ardu
                QtTest.QTest.qWait(700)
                #arduino.close()
                #------------------------------------
                saldoapartamento101=saldoapartamento101+saldotarjeta
                #saldotarjeta=0
                self.fin()
                print("final")
            else:
                self.linea.setText("INTENTE DE NUEVO")
                intento=""
        elif apartamento==102:
            if intento==contra2:
                #LEER TARJETA Y BORRARLA
                #--------------------------------------
                #arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)
                
                QtTest.QTest.qWait(700)

                arduino.write(b'2') #ingresa a funcion leer arduino
                
                QtTest.QTest.qWait(700)

                line = arduino.readline()
                line3 = line.decode('ascii', 'strict')
                print(line3)
                print(type(line3))

                saldo = str(line3)
    
                posi = saldo.find(" ")
                
                saldo = saldo[0:posi]
                
                saldotarjeta = int(saldo)
                print(saldotarjeta)
                print("Retirar")
                QtTest.QTest.qWait(700)
                # aux=str(saldotarjeta)
                '''
                arduino.setDTR(False)
                time.sleep(1)
                arduino.flushInput()
                arduino.setDTR(True)
                '''
                arduino.write(b'1') #ingresa a funcion escribir arduino
                
                QtTest.QTest.qWait(700)
                print("poner")
                borrar = 250
                borrar = str(borrar)
                borrar = bytes(borrar, 'utf-8')
                arduino.write(borrar)
                arduino.write(b'#')
                
                QtTest.QTest.qWait(700)

                arduino.write(b'4') #ya entra en el ardu
                QtTest.QTest.qWait(700)
                #arduino.close()
                #------------------------------------
                saldoapartamento102=saldoapartamento102+saldotarjeta
                #saldotarjeta=0
                self.fin()
            else:
                self.linea.setText("INTENTE DE NUEVO")
                intento=""
        elif apartamento==103:
            if intento==contra3:
                #LEER TARJETA Y BORRARLA
                #--------------------------------------
                #arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)
                
                QtTest.QTest.qWait(2000)

                arduino.write(b'2') #ingresa a funcion leer arduino
                
                QtTest.QTest.qWait(1000)

                line = arduino.readline()
                line3 = line.decode('ascii', 'strict')
                print(line3)
                print(type(line3))

                saldo = str(line3)
    
                posi = saldo.find(" ")
                
                saldo = saldo[0:posi]
                
                saldotarjeta = int(saldo)
                print(saldotarjeta)
                print("Retirar")
                QtTest.QTest.qWait(2000)
                # aux=str(saldotarjeta)
                '''
                arduino.setDTR(False)
                time.sleep(1)
                arduino.flushInput()
                arduino.setDTR(True)
                '''
                arduino.write(b'1') #ingresa a funcion escribir arduino
                
                QtTest.QTest.qWait(1000)
                print("poner")
                borrar = 000
                borrar = str(borrar)
                borrar = bytes(borrar, 'utf-8')
                arduino.write(borrar)
                arduino.write(b'#')
                
                QtTest.QTest.qWait(2000)

                arduino.write(b'5') #ya entra en el ardu
                QtTest.QTest.qWait(500)
                #arduino.close()
                #------------------------------------
                saldoapartamento103=saldoapartamento103+saldotarjeta
                #saldotarjeta=0
                self.fin()
            else:
                self.linea.setText("INTENTE DE NUEVO")
                intento=""
        elif apartamento==104:
            if intento==contra4:
                #LEER TARJETA Y BORRARLA
                #--------------------------------------
                #arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)
                
                QtTest.QTest.qWait(2000)

                arduino.write(b'2') #ingresa a funcion leer arduino
                
                QtTest.QTest.qWait(1000)

                line = arduino.readline()
                line3 = line.decode('ascii', 'strict')
                print(line3)
                print(type(line3))

                saldo = str(line3)
    
                posi = saldo.find(" ")
                
                saldo = saldo[0:posi]
                
                saldotarjeta = int(saldo)
                print(saldotarjeta)
                print("Retirar")
                QtTest.QTest.qWait(2000)
                # aux=str(saldotarjeta)
                '''
                arduino.setDTR(False)
                time.sleep(1)
                arduino.flushInput()
                arduino.setDTR(True)
                '''
                arduino.write(b'1') #ingresa a funcion escribir arduino
                
                QtTest.QTest.qWait(1000)
                print("poner")
                borrar = 000
                borrar = str(borrar)
                borrar = bytes(borrar, 'utf-8')
                arduino.write(borrar)
                arduino.write(b'#')
                
                QtTest.QTest.qWait(2000)

                arduino.write(b'6') #ya entra en el ardu
                QtTest.QTest.qWait(500)
                #arduino.close()
                #------------------------------------
                saldoapartamento104=saldoapartamento104+saldotarjeta
                #saldotarjeta=0
                self.fin()
            else:
                self.linea.setText("INTENTE DE NUEVO")
                intento=""
        
        elif apartamento==105:
            if intento==contra5:
               #LEER TARJETA Y BORRARLA
                #--------------------------------------
                #arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)
                
                QtTest.QTest.qWait(2000)

                arduino.write(b'2') #ingresa a funcion leer arduino
                
                QtTest.QTest.qWait(1000)

                line = arduino.readline()
                line3 = line.decode('ascii', 'strict')
                print(line3)
                print(type(line3))

                saldo = str(line3)
    
                posi = saldo.find(" ")
                
                saldo = saldo[0:posi]
                
                saldotarjeta = int(saldo)
                print(saldotarjeta)
                print("Retirar")
                QtTest.QTest.qWait(2000)
                # aux=str(saldotarjeta)
                '''
                arduino.setDTR(False)
                time.sleep(1)
                arduino.flushInput()
                arduino.setDTR(True)
                '''
                arduino.write(b'1') #ingresa a funcion escribir arduino
                
                QtTest.QTest.qWait(1000)
                print("poner")
                borrar = 000
                borrar = str(borrar)
                borrar = bytes(borrar, 'utf-8')
                arduino.write(borrar)
                arduino.write(b'#')
                
                QtTest.QTest.qWait(2000)

                arduino.write(b'7') #ya entra en el ardu
                QtTest.QTest.qWait(500)
                #arduino.close()
                #------------------------------------
                saldoapartamento105=saldoapartamento105+saldotarjeta
                #saldotarjeta=0
                self.fin()
            else:
                self.linea.setText("INTENTE DE NUEVO")
                intento=""
        elif apartamento==106:
            if intento==contra6:
               #LEER TARJETA Y BORRARLA
                #--------------------------------------
                #arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)
                
                QtTest.QTest.qWait(2000)

                arduino.write(b'2') #ingresa a funcion leer arduino
                
                QtTest.QTest.qWait(1000)

                line = arduino.readline()
                line3 = line.decode('ascii', 'strict')
                print(line3)
                print(type(line3))

                saldo = str(line3)
    
                posi = saldo.find(" ")
                
                saldo = saldo[0:posi]
                
                saldotarjeta = int(saldo)
                print(saldotarjeta)
                print("Retirar")
                QtTest.QTest.qWait(2000)
                # aux=str(saldotarjeta)
                '''
                arduino.setDTR(False)
                time.sleep(1)
                arduino.flushInput()
                arduino.setDTR(True)
                '''
                arduino.write(b'1') #ingresa a funcion escribir arduino
                
                QtTest.QTest.qWait(1000)
                print("poner")
                borrar = 000
                borrar = str(borrar)
                borrar = bytes(borrar, 'utf-8')
                arduino.write(borrar)
                arduino.write(b'#')
                
                QtTest.QTest.qWait(2000)

                arduino.write(b'8') #ya entra en el ardu
                QtTest.QTest.qWait(500)
                #arduino.close()
                #------------------------------------
                saldoapartamento106=saldoapartamento106+saldotarjeta
                #saldotarjeta=0
                self.fin()
            else:
                self.linea.setText("INTENTE DE NUEVO")
                intento=""

    def contrauno(self):
        global intento
        global contrador
        if contrador<3:
            intento=intento+"1"
            contrador=contrador+1
        else:
            intento=intento+"1"
            contrador=0
            self.realizarpago()
    def contrados(self):
        global intento
        global contrador
        if contrador<3:
            intento=intento+"2"
            contrador=contrador+1

        else:
            intento=intento+"2"
            contrador=0
            self.realizarpago()
    def contratres(self):
        global intento
        global contrador
        if contrador<3:
            intento=intento+"3"
            contrador=contrador+1
        else:
            intento=intento+"3"
            contrador=0
            self.realizarpago()
    def contracuatro(self):
        global intento
        global contrador
        if contrador<3:
            intento=intento+"4"
            contrador=contrador+1
        else:
            intento=intento+"4"
            contrador=0
            self.realizarpago()

    def abrirVentanavolver(self):
        self.hide()
        otra_ventana = Ventanapago(self)
        otra_ventana.show()
    def fin(self):
        self.hide()
        otra_ventana = Ventanafin(self)
        otra_ventana.show()
class Ventanafin(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanafin, self).__init__(parent)
        loadUi('pagofinal.ui', self)
        global contrador
        contrador=0
        self.title = 'Sistema de pago'
        self.setWindowTitle(self.title)
        self.linea.setText("PAGO REALIZADO CON EXITO")
        self.volver.clicked.connect(self.abrirVentanavolver)
    def abrirVentanavolver(self):
        self.hide()
        otra_ventana = VentanaInicio2(self)
        otra_ventana.show()
    
class Ventanatarjeta(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanatarjeta, self).__init__(parent)
        loadUi('principal.ui', self)
        global contrador
        global arduino
        contrador=0
        global saldotarjeta

        aux = "vuelva a empezar"

        #--------------------------------------
        #AQUI REALIZAR LA LECTURA TARJETA
        #arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)
        print("SALDO")
        '''
        arduino.setDTR(False)
        time.sleep(1)
        arduino.flushInput()
        arduino.setDTR(True)
		'''
        
        QtTest.QTest.qWait(120)

        arduino.write(b'2') #ingresa a funcion leer arduino

        QtTest.QTest.qWait(50)

        line = arduino.readline()
        line3 = line.decode('ascii', 'strict')
        print("line3: ", line3)
        # aux=str(saldotarjeta)
        saldo = str(line3)
    
        posi = saldo.find(" ")
        
        saldo = saldo[0:posi]
        aux = int(saldo)
        aux = str(aux)
        #arduino.close()
        print(aux)
        #------------------------------------
        self.title = 'Sistema de pago'
        self.setWindowTitle(self.title)
        self.linea.setText(aux)
        self.apartamento.clicked.connect(self.abrirVentanaapartamento)
        self.botonpago.clicked.connect(self.abrirVentanapago)
        

    def abrirVentanaapartamento(self):
        self.hide()
        otra_ventana = Ventanapartamento(self)
        otra_ventana.show()
    def abrirVentanapago(self):
        self.hide()
        otra_ventana = Ventanapago(self)
        otra_ventana.show()
class Ventanapartamento(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanapartamento, self).__init__(parent)
        loadUi('apartamentos.ui', self)
        self.title = 'Sistema de pago'
        self.setWindowTitle(self.title)
        self.linea.setText("SELECCIONE EL APARTAMENTO")
        self.uno.clicked.connect(self.abrirVentanapago101)
        self.dos.clicked.connect(self.abrirVentanapago102)
        self.tres.clicked.connect(self.abrirVentanapago103)
        self.cuatro.clicked.connect(self.abrirVentanapago104)
        self.cinco.clicked.connect(self.abrirVentanapago105)
        self.seis.clicked.connect(self.abrirVentanapago106)
        self.volver.clicked.connect(self.abrirVentanavolver)
    def abrirVentanapago101(self):
        global apartamento
        global saldoapartamento101
        # PEDIRLE AL ARDUINO EL SALDO
        arduino.write(b'9')
        QtTest.QTest.qWait(200)
        line = arduino.readline()
        line3 = line.decode('ascii', 'strict')
        print(line3)
        #aux = line3
        saldoapartamento101 = int(float(line3))
        #---------------------------
        aux=str(saldoapartamento101)
        self.linea.setText(aux)
    def abrirVentanapago102(self):
        global apartamento
        global saldoapartamento102
        # PEDIRLE AL ARDUINO EL SALDO
        arduino.write(b'0')
        QtTest.QTest.qWait(200)
        line = arduino.readline()
        line3 = line.decode('ascii', 'strict')
        print(line3)
        #aux = line3
        saldoapartamento102 = int(float(line3))
        #---------------------------
        aux=str(saldoapartamento102)
        self.linea.setText(aux)
    def abrirVentanapago103(self):
        global apartamento
        global saldoapartamento103
        # PEDIRLE AL ARDUINO EL SALDO
        arduino.write(b'$')
        QtTest.QTest.qWait(200)
        line = arduino.readline()
        line3 = line.decode('ascii', 'strict')
        print(line3)
        #aux = line3
        saldoapartamento103 = int(float(line3))
        #---------------------------
        aux=str(saldoapartamento103)
        self.linea.setText(aux)
    def abrirVentanapago104(self):
        global apartamento
        global saldoapartamento104
        # PEDIRLE AL ARDUINO EL SALDO
        arduino.write(b'%')
        QtTest.QTest.qWait(200)
        line = arduino.readline()
        line3 = line.decode('ascii', 'strict')
        print(line3)
        #aux = line3
        saldoapartamento104 = int(float(line3))
        #---------------------------
        aux=str(saldoapartamento104)
        self.linea.setText(aux)
    def abrirVentanapago105(self):
        global apartamento
        global saldoapartamento105
        # PEDIRLE AL ARDUINO EL SALDO
        arduino.write(b'&')
        QtTest.QTest.qWait(200)
        line = arduino.readline()
        line3 = line.decode('ascii', 'strict')
        print(line3)
        #aux = line3
        saldoapartamento105 = int(float(line3))
        #---------------------------
        aux=str(saldoapartamento105)
        self.linea.setText(aux)
    def abrirVentanapago106(self):
        global apartamento
        global saldoapartamento106
        # PEDIRLE AL ARDUINO EL SALDO
        arduino.write(b'/')
        QtTest.QTest.qWait(200)
        line = arduino.readline()
        line3 = line.decode('ascii', 'strict')
        print(line3)
        #aux = line3
        saldoapartamento106 = int(float(line3))
        #---------------------------
        aux=str(saldoapartamento106)
        self.linea.setText(aux)
    def abrirVentanavolver(self):
        self.hide()
        otra_ventana = VentanaInicio2(self)
        otra_ventana.show()

app = QApplication(sys.argv)
main = VentanaInicio()
main.show()
sys.exit(app.exec_())
