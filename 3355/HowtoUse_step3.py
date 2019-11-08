# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HowtoUse_step3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HowtoUse_step3(object):
    def setupUi(self, HowtoUse_step3):
        HowtoUse_step3.setObjectName("selectExercise")
        HowtoUse_step3.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_heart/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HowtoUse_step3.setWindowIcon(icon)
        HowtoUse_step3.setStyleSheet("background-color:\"Aliceblue\";")
        self.selectTitle = QtWidgets.QLabel(HowtoUse_step3)
        self.selectTitle.setGeometry(QtCore.QRect(100, 440, 650, 60))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")
        self.Photo = QtWidgets.QWidget(HowtoUse_step3)
        self.Photo.setGeometry(QtCore.QRect(210, 120, 430, 300))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"Dodgerblue\";image: url(:/exercise1/ex1.png);")
        self.Photo.setObjectName("Photo")
        self.prev = QtWidgets.QPushButton(HowtoUse_step3)
        self.prev.setGeometry(QtCore.QRect(260, 510, 140, 40))
        self.prev.setStyleSheet("background-color:\"red\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.prev.setObjectName("prev")
        self.start = QtWidgets.QPushButton(HowtoUse_step3)
        self.start.setGeometry(QtCore.QRect(450, 510, 130, 40))
        self.start.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.start.setObjectName("start")
        self.logo = QtWidgets.QWidget(HowtoUse_step3)
        self.logo.setGeometry(QtCore.QRect(730, 20, 90, 60))
        self.logo.setStyleSheet("background-color:\"Dodgerblue\";")
        self.logo.setObjectName("logo")
        self.home_button = QtWidgets.QWidget(HowtoUse_step3)
        self.home_button.setGeometry(QtCore.QRect(30, 20, 60, 60))
        self.home_button.setStyleSheet("background-color:\"Dodgerblue\";")
        self.home_button.setObjectName("home_button")

        self.retranslateUi(HowtoUse_step3)
        QtCore.QMetaObject.connectSlotsByName(HowtoUse_step3)

        #self.startButton.clicked.connect(self.start_clicked)  # start_clicked 함수 호출

    # start_clicked 함수 선언 - 메인 페이지에서 운동 선택 페이지로 전환
    #def start_clicked(self):
    #    homePT.close()
    #    selectEx.show()

    def retranslateUi(self, HowtoUse_step3):
        _translate = QtCore.QCoreApplication.translate
        HowtoUse_step3.setWindowTitle(_translate("HowtoUse_step3", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("HowtoUse_step3", "<html><head/><body><p align=\"center\">Step3. 결과 확인</p></body></html>"))
        self.prev.setText(_translate("HowtoUse_step3", "prev"))
        self.start.setText(_translate("HowtoUse_step3", "start"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HowtoUse_step3 = QtWidgets.QDialog()
    ui = Ui_HowtoUse_step3()
    ui.setupUi(HowtoUse_step3)
    HowtoUse_step3.show()
    sys.exit(app.exec_())