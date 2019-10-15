# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_homePT(object):
    def setupUi(self, homePT):
        homePT.setObjectName("homePT")
        homePT.resize(850, 600)
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png')
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        homePT.setWindowIcon(icon)
        homePT.setStyleSheet("background-color:\"Aliceblue\";")
        self.howToUse = QtWidgets.QPushButton(homePT)
        self.howToUse.setGeometry(QtCore.QRect(430, 360, 180, 60))
        self.howToUse.setAutoFillBackground(False)
        self.howToUse.setStyleSheet("background-color:\"slateblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.howToUse.setObjectName("howToUse")
        self.startButton = QtWidgets.QPushButton(homePT)
        self.startButton.setGeometry(QtCore.QRect(230, 360, 180, 60))
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("background-color:\"Royalblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.startButton.setCheckable(False)
        self.startButton.setObjectName("startButton")
        self.label = QtWidgets.QLabel(homePT)
        self.label.setGeometry(QtCore.QRect(230, 120, 380, 300))
        pixmap = QPixmap('logo.png')
        pixmap1 = pixmap.scaled(380, 300, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap1)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.howToUse.raise_()
        self.startButton.raise_()

        self.retranslateUi(homePT)
        QtCore.QMetaObject.connectSlotsByName(homePT)

    def retranslateUi(self, homePT):
        _translate = QtCore.QCoreApplication.translate
        homePT.setWindowTitle(_translate("homePT", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.howToUse.setText(_translate("homePT", "How To Use"))
        self.startButton.setText(_translate("homePT", "START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homePT = QtWidgets.QDialog()
    ui = Ui_homePT()
    ui.setupUi(homePT)
    homePT.show()
    sys.exit(app.exec_())

