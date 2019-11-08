# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HowtoUse_step1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectExercise(object):
    def setupUi(self, selectExercise):
        selectExercise.setObjectName("selectExercise")
        selectExercise.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_heart/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectExercise.setWindowIcon(icon)
        selectExercise.setStyleSheet("background-color:\"Aliceblue\";")
        self.selectTitle = QtWidgets.QLabel(selectExercise)
        self.selectTitle.setGeometry(QtCore.QRect(110, 450, 650, 61))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")
        self.Photo = QtWidgets.QWidget(selectExercise)
        self.Photo.setGeometry(QtCore.QRect(210, 120, 431, 301))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"Dodgerblue\";image: url(:/exercise1/ex1.png);")
        self.Photo.setObjectName("Photo")
        self.exButton2 = QtWidgets.QPushButton(selectExercise)
        self.exButton2.setGeometry(QtCore.QRect(450, 510, 131, 40))
        self.exButton2.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.exButton2.setObjectName("exButton2")
        self.widget = QtWidgets.QWidget(selectExercise)
        self.widget.setGeometry(QtCore.QRect(730, 20, 91, 61))
        self.widget.setStyleSheet("background-color:\"Dodgerblue\";")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(selectExercise)
        self.widget_2.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.widget_2.setStyleSheet("background-color:\"Dodgerblue\";")
        self.widget_2.setObjectName("widget_2")

        self.retranslateUi(selectExercise)
        QtCore.QMetaObject.connectSlotsByName(selectExercise)

    def retranslateUi(self, selectExercise):
        _translate = QtCore.QCoreApplication.translate
        selectExercise.setWindowTitle(_translate("selectExercise", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("selectExercise", "<html><head/><body><p align=\"center\">Step1. 원하는 운동을 선택해주세요</p><p align=\"center\"><br/></p></body></html>"))
        self.exButton2.setText(_translate("selectExercise", "next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectExercise = QtWidgets.QDialog()
    ui = Ui_selectExercise()
    ui.setupUi(selectExercise)
    selectExercise.show()
    sys.exit(app.exec_())

