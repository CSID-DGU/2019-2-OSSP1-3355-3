
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 메인 페이지
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
        self.mainlogo = QtWidgets.QLabel(homePT)
        self.mainlogo.setGeometry(QtCore.QRect(230, 120, 380, 300))
        pixmap = QPixmap('logo.png')
        pixmap1 = pixmap.scaled(380, 300, QtCore.Qt.KeepAspectRatio)
        self.mainlogo.setPixmap(pixmap1)
        self.mainlogo.setText("")
        self.mainlogo.setObjectName("label")
        self.mainlogo.raise_()
        self.howToUse.raise_()
        self.startButton.raise_()

        self.retranslateUi(homePT)
        QtCore.QMetaObject.connectSlotsByName(homePT)
        homePT2 = QtWidgets.QDialog()
        ui2 = Ui_selectExercise()

        self.startButton.clicked.connect(self.start_clicked)

    def start_clicked(self):
        #메인 화면 닫고 운동 선택 화면
        homePT.close()
        selectEx.show()

    def retranslateUi(self, homePT):
        _translate = QtCore.QCoreApplication.translate
        homePT.setWindowTitle(_translate("homePT", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.howToUse.setText(_translate("homePT", "How To Use"))
        self.startButton.setText(_translate("homePT", "START"))

# 운동 선택 페이지
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

    # 메인 페이지
    homePT = QtWidgets.QDialog()
    ui = Ui_homePT()
    ui.setupUi(homePT)
    homePT.show()
    #운동 선택 창
    selectEx = QtWidgets.QDialog()
    ui2 = Ui_selectExercise()
    ui2.setupUi(selectEx)


    sys.exit(app.exec_())

