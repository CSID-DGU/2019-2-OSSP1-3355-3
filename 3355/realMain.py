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
        #homePT.setStyleSheet("background-image: url('hometraining3.jpg')")

        # How To Use 버튼
        self.howToUse = QtWidgets.QPushButton(homePT)
        self.howToUse.setGeometry(QtCore.QRect(430, 360, 180, 60)) # 버튼 위치 및 사이즈 설정
        self.howToUse.setAutoFillBackground(False)
        self.howToUse.setStyleSheet("background-color:\"Slateblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
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

        # 버튼 이벤트 - howToUse 버튼 클릭 시
        self.howToUse.clicked.connect(self.how_clicked)  # start_clicked 함수 호출

    # start_clicked 함수 선언 - 메인 페이지에서 운동 선택 페이지로 전환
    def start_clicked(self):
        homePT.close()
        selectEx.show()

    # howToUse 함수 선언 - 안내 페이지로 전환
    def how_clicked(self):
        homePT.close()
        how1.show()

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
        icon1 = QtGui.QIcon('homebutton.png')  # 홈버튼 이미지
        self.homeButton = QtWidgets.QPushButton(selectExercise)
        self.homeButton.setGeometry(QtCore.QRect(790, 20, 40, 40))  # 버튼 위치 및 사이즈 설정
        self.homeButton.setIcon(icon1)  # 이미지 설정
        self.homeButton.setIconSize(QtCore.QSize(40, 40))  # 아이콘 사이즈 조정
        self.homeButton.setStyleSheet('QPushButton{border: 0px solid;}')
        # 클릭 시 홈화면으로 이동하도록

        # 이전버튼
        icon2 = QtGui.QIcon('backButton.png')  # 홈버튼 이미지
        self.backButton = QtWidgets.QPushButton(selectExercise)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 40, 40))  # 버튼 위치 및 사이즈 설정
        self.backButton.setIcon(icon2)  # 이미지 설정
        self.backButton.setIconSize(QtCore.QSize(40, 40))  # 아이콘 사이즈 조정
        self.backButton.setStyleSheet('QPushButton{border: 0px solid;}')
        # 클릭 시 이전화면으로 이동하도록

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

        # 버튼 이벤트 - 홈 버튼 클릭 시
        self.homeButton.clicked.connect(self.home_clicked)

        # 버튼 이벤트 - 백 버튼 클릭 시
        self.backButton.clicked.connect(self.back_clicked)

        # 버튼 이벤트 - exButton1 버튼 클릭 시
        self.exButton1.clicked.connect(self.ex_clicked)  # ex_clicked 함수 호출

        # 버튼 이벤트 - exButton2 버튼 클릭 시
        self.exButton2.clicked.connect(self.ex_clicked)  # ex_clicked 함수 호출

        # 버튼 이벤트 - exButton3 버튼 클릭 시
        self.exButton3.clicked.connect(self.ex_clicked)  # ex_clicked 함수 호출

        # 버튼 이벤트 - exButton4 버튼 클릭 시
        self.exButton4.clicked.connect(self.ex_clicked)  # ex_clicked 함수 호출

        # home_clicked 함수 선언 - 메인 페이지로 돌아감
    def home_clicked(self):
        selectEx.close()
        homePT.show()

        # back_clicked 함수 선언 - 이전 페이지로 돌아감
    def back_clicked(self):
        selectEx.close()
        homePT.show()

        # ex_clicked 함수 선언 - 메인 페이지에서 운동 선택 페이지로 전환
    def ex_clicked(self):
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

        # 홈버튼
        icon1 = QtGui.QIcon('homeButton.png')  # 홈버튼 이미지
        self.homeButton = QtWidgets.QPushButton(self)
        self.homeButton.setGeometry(QtCore.QRect(790, 20, 40, 40))  # 버튼 위치 및 사이즈 설정
        self.homeButton.setIcon(icon1)  # 이미지 설정
        self.homeButton.setIconSize(QtCore.QSize(40, 40))  # 아이콘 사이즈 조정
        self.homeButton.setStyleSheet('QPushButton{border: 0px solid;}')
        # 클릭 시 홈화면으로 이동하도록

        # 이전버튼
        icon2 = QtGui.QIcon('backButton.png')  # 홈버튼 이미지
        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 40, 40))  # 버튼 위치 및 사이즈 설정
        self.backButton.setIcon(icon2)  # 이미지 설정
        self.backButton.setIconSize(QtCore.QSize(40, 40))  # 아이콘 사이즈 조정
        self.backButton.setStyleSheet('QPushButton{border: 0px solid;}')
        # 클릭 시 이전화면으로 이동하도록

        # 스타일시트
        self.setStyleSheet("font: 24pt\"경기천년제목M Medium\"; background-color:\"Aliceblue\";")

        # 파일 선택 문구
        self.textlabel = QtWidgets.QLabel(self)
        self.textlabel.setText("파일을 선택해주세요")
        self.textlabel.setGeometry(QtCore.QRect(220, 200, 420, 50))
        self.textlabel.setStyleSheet("color:\"black\";font: 30pt\"경기천년제목M Medium\";")
        self.textlabel.setAlignment(QtCore.Qt.AlignCenter)

        # 파일 선택 버튼
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(340, 330, 160, 40))  # 버튼 위치 및 사이즈 설정
        self.pushButton.setText("파일 선택")
        self.pushButton.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")

        # 선택된 파일 위치
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 500, 700, 50))
        self.label.setStyleSheet("color:\"black\";font: 12pt\"경기천년제목M Medium\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # 버튼 이벤트 - 홈 버튼 클릭 시
        self.homeButton.clicked.connect(self.home_clicked)

        # 버튼 이벤트 - 백 버튼 클릭 시
        self.backButton.clicked.connect(self.back_clicked)

        # 버튼 이벤트 - 파일 선택 클릭 시
        self.pushButton.clicked.connect(self.pushButtonClicked)

        # home_clicked 함수 선언 - 메인 페이지로 돌아감
    def home_clicked(self):
        selectFi.close()
        homePT.show()

        # back_clicked 함수 선언 - 이전 페이지로 돌아감
    def back_clicked(self):
        selectFi.close()
        selectEx.show()

    # 파일 선택 버튼 클릭 시 수행되는 함수
    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])

