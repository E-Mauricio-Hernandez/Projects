import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore
import LogoU_rc
import Motor_rc
import numpy as np
import math
import cv2
import os
pi = math.pi
raiz3 = 1.732050808
import time
global n
global matriz
global redes
global m
global deltabool
deltabool=0
m=1
n=1
class VentanaInicio(QMainWindow):
    def __init__(self):
        super(VentanaInicio, self).__init__()
        loadUi('Inicio.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icon_1.png"))
        self.pushButton_C.clicked.connect(self.abrirVentanaGenerador)
        self.pushButton_S.clicked.connect(self.close)

    def abrirVentanaGenerador(self):
        self.hide()
        otra_ventana = VentanaGenerador(self)
        otra_ventana.show()

class VentanaGenerador(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaGenerador, self).__init__(parent)
        loadUi('Generador.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.pushButton_C.clicked.connect(self.abrirVentanaCantidadTransformador)
        self.pushButton_R.clicked.connect(self.abrirVentanaInicio)
        self.pushButton_G.clicked.connect(self.datosGenerador)
        self.lineEdit_F.returnPressed.connect(self.pushButton_G.click)

    def abrirVentanaCantidadTransformador(self):
        global redes
        self.hide()
        otra_ventana = VentanaCantidadTransformador(self)
        otra_ventana.show()

    def abrirVentanaInicio(self):
        self.parent().show()
        self.close()

    @QtCore.pyqtSlot()  
    def datosGenerador(self):
        global a
        global redes
        a = self.lineEdit_F.text() 
        redes=[0]*int(a)

class VentanaCantidadTransformador(VentanaGenerador, QMainWindow):
    def __init__(self, parent=None):
        global a
        global n
        global trifasica
        bandera=0
        super(VentanaCantidadTransformador, self).__init__(parent)
        loadUi('numeromaquinas.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        aux=str(n)
        self.datos_red.setText(aux)
        self.maquinasred.returnPressed.connect(self.botonguardar.click)
        self.okboton.clicked.connect(self.numerodeveces)
        self.botonguardar.clicked.connect(self.datos)
        
    def numerodeveces(self):
        global a
        global n
        self.hide()
        if int(a)>n:
            n+=1
            otra_ventana=VentanaCantidadTransformador(self)
            otra_ventana.show()
        else:
            n=1
            self.siguienteventana1()
    def siguienteventana1(self):
        global matriz
        global maximo
        maximo=max(redes)+1
        matriz=np.zeros ((maximo,11,int(a)),np.float32)
        
        self.hide()
        otra_ventana = ventanadatosred(self)
        otra_ventana.show()
    @QtCore.pyqtSlot()
    def datos(self):
        global n
        redes[n-1]=int(self.maquinasred.text())

class ventanadatosred(VentanaCantidadTransformador, QMainWindow):

    def __init__(self, parent=None):
        global a
        global n
        global trifasica
        global matriz
        global trifasica
        trifasica=0
        super(VentanaCantidadTransformador, self).__init__(parent)
        loadUi('CantidadTransformador.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        aux=str(n)
        self.datos_red.setText(aux)
        self.voltajered.returnPressed.connect(self.botonguardar.click)
        self.frecuenciared.returnPressed.connect(self.botonguardar.click)
        self.okboton.clicked.connect(self.numerodeveces)
        self.checkBox_Si.stateChanged.connect(self.estadotrifasica)
        self.botonguardar.clicked.connect(self.datos1)
    def estadotrifasica(self):
        global trifasica
        if (trifasica==0):
            trifasica=1
        else:
            trifasica=0
    def numerodeveces(self):
        global a
        global n
        global matriz
        global redes
        global trifasica
        self.hide()
        if int(a)>n:
            n+=1
            otra_ventana=ventanadatosred(self)
            otra_ventana.show()
        else:
            n=1
            self.siguienteventana()
    @QtCore.pyqtSlot()
    def datos1(self):
        global n
        global a
        global matriz
        global trifasica
        global redes
        global maximo
        
        for j in range (0,maximo):
            matriz[j,0,n-1]=float(self.voltajered.text())
            matriz[j,7,n-1]=trifasica
            matriz[j,10,n-1]=float(self.frecuenciared.text())
    def siguienteventana(self):
        self.hide()
        otra_ventana = ventanadatosmaquina(self)
        otra_ventana.show() 

class ventanadatosmaquina(ventanadatosred, QMainWindow):
    def __init__(self, parent=None):
        global a
        global n
        global m
        global trifasica
        global estrella
        global matriz
        global trifasica
        estrella=0
        super(VentanaCantidadTransformador, self).__init__(parent)
        loadUi('datosmaquinas.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        aux=str(m)
        aux1=str(n)
        self.datos_red.setText(aux)
        self.datos_maquinas.setText(aux1)
        self.hpmaquina.returnPressed.connect(self.botonguardar.click)
        self.fpmaquina.returnPressed.connect(self.botonguardar.click)
        self.okboton.clicked.connect(self.numerodeveces)
        self.estrellaboton.stateChanged.connect(self.estadoestrella)
        self.botonguardar.clicked.connect(self.datos1)  

    def estadoestrella(self):
        global estrella
        if (estrella==0):
            estrella=1
        else:
            estrella=0
    def numerodeveces2(self):
        global a
        global n
        global m
        global matriz
        global redes
        global trifasica
        if int(a)>n:
            n+=1
            otra_ventana=ventanadatosmaquina(self)
            otra_ventana.show()
        else:
            n=1
            self.siguienteventana()
    def numerodeveces(self):
        global a
        global n
        global m
        global matriz
        global redes
        global trifasica    
        self.hide()
        j=n-1
        if int(redes[j])>m:
            m+=1
            otra_ventana=ventanadatosmaquina(self)
            otra_ventana.show()
        else:
            m=1
            self.numerodeveces2()
    @QtCore.pyqtSlot()
    def datos1(self):
        global n
        global a
        global m
        global matriz
        global trifasica
        global redes
        global maximo
        global estrella
        matriz[m,2,n-1]=float(self.hpmaquina.text())*746
        matriz[m,3,n-1]=float(self.fpmaquina.text())
        ayuda=float(self.fpmaquina.text())
        if ayuda>1:
            matriz[m,3,n-1]=0.8
        else:
            matriz[m,3,n-1]=ayuda
        if(matriz[m,7,n-1]==0):
            matriz[m,8,n-1]=2
        else:
            matriz[m,8,n-1]=estrella
        def corriente (p,v,fp,var):
            variable=raiz3
            if var==0:
                variable=1
            i=p/(v*fp*variable);
            return(i)
        def potenciareactiva (v,i,var,fp):
            variable=raiz3
            if var==0:
                variable=1
            q=v*i*variable*math.sin(math.acos(fp));
            return (q)
        def aparente (v,i,var):
            variable=raiz3
            if var==0:
                variable=1
            s=v*i*variable;
            return(s)

        matriz[m,1,n-1]=corriente(matriz[m,2,n-1],matriz[m,0,n-1],matriz[m,3,n-1],matriz[m,7,n-1])
        matriz[m,4,n-1]=potenciareactiva(matriz[m,0,n-1],matriz[m,1,n-1],matriz[m,7,n-1],matriz[m,3,n-1])
        matriz[m,5,n-1]=aparente(matriz[m,0,n-1],matriz[m,1,n-1],matriz[m,7,n-1])

    def siguienteventana(self):
        global redes
        global matriz
        self.hide()
        for i in range(0,int(a)):
            volred=matriz[0,0,i]
            corred=0
            reared=0
            actred=0
            apared=0
            facred=0
            variabletri=raiz3
            var=matriz[0,7,i]
            if var==0:
                variabletri=1
            for j in range(0,redes[i]):
                actred=matriz[j+1,2,i]+actred
                reared=matriz[j+1,4,i]+reared
            apared=math.sqrt((actred**2)+(reared**2))
            factor=math.cos(math.atan(reared/actred))
            matriz[0,3,i]=factor
            corred=actred/(volred*matriz[0,3,i]*variabletri)
            matriz[0,1,i]=corred
            matriz[0,2,i]=actred
            matriz[0,4,i]=reared
            matriz[0,5,i]=apared
        otra_ventana = ventanadatoideal(self)
        otra_ventana.show()

class ventanadatoideal(ventanadatosred, QMainWindow):
    def __init__(self, parent=None):
        global a
        global n
        global m
        global trifasica
        global estrella
        global matriz
        global trifasica
        estrella=0
        super(VentanaCantidadTransformador, self).__init__(parent)
        loadUi('ideal.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.valorideal.returnPressed.connect(self.botonguardar.click)
        self.okboton.clicked.connect(self.siguienteventana)
        self.botonguardar.clicked.connect(self.datos1)
        self.checkdelta.stateChanged.connect(self.estadodelta)  

    def datos1(self):
        global deltabool
        ideal=float(self.valorideal.text())
        if ideal<0 or ideal>1:
            ideal=1
        for i in range(0,int(a)):
            matriz[0,9,i]=ideal
            teta=math.acos(matriz[0,9,i])
            q2=math.tan(teta)*matriz[0,2,i]
            dif=matriz[0,4,i]-q2
            if matriz[0,7,i]==0:
                capa=dif/((matriz[0,0,i]**2)*(2*math.pi*matriz[0,10,i]))
                matriz[0,6,i]=capa
            else:
                if deltabool==1:
                    capa=dif/((matriz[0,0,i]**2)*(2*math.pi*matriz[0,10,i]))
                    matriz[0,6,i]=capa

                else:
                    capa=dif/(((matriz[0,0,i]/3)**2)*(2*math.pi*matriz[0,10,i]))
                    matriz[0,6,i]=capa
    def siguienteventana(self):
        otra_ventana = muestrafinal(self)
        otra_ventana.show()
        self.hide()

    def estadodelta(self):
        global deltabool
        if (deltabool==0):
            deltabool=1
        else:
            deltabool=0

class muestrafinal(ventanadatosred, QMainWindow):
    def __init__(self, parent=None):
        global a
        global n
        global m
        global trifasica
        global estrella
        global matriz
        global trifasica
        super(VentanaCantidadTransformador, self).__init__(parent)
        loadUi('final.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.varred.setText(str(n))
        self.varvoltaje.setText(str(matriz[0,0,n-1]))
        self.varcorriente.setText(str(matriz[0,1,n-1]))
        self.varactiva.setText(str(matriz[0,2,n-1]))
        self.varreactiva.setText(str(matriz[0,4,n-1]))
        self.varaparente.setText(str(matriz[0,5,n-1]))
        self.varcapa.setText(str(matriz[0,6,n-1]))
        self.varfp.setText(str(matriz[0,3,n-1]))
        self.okboton.clicked.connect(self.numerodeveces) 


    def siguienteventana(self):
        self.hide()
        otra_ventana = VentanaFin(self)
        otra_ventana.show()
    def numerodeveces(self):
        global a
        global n
        global matriz
        global redes
        global trifasica
        self.hide()
        if int(a)>n:
            n+=1
            otra_ventana=muestrafinal(self)
            otra_ventana.show()
        else:
            n=1
            self.grafica()
    def grafica(self):
        global matriz
        global a
        global redes
        imagen = cv2.imread('VISUALIZACION/img4.png' , cv2.IMREAD_COLOR)
        for i in range(0,int(a)):
            if matriz[1,7,i]==0:
                imagen2= cv2.imread('VISUALIZACION/img1mono.png' , cv2.IMREAD_COLOR)
                imagen = np.concatenate((imagen, imagen2), axis=1)
                cv2.imwrite('salida.png', imagen)
            elif matriz[1,8,i]==0:
                imagen2= cv2.imread('VISUALIZACION/img1triestre.png' , cv2.IMREAD_COLOR)
                imagen = np.concatenate((imagen, imagen2), axis=1)
                cv2.imwrite('salida.png', imagen)
            elif matriz[1,8,i]==1:
                imagen2= cv2.imread('VISUALIZACION/img1tridelta.png' , cv2.IMREAD_COLOR)
                imagen = np.concatenate((imagen, imagen2), axis=1)
                cv2.imwrite('salida.png', imagen)
            for j in range(1,redes[i]):
                if matriz[j+1,7,i]==0:
                    imagen2= cv2.imread('VISUALIZACION/img2mono.png' , cv2.IMREAD_COLOR)
                    imagen = np.concatenate((imagen, imagen2), axis=1)
                    cv2.imwrite('salida.png', imagen)
                elif matriz[j+1,8,i]==1:
                    imagen2= cv2.imread('VISUALIZACION/img2tridelta.png' , cv2.IMREAD_COLOR)
                    imagen = np.concatenate((imagen, imagen2), axis=1)
                    cv2.imwrite('salida.png', imagen)
                elif matriz[j+1,8,i]==0:
                    imagen2= cv2.imread('VISUALIZACION/img2triestre.png' , cv2.IMREAD_COLOR)
                    imagen = np.concatenate((imagen, imagen2), axis=1)
                    cv2.imwrite('salida.png', imagen)
            if matriz[1,7,i]==0:
                imagen2= cv2.imread('VISUALIZACION/img3mono.png' , cv2.IMREAD_COLOR)
                imagen = np.concatenate((imagen, imagen2), axis=1)
                cv2.imwrite('salida.png', imagen)
            elif matriz[1,7,i]==1:
                imagen2= cv2.imread('VISUALIZACION/img3tri.png' , cv2.IMREAD_COLOR)
                imagen = np.concatenate((imagen, imagen2), axis=1)
                cv2.imwrite('salida.png', imagen)
        imagen2= cv2.imread('VISUALIZACION/img4.png' , cv2.IMREAD_COLOR)
        imagen = np.concatenate((imagen, imagen2), axis=1)
        imagenintegrantes=cv2.imread('integrantes.png' , cv2.IMREAD_COLOR)
        cv2.imshow ('sistema ', imagen)
        cv2.waitKey()
        cv2.destroyAllWindows()
        cv2.imshow ('integrantes ', imagenintegrantes)
        cv2.waitKey()
        cv2.destroyAllWindows()
        self.siguienteventana()
            
class VentanaFin(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaFin, self).__init__(parent)
        loadUi('Fin.ui', self)
        self.title = 'Universidad de los llanos'
        self.setWindowTitle(self.title)
        self.pushButton_S.clicked.connect(self.close)

app = QApplication(sys.argv)
main = VentanaInicio()
main.show()
sys.exit(app.exec_())
