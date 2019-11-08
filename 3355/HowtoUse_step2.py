# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HowtoUse_step2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HowtoUse_step2(object):
    def setupUi(self, HowtoUse_step2):
        HowtoUse_step2.setObjectName("selectExercise")
        HowtoUse_step2.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_heart/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HowtoUse_step2.setWindowIcon(icon)
        HowtoUse_step2.setStyleSheet("background-color:\"Aliceblue\";")
        self.selectTitle = QtWidgets.QLabel(HowtoUse_step2)
        self.selectTitle.setGeometry(QtCore.QRect(100, 440, 650, 60))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")
        self.Photo = QtWidgets.QWidget(HowtoUse_step2)
        self.Photo.setGeometry(QtCore.QRect(210, 120, 430, 300))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"Dodgerblue\";image: url(:/exercise1/ex1.png);")
        self.Photo.setObjectName("Photo")
        self.prev = QtWidgets.QPushButton(HowtoUse_step2)
        self.prev.setGeometry(QtCore.QRect(260, 510, 140, 40))
        self.prev.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.prev.setObjectName("exButton1")
        self.next = QtWidgets.QPushButton(HowtoUse_step2)
        self.next.setGeometry(QtCore.QRect(450, 510, 130, 40))
        self.next.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.next.setObjectName("exButton2")
        self.logo = QtWidgets.QWidget(HowtoUse_step2)
        self.logo.setGeometry(QtCore.QRect(730, 20, 90, 60))
        self.logo.setStyleSheet("background-color:\"Dodgerblue\";")
        self.logo.setObjectName("widget")
        self.home_button = QtWidgets.QWidget(HowtoUse_step2)
        self.home_button.setGeometry(QtCore.QRect(30, 20, 60, 60))
        self.home_button.setStyleSheet("background-color:\"black\";")
        self.home_button.setObjectName("home_button")

        self.retranslateUi(HowtoUse_step2)
        QtCore.QMetaObject.connectSlotsByName(HowtoUse_step2)

    def retranslateUi(self, HowtoUse_step2):
        _translate = QtCore.QCoreApplication.translate
        HowtoUse_step2.setWindowTitle(_translate("HowtoUse_step2", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("HowtoUse_step2", "<html><head/><body><p align=\"center\">Step2. 동영상 파일을 불러와 주세요</p></body></html>"))
        self.prev.setText(_translate("HowtoUse_step2", "prev"))
        self.next.setText(_translate("HowtoUse_step2", "next"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HowtoUse_step2 = QtWidgets.QDialog()
    ui = Ui_HowtoUse_step2()
    ui.setupUi(HowtoUse_step2)
    HowtoUse_step2.show()
    sys.exit(app.exec_())