# How to Use step 1 페이지
class HowtoUse_step1(object):
    def setupUi(self, HowtoUse):

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png')  # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HowtoUse.setWindowIcon(icon)

        HowtoUse.setObjectName("selectExercise")
        HowtoUse.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_heart/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HowtoUse.setWindowIcon(icon)
        HowtoUse.setStyleSheet("background-color:\"Aliceblue\";")
        self.selectTitle = QtWidgets.QLabel(HowtoUse)
        self.selectTitle.setGeometry(QtCore.QRect(110, 450, 650, 61))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")
        self.Photo = QtWidgets.QWidget(HowtoUse)
        self.Photo.setGeometry(QtCore.QRect(210, 120, 431, 301))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"Dodgerblue\";image: url(:/exercise1/ex1.png);")
        self.Photo.setObjectName("Photo")
        self.nextButton = QtWidgets.QPushButton(HowtoUse)
        self.nextButton.setGeometry(QtCore.QRect(450, 510, 131, 40))
        self.nextButton.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.nextButton.setObjectName("exButton2")
        self.widget = QtWidgets.QWidget(HowtoUse)
        self.widget.setGeometry(QtCore.QRect(730, 20, 91, 61))
        self.widget.setStyleSheet("background-color:\"Dodgerblue\";")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(HowtoUse)
        self.widget_2.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.widget_2.setStyleSheet("background-color:\"Dodgerblue\";")
        self.widget_2.setObjectName("widget_2")

        self.retranslateUi(HowtoUse)
        QtCore.QMetaObject.connectSlotsByName(HowtoUse)

        self.nextButton.clicked.connect(self.next_clicked)

    def next_clicked(self):
        how1.close()
        how2.show()

    def retranslateUi(self, HowtoUse):
        _translate = QtCore.QCoreApplication.translate
        HowtoUse.setWindowTitle(_translate("selectExercise", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("selectExercise", "<html><head/><body><p align=\"center\">Step1. 원하는 운동을 선택해주세요</p><p align=\"center\"><br/></p></body></html>"))
        self.nextButton.setText(_translate("selectExercise", "next"))

# How to Use step 2 페이지
class HowtoUse_step2(object):
    def setupUi(self, HowtoUse):

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png')  # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        how2.setWindowIcon(icon)

        HowtoUse.setObjectName("selectExercise")
        HowtoUse.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_heart/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HowtoUse.setWindowIcon(icon)
        HowtoUse.setStyleSheet("background-color:\"Aliceblue\";")
        self.selectTitle = QtWidgets.QLabel(HowtoUse)
        self.selectTitle.setGeometry(QtCore.QRect(100, 440, 650, 61))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")
        self.Photo = QtWidgets.QWidget(HowtoUse)
        self.Photo.setGeometry(QtCore.QRect(210, 120, 431, 301))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"Dodgerblue\";image: url(:/exercise1/ex1.png);")
        self.Photo.setObjectName("Photo")
        self.preButton = QtWidgets.QPushButton(HowtoUse)
        self.preButton.setGeometry(QtCore.QRect(260, 510, 141, 40))
        self.preButton.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.preButton.setObjectName("exButton1")
        self.nextButton = QtWidgets.QPushButton(HowtoUse)
        self.nextButton.setGeometry(QtCore.QRect(450, 510, 131, 40))
        self.nextButton.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.nextButton.setObjectName("exButton2")
        self.widget = QtWidgets.QWidget(HowtoUse)
        self.widget.setGeometry(QtCore.QRect(730, 20, 91, 61))
        self.widget.setStyleSheet("background-color:\"Dodgerblue\";")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(HowtoUse)
        self.widget_2.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.widget_2.setStyleSheet("background-color:\"Dodgerblue\";")
        self.widget_2.setObjectName("widget_2")

        self.retranslateUi(HowtoUse)
        QtCore.QMetaObject.connectSlotsByName(HowtoUse)

        self.nextButton.clicked.connect(self.next_clicked)
        self.preButton.clicked.connect(self.pre_clicked)

    def next_clicked(self):
        how2.close()
        how3.show()

    def pre_clicked(self):
        how2.close()
        how1.show()

    def retranslateUi(self, HowtoUse):
        _translate = QtCore.QCoreApplication.translate
        HowtoUse.setWindowTitle(_translate("selectExercise", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("selectExercise",
                                                "<html><head/><body><p align=\"center\">Step2. 동영상 파일을 불러와 주세요</p></body></html>"))
        self.preButton.setText(_translate("selectExercise", "prev"))
        self.nextButton.setText(_translate("selectExercise", "next"))

# How to Use step 3 페이지
class HowtoUse_step3(object):
    def setupUi(self, HowtoUse):

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png')  # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        how3.setWindowIcon(icon)

        HowtoUse.setObjectName("selectExercise")
        HowtoUse.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_heart/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HowtoUse.setWindowIcon(icon)
        HowtoUse.setStyleSheet("background-color:\"Aliceblue\";")
        self.selectTitle = QtWidgets.QLabel(HowtoUse)
        self.selectTitle.setGeometry(QtCore.QRect(100, 440, 650, 61))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")
        self.Photo = QtWidgets.QWidget(HowtoUse)
        self.Photo.setGeometry(QtCore.QRect(210, 120, 431, 301))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"Dodgerblue\";image: url(:/exercise1/ex1.png);")
        self.Photo.setObjectName("Photo")
        self.preButton = QtWidgets.QPushButton(HowtoUse)
        self.preButton.setGeometry(QtCore.QRect(260, 510, 141, 40))
        self.preButton.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.preButton.setObjectName("exButton1")
        self.nextButton = QtWidgets.QPushButton(HowtoUse)
        self.nextButton.setGeometry(QtCore.QRect(450, 510, 131, 40))
        self.nextButton.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.nextButton.setObjectName("exButton2")
        self.widget = QtWidgets.QWidget(HowtoUse)
        self.widget.setGeometry(QtCore.QRect(730, 20, 91, 61))
        self.widget.setStyleSheet("background-color:\"Dodgerblue\";")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(HowtoUse)
        self.widget_2.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.widget_2.setStyleSheet("background-color:\"Dodgerblue\";")
        self.widget_2.setObjectName("widget_2")

        self.retranslateUi(HowtoUse)
        QtCore.QMetaObject.connectSlotsByName(HowtoUse)

        self.nextButton.clicked.connect(self.next_clicked)
        self.preButton.clicked.connect(self.pre_clicked)

    def next_clicked(self):
        how3.close()
        homePT.show()

    def pre_clicked(self):
        how3.close()
        how2.show()

    def retranslateUi(self, HowtoUse):
        _translate = QtCore.QCoreApplication.translate
        HowtoUse.setWindowTitle(_translate("selectExercise", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("selectExercise", "<html><head/><body><p align=\"center\">Step3. 결과 확인</p></body></html>"))
        self.preButton.setText(_translate("selectExercise", "prev"))
        self.nextButton.setText(_translate("selectExercise", "start"))

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

    # how to use 페이지
    how1 = QtWidgets.QDialog()
    ui3 = HowtoUse_step1()
    ui3.setupUi(how1)
    how2 = QtWidgets.QDialog()
    ui4 = HowtoUse_step2()
    ui4.setupUi(how2)
    how3 = QtWidgets.QDialog()
    ui5 = HowtoUse_step3()
    ui5.setupUi(how3)

    sys.exit(app.exec_())
