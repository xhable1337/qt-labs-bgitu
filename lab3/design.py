# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 160)
        MainWindow.setMinimumSize(QtCore.QSize(450, 160))
        MainWindow.setMaximumSize(QtCore.QSize(450, 160))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.field_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.field_1.setGeometry(QtCore.QRect(260, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Circe Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.field_1.setFont(font)
        self.field_1.setPlaceholderText("")
        self.field_1.setObjectName("field_1")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(20, 20, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Circe")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox_1")
        self.field_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.field_2.setGeometry(QtCore.QRect(260, 60, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Circe Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.field_2.setFont(font)
        self.field_2.setPlaceholderText("")
        self.field_2.setObjectName("field_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 70, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Circe")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.field_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.field_3.setGeometry(QtCore.QRect(260, 110, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Circe Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.field_3.setFont(font)
        self.field_3.setPlaceholderText("")
        self.field_3.setObjectName("field_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 120, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Circe")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тест чекбоксов"))
        self.field_1.setText(_translate("MainWindow", "Здравствуйте!"))
        self.checkBox_1.setText(_translate("MainWindow", "Переключить поле 1"))
        self.field_2.setText(_translate("MainWindow", "Добрый день!"))
        self.checkBox_2.setText(_translate("MainWindow", "Переключить поле 2"))
        self.field_3.setText(_translate("MainWindow", "Приветствую!"))
        self.checkBox_3.setText(_translate("MainWindow", "Переключить поле 3"))