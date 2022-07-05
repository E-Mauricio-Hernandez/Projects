import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtTest
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'inicio'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 700
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('ima1.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()
        QtTest.QTest.qWait(4000)
        self.hide()
        self.imagen2()
    def imagen2(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('ima2.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()
        QtTest.QTest.qWait(4000)
        self.hide()
        self.imagen3()
    def imagen3(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('ima3.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()
        QtTest.QTest.qWait(4000)
        self.hide()
        self.imagen4()
    def imagen4(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('ima4.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()
        QtTest.QTest.qWait(4000)
        self.hide()
        self.imagen5()
    def imagen5(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('ima5.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()
        QtTest.QTest.qWait(4000)
        self.hide()
        self.imagen6()
    def imagen6(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('ima7.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()
        QtTest.QTest.qWait(4000)
        self.hide()
        self.imagen7()
    def imagen7(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('ima6.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()
        QtTest.QTest.qWait(8000)
        self.hide()
        self.initUI()


 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())