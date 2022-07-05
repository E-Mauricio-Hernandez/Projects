# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PITHInterfaz.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 302)
        MainWindow.setStyleSheet("background-color: rgb(14, 124, 123);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 90, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(191, 4, 45);\n"
"background-color: rgb(212, 244, 221);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 90, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(173, 4, 40);\n"
"background-color: rgb(23, 190, 187);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 144, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(19)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(191, 4, 45);\n"
"background-color: rgb(23, 190, 187);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 145, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(191, 4, 45);\n"
"background-color: rgb(212, 244, 221);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(45, 25, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(45)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(238, 6, 56);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(212, 244, 221);")
        self.label_3.setObjectName("label_3")
        self.pkwh = QtWidgets.QLabel(self.centralwidget)
        self.pkwh.setGeometry(QtCore.QRect(269, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pkwh.setFont(font)
        self.pkwh.setStyleSheet("color: rgb(212, 244, 221);")
        self.pkwh.setObjectName("pkwh")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(212, 244, 221);")
        self.label_4.setObjectName("label_4")
        self.vueltas = QtWidgets.QLabel(self.centralwidget)
        self.vueltas.setGeometry(QtCore.QRect(269, 250, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.vueltas.setFont(font)
        self.vueltas.setStyleSheet("color: rgb(212, 244, 221);")
        self.vueltas.setObjectName("vueltas")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "kWh"))
        self.pushButton_2.setText(_translate("MainWindow", "RECARGAR"))
        self.label_2.setText(_translate("MainWindow", "P.I.T.H. Software"))
        self.label_3.setText(_translate("MainWindow", "Valor kWh actual:         $"))
        self.pkwh.setText(_translate("MainWindow", "500"))
        self.label_4.setText(_translate("MainWindow", "Devolver:                        $"))
        self.vueltas.setText(_translate("MainWindow", "0"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
