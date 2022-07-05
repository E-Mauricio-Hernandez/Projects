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
import time
class VentanaInicio(QMainWindow):
    
    def __init__(self):
        super(VentanaInicio, self).__init__()
        loadUi('DOS.ui', self)
        self.low.clicked.connect(self.forma1)
        self.low_2.clicked.connect(self.forma2)
        self.low_3.clicked.connect(self.forma3)
        self.low_4.clicked.connect(self.forma4)
        self.low_5.clicked.connect(self.forma5)
        self.low_6.clicked.connect(self.forma6)
        self.low_7.clicked.connect(self.forma7)
        self.low_8.clicked.connect(self.forma8)


    
    def forma1(self):
        f = open ('datos.txt','wb')
        f.write('1')
        f.close()
    def forma2(self):
        f = open ('datos.txt','wb')
        f.write('2')
        f.close()
    def forma3(self):
        f = open ('datos.txt','wb')
        f.write('3')
        f.close()
    def forma4(self):
        f = open ('datos.txt','wb')
        f.write('4')
        f.close()
    def forma5(self):
        f = open ('datos.txt','wb')
        f.write('5')
        f.close()
    def forma6(self):
        f = open ('datos.txt','wb')
        f.write('6')
        f.close()
    def forma7(self):
        f = open ('datos.txt','wb')
        f.write('7')
        f.close()
    def forma8(self):
        f = open ('datos.txt','wb')
        f.write('8')
        f.close()



app = QApplication(sys.argv)
main = VentanaInicio()
main.show()
sys.exit(app.exec_())



