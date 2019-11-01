# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectExercise.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import realMain


# 운동 선택 페이지
class Ui_selectExercise(object):

    # 운동 선택 페이지 UI setup
    def setupUi(self, selectExercise):
        selectExercise.setObjectName("selectExercise")
        selectExercise.resize(850, 600)

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png')  # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectExercise.setWindowIcon(icon)

        # 스타일시트 - 배경색 설정
        selectExercise.setStyleSheet("background-color:\"Aliceblue\";")

        # 타이틀 문구 - 운동 선택 문구
        self.selectTitle = QtWidgets.QLabel(selectExercise)
        self.selectTitle.setGeometry(QtCore.QRect(100, 50, 650, 80))  # 위치 및 사이즈 설정
        self.selectTitle.setStyleSheet("font: 26pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")

        # 운동 1 버튼
        self.exButton1 = QtWidgets.QPushButton(selectExercise)
        self.exButton1.setGeometry(QtCore.QRect(100, 360, 290, 40))  # 버튼 위치 및 사이즈 설정
        self.exButton1.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.exButton1.setObjectName("exButton1")
        # 운동 2 버튼
        self.exButton2 = QtWidgets.QPushButton(selectExercise)
        self.exButton2.setGeometry(QtCore.QRect(450, 360, 290, 40))  # 버튼 위치 및 사이즈 설정
        self.exButton2.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.exButton2.setObjectName("exButton2")

        # 운동 1 이미지
        self.ex1 = QtWidgets.QLabel(selectExercise)
        self.ex1.setGeometry(QtCore.QRect(100, 170, 290, 172))  # 위치 및 사이즈 설정
        pixex1 = QPixmap('ex1.png')  # 이미지 삽입
        pixexercise1 = pixex1.scaled(290, 172, QtCore.Qt.KeepAspectRatio)  # 이미지 사이즈 설정
        self.ex1.setPixmap(pixexercise1)
        self.ex1.setText("")
        self.ex1.setObjectName("ex1")
        # 운동 2 이미지
        self.ex2 = QtWidgets.QLabel(selectExercise)
        self.ex2.setGeometry(QtCore.QRect(450, 170, 290, 172))  # 위치 및 사이즈 설정
        pixex2 = QPixmap('ex2.jpg')  # 이미지 삽입
        pixexercise2 = pixex2.scaled(290, 172, QtCore.Qt.KeepAspectRatio)  # 이미지 사이즈 설정
        self.ex2.setPixmap(pixexercise2)
        self.ex2.setStyleSheet("background-color: rgb(255, 255, 255);")  # 라벨 배경색 설정
        self.ex2.setText("")
        self.ex2.setObjectName("ex2")

        # retranslateUi 함수 호출
        self.retranslateUi(selectExercise)
        QtCore.QMetaObject.connectSlotsByName(selectExercise)

        # 버튼 이벤트 - exButton1 버튼 클릭 시
        self.exButton1.clicked.connect(self.ex1_clicked)  # ex1_clicked 함수 호출

        # ex1_clicked 함수 선언 - 메인 페이지에서 운동 선택 페이지로 전환

    def ex1_clicked(self):
        realMain.window.show()

    # retranslateUi 함수 선언
    def retranslateUi(self, selectExercise):
        _translate = QtCore.QCoreApplication.translate
        selectExercise.setWindowTitle(_translate("selectExercise", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(
            _translate("selectExercise", "<html><head/><body><p align=\"center\">원하는 운동을 선택해주세요.</p></body></html>"))
        self.exButton1.setText(_translate("selectExercise", "플랭크"))
        self.exButton2.setText(_translate("selectExercise", "스쿼트"))
