# -*- coding: utf-8 -*-

# Form implementation generated from reading sui file 'HowtoUse_step1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HowtoUse_step1(object):
    def setupUi(self, HowtoUse_step1):
        HowtoUse_step1.setObjectName("selectExercise")
        HowtoUse_step1.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_heart/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HowtoUse_step1.setWindowIcon(icon)
        HowtoUse_step1.setStyleSheet("background-color:\"Aliceblue\";")
        self.selectTitle = QtWidgets.QLabel(HowtoUse_step1)
        self.selectTitle.setGeometry(QtCore.QRect(110, 450, 650, 60))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")
        self.Photo = QtWidgets.QWidget(HowtoUse_step1)
        self.Photo.setGeometry(QtCore.QRect(210, 120, 430, 300))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"red\";image: url(:/exercise1/ex1.png);")
        self.Photo.setObjectName("Photo")
        self.next = QtWidgets.QPushButton(HowtoUse_step1)
        self.next.setGeometry(QtCore.QRect(450, 510, 130, 40))
        self.next.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.next.setObjectName("next")
        self.logo = QtWidgets.QWidget(HowtoUse_step1)
        self.logo.setGeometry(QtCore.QRect(730, 20, 90, 60))
        self.logo.setStyleSheet("background-color:\"Dodgerblue\";")
        self.logo.setObjectName("logo")
        self.home_button = QtWidgets.QWidget(HowtoUse_step1)
        self.home_button.setGeometry(QtCore.QRect(30, 20, 60, 60))
        self.home_button.setStyleSheet("background-color:\"Dodgerblue\";")
        self.home_button.setObjectName("home_button")
        icon.addPixmap(QtGui.QPixmap(":/icon_heart/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.retranslateUi(HowtoUse_step1)
        QtCore.QMetaObject.connectSlotsByName(HowtoUse_step1)

    def retranslateUi(self, HowtoUse_step1):
        _translate = QtCore.QCoreApplication.translate
        HowtoUse_step1.setWindowTitle(_translate("HowtoUse_step1", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("HowtoUse_step1", "<html><head/><body><p align=\"center\">Step1. 원하는 운동을 선택해주세요</p><p align=\"center\"><br/></p></body></html>"))
        self.next.setText(_translate("HowtoUse_step1", "next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HowtoUse_step1 = QtWidgets.QDialog()
    ui = Ui_HowtoUse_step1()
    ui.setupUi(HowtoUse_step1)
    HowtoUse_step1.show()
    sys.exit(app.exec_())

