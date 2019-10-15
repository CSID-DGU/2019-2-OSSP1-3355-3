# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectExercise.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_selectExercise(object):
    def setupUi(self, selectExercise):
        selectExercise.setObjectName("selectExercise")
        selectExercise.resize(850, 600)
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png')
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectExercise.setWindowIcon(icon)
        selectExercise.setStyleSheet("background-color:\"Aliceblue\";")
        self.selectTitle = QtWidgets.QLabel(selectExercise)
        self.selectTitle.setGeometry(QtCore.QRect(100, 50, 650, 80))
        self.selectTitle.setStyleSheet("font: 26pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")
        self.exButton1 = QtWidgets.QPushButton(selectExercise)
        self.exButton1.setGeometry(QtCore.QRect(100, 360, 290, 40))
        self.exButton1.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.exButton1.setObjectName("exButton1")
        self.exButton2 = QtWidgets.QPushButton(selectExercise)
        self.exButton2.setGeometry(QtCore.QRect(450, 360, 290, 40))
        self.exButton2.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.exButton2.setObjectName("exButton2")
        self.ex1 = QtWidgets.QLabel(selectExercise)
        self.ex1.setGeometry(QtCore.QRect(100, 170, 290, 172))
        pixex1 = QPixmap('ex1.png')
        pixexercise1 = pixex1.scaled(290, 172, QtCore.Qt.KeepAspectRatio)
        self.ex1.setPixmap(pixexercise1)
        self.ex1.setText("")
        self.ex1.setObjectName("ex1")
        self.ex2 = QtWidgets.QLabel(selectExercise)
        self.ex2.setGeometry(QtCore.QRect(450, 170, 290, 172))
        pixex2 = QPixmap('ex2.jpg')
        pixexercise2 = pixex2.scaled(290, 172, QtCore.Qt.KeepAspectRatio)
        self.ex2.setPixmap(pixexercise2)
        self.ex2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ex2.setText("")
        self.ex2.setObjectName("ex2")

        self.retranslateUi(selectExercise)
        QtCore.QMetaObject.connectSlotsByName(selectExercise)

    def retranslateUi(self, selectExercise):
        _translate = QtCore.QCoreApplication.translate
        selectExercise.setWindowTitle(_translate("selectExercise", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("selectExercise", "<html><head/><body><p align=\"center\">원하는 운동을 선택해주세요.</p></body></html>"))
        self.exButton1.setText(_translate("selectExercise", "플랭크"))
        self.exButton2.setText(_translate("selectExercise", "스쿼트"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectExercise = QtWidgets.QDialog()
    ui = Ui_selectExercise()
    ui.setupUi(selectExercise)
    selectExercise.show()
    sys.exit(app.exec_())

