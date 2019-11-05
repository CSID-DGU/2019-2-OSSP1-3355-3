from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 메인 페이지
class Ui_homePT(object):
    # 메인 페이지 UI setup
    def setupUi(self, homePT):
        homePT.setObjectName("homePT")
        homePT.resize(850, 600)

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png') # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        homePT.setWindowIcon(icon)

        # 스타일시트 - 배경색 설정
        homePT.setStyleSheet("background-color:\"Aliceblue\";")

        # How To Use 버튼
        self.howToUse = QtWidgets.QPushButton(homePT)
        self.howToUse.setGeometry(QtCore.QRect(430, 360, 180, 60)) # 버튼 위치 및 사이즈 설정
        self.howToUse.setAutoFillBackground(False)
        self.howToUse.setStyleSheet("background-color:\"slateblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.howToUse.setObjectName("howToUse")

        # START 버튼
        self.startButton = QtWidgets.QPushButton(homePT)
        self.startButton.setGeometry(QtCore.QRect(230, 360, 180, 60)) # 버튼 위치 및 사이즈 설정
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("background-color:\"Royalblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.startButton.setCheckable(False)
        self.startButton.setObjectName("startButton")

        # 메인 로고 이미지
        self.mainlogo = QtWidgets.QLabel(homePT)
        self.mainlogo.setGeometry(QtCore.QRect(230, 120, 380, 300)) # 위치 및 사이즈 설정
        pixmap = QPixmap('logo.png') # 이미지 삽입
        pixmap1 = pixmap.scaled(380, 300, QtCore.Qt.KeepAspectRatio) # 이미지 사이즈 설정
        self.mainlogo.setPixmap(pixmap1)
        self.mainlogo.setText("")
        self.mainlogo.setObjectName("mainlogo")

        self.mainlogo.raise_()
        self.howToUse.raise_()
        self.startButton.raise_()

        # retranslateUi 함수 호출
        self.retranslateUi(homePT)

        # 버튼 이벤트 - START 버튼 클릭 시
        self.startButton.clicked.connect(self.start_clicked) # start_clicked 함수 호출

    # start_clicked 함수 선언 - 메인 페이지에서 운동 선택 페이지로 전환
    def start_clicked(self):
        homePT.close()
        selectEx.show()

    # retranslateUi 함수 선언
    def retranslateUi(self, homePT):
        _translate = QtCore.QCoreApplication.translate
        homePT.setWindowTitle(_translate("homePT", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.howToUse.setText(_translate("homePT", "How To Use"))
        self.startButton.setText(_translate("homePT", "START"))

# 운동 선택 페이지

class Ui_selectExercise(object):
    # 운동 선택 페이지 UI setup
    def setupUi(self, selectExercise):
        selectExercise.setObjectName("selectExercise")
        selectExercise.resize(850, 600)

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png') # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectExercise.setWindowIcon(icon)

        # 스타일시트 - 배경색 설정
        selectExercise.setStyleSheet("background-color:\"Aliceblue\";")

        # 홈버튼
        icon1 = QtGui.QIcon('homeButton.png')  # 홈버튼 이미지
        self.homeButton = QtWidgets.QPushButton(selectExercise)
        self.homeButton.setGeometry(QtCore.QRect(20, 20, 40, 40))  # 버튼 위치 및 사이즈 설정
        self.homeButton.setIcon(icon1)  # 이미지 설정
        self.homeButton.setIconSize(QtCore.QSize(40, 40))  # 아이콘 사이즈 조정
        self.homeButton.setStyleSheet('QPushButton{border: 0px solid;}')
        # 클릭 시 홈화면으로 이동하도록

        # 타이틀 문구 - 운동 선택 문구
        self.selectTitle = QtWidgets.QLabel(selectExercise)
        self.selectTitle.setGeometry(QtCore.QRect(100, 20, 650, 80)) # 위치 및 사이즈 설정
        self.selectTitle.setStyleSheet("font: 26pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")

        # 운동 1 버튼
        self.exButton1 = QtWidgets.QPushButton(selectExercise)
        self.exButton1.setGeometry(QtCore.QRect(100, 280, 290, 40)) # 버튼 위치 및 사이즈 설정
        self.exButton1.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.exButton1.setObjectName("exButton1")

        # 운동 2 버튼
        self.exButton2 = QtWidgets.QPushButton(selectExercise)
        self.exButton2.setGeometry(QtCore.QRect(450, 280, 290, 40)) # 버튼 위치 및 사이즈 설정
        self.exButton2.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.exButton2.setObjectName("exButton2")

        # 운동 3 버튼
        self.exButton3 = QtWidgets.QPushButton(selectExercise)
        self.exButton3.setGeometry(QtCore.QRect(100, 510, 290, 40))  # 버튼 위치 및 사이즈 설정
        self.exButton3.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.exButton3.setObjectName("exButton3")

        # 운동 4 버튼
        self.exButton4 = QtWidgets.QPushButton(selectExercise)
        self.exButton4.setGeometry(QtCore.QRect(450, 510, 290, 40)) # 버튼 위치 및 사이즈 설정
        self.exButton4.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.exButton4.setObjectName("exButton4")

        # 운동 1 이미지
        self.ex1 = QtWidgets.QLabel(selectExercise)
        self.ex1.setGeometry(QtCore.QRect(100, 100, 290, 172)) # 위치 및 사이즈 설정
        pixex1 = QPixmap('pullup.jpg') # 이미지 삽입
        pixexercise1 = pixex1.scaled(290, 172, QtCore.Qt.KeepAspectRatio) # 이미지 사이즈 설정
        self.ex1.setPixmap(pixexercise1)
        self.ex1.setText("")
        self.ex1.setObjectName("ex1")

        # 운동 2 이미지
        self.ex2 = QtWidgets.QLabel(selectExercise)
        self.ex2.setGeometry(QtCore.QRect(450, 100, 290, 172)) # 위치 및 사이즈 설정
        pixex2 = QPixmap('squat.jpg') # 이미지 삽입
        pixexercise2 = pixex2.scaled(290, 172, QtCore.Qt.KeepAspectRatio) # 이미지 사이즈 설정
        self.ex2.setPixmap(pixexercise2)
        self.ex2.setStyleSheet("background-color: rgb(255, 255, 255);") # 라벨 배경색 설정
        self.ex2.setText("")
        self.ex2.setObjectName("ex2")

        # 운동 3 이미지
        self.ex3 = QtWidgets.QLabel(selectExercise)
        self.ex3.setGeometry(QtCore.QRect(100, 330, 290, 172))  # 위치 및 사이즈 설정
        pixex3 = QPixmap('plank.png')  # 이미지 삽입
        pixexercise3 = pixex3.scaled(290, 172, QtCore.Qt.KeepAspectRatio)  # 이미지 사이즈 설정
        self.ex3.setPixmap(pixexercise3)
        self.ex3.setText("")
        self.ex3.setObjectName("ex3")

        # 운동 4 이미지
        self.ex4 = QtWidgets.QLabel(selectExercise)
        self.ex4.setGeometry(QtCore.QRect(450, 330, 290, 172))  # 위치 및 사이즈 설정
        pixex4 = QPixmap('runge.jpg')  # 이미지 삽입
        pixexercise4 = pixex4.scaled(290, 172, QtCore.Qt.KeepAspectRatio)  # 이미지 사이즈 설정
        self.ex4.setPixmap(pixexercise4)
        self.ex4.setStyleSheet("background-color: rgb(255, 255, 255);")  # 라벨 배경색 설정
        self.ex4.setText("")
        self.ex4.setObjectName("ex4")

        # retranslateUi 함수 호출
        self.retranslateUi(selectExercise)
        QtCore.QMetaObject.connectSlotsByName(selectExercise)

        # 버튼 이벤트 - exButton1 버튼 클릭 시
        self.exButton1.clicked.connect(self.ex1_clicked)  # ex1_clicked 함수 호출

        # ex1_clicked 함수 선언 - 메인 페이지에서 운동 선택 페이지로 전환
    def ex1_clicked(self):
        selectEx.close()
        selectFi.show()

    # retranslateUi 함수 선언
    def retranslateUi(self, selectExercise):
        _translate = QtCore.QCoreApplication.translate
        selectExercise.setWindowTitle(_translate("selectExercise", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("selectExercise", "<html><head/><body><p align=\"center\">원하는 운동을 선택해주세요.</p></body></html>"))
        self.exButton1.setText(_translate("selectExercise", "풀업"))
        self.exButton2.setText(_translate("selectExercise", "스쿼트"))
        self.exButton3.setText(_translate("selectExercise", "플랭크"))
        self.exButton4.setText(_translate("selectExercise", "런지"))

# 파일 선택 페이지
class SelectFile(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(850, 600)
        self.setWindowTitle("HomePT와 함께 하는 올바른 홈트레이닝 라이프")

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png') # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; background-color:\"Aliceblue\";")
        self.textlabel = QLabel()
        self.textlabel.setText("파일을 선택해주세요")
        self.textlabel.setStyleSheet("color:\"black\";font: 16pt\"경기천년제목M Medium\";")
        self.textlabel.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButton = QPushButton("파일 선택")
        self.pushButton.clicked.connect(self.pushButtonClicked)

        self.pushButton.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.textlabel)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])

# main 함수
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # 메인 페이지
    homePT = QtWidgets.QDialog()
    ui = Ui_homePT()
    ui.setupUi(homePT)
    homePT.show()

    # 운동 선택 페이지
    selectEx = QtWidgets.QDialog()
    ui2 = Ui_selectExercise()
    ui2.setupUi(selectEx)

    # 파일 선택 페이지
    selectFi = SelectFile()

    sys.exit(app.exec_())