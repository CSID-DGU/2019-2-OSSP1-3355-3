# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_homePT(object):
    def setupUi(self, homePT):
        homePT.setObjectName("homePT")
        homePT.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../Users/오유민/Pictures/Saved Pictures/hart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        homePT.setWindowIcon(icon)
        homePT.setStyleSheet("background-color:\"lemonchiffon\";")
        self.purposePhrases = QtWidgets.QLabel(homePT)
        self.purposePhrases.setGeometry(QtCore.QRect(80, 130, 700, 140))
        self.purposePhrases.setAutoFillBackground(False)
        self.purposePhrases.setStyleSheet("font: 26pt\"경기천년제목M Medium\"; color:\"black\";")
        self.purposePhrases.setObjectName("purposePhrases")
        self.howToUse = QtWidgets.QPushButton(homePT)
        self.howToUse.setGeometry(QtCore.QRect(240, 350, 180, 60))
        self.howToUse.setAutoFillBackground(False)
        self.howToUse.setStyleSheet("background-color:\"orange\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.howToUse.setObjectName("howToUse")
        self.startButton = QtWidgets.QPushButton(homePT)
        self.startButton.setGeometry(QtCore.QRect(440, 350, 180, 60))
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("background-color:\"Tomato\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.startButton.setObjectName("startButton")

        self.retranslateUi(homePT)
        QtCore.QMetaObject.connectSlotsByName(homePT)

    def retranslateUi(self, homePT):
        _translate = QtCore.QCoreApplication.translate
        homePT.setWindowTitle(_translate("homePT", "홈PT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.purposePhrases.setText(_translate("homePT", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">홈PT와 올바른 홈트레이닝 라이프를 함께 해요!</span></p></body></html>"))
        self.howToUse.setText(_translate("homePT", "How To Use"))
        self.startButton.setText(_translate("homePT", "START"))
    def bfunc(self):
        print("btclicked")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homePT = QtWidgets.QDialog()
    ui = Ui_homePT()
    ui.setupUi(homePT)
    homePT.show()
    sys.exit(app.exec_())