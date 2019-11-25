from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import test_plank

global filename

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
        homePT.setStyleSheet("QWidget#homePT {border-image: url(trainingimage.jpg) 0 0 0 0 stretch stretch;}")

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
        how.show()

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
        icon1 = QtGui.QIcon('home.png')  # 홈버튼 이미지
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
        self.selectTitle.setGeometry(QtCore.QRect(100, 10, 650, 80)) # 위치 및 사이즈 설정
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
        self.exButton1.clicked.connect(self.ex1_clicked)  # ex_clicked 함수 호출

        # 버튼 이벤트 - exButton2 버튼 클릭 시
        self.exButton2.clicked.connect(self.ex2_clicked)  # ex_clicked 함수 호출

        # 버튼 이벤트 - exButton3 버튼 클릭 시
        self.exButton3.clicked.connect(self.ex3_clicked)  # ex_clicked 함수 호출

        # 버튼 이벤트 - exButton4 버튼 클릭 시
        self.exButton4.clicked.connect(self.ex4_clicked)  # ex_clicked 함수 호출

    # home_clicked 함수 선언 - 메인 페이지로 돌아감
    def home_clicked(self):
        selectEx.close()
        homePT.show()

    # back_clicked 함수 선언 - 이전 페이지로 돌아감
    def back_clicked(self):
        selectEx.close()
        homePT.show()

    # ex1_clicked 함수 선언 - 풀업 선택 페이지로 전환
    def ex1_clicked(self):
        selectFi.textlabel.setText("풀업 운동 영상을 선택해주세요") # 문구 출력
        selectFi.pixex = QPixmap("pullup.jpg") # 이미지 출력
        selectFi.pixexercise = selectFi.pixex.scaled(500, 300, QtCore.Qt.KeepAspectRatio)  # 이미지 사이즈 설정
        selectFi.ex.setPixmap(selectFi.pixexercise)
        selectEx.close()
        selectFi.show()

    # ex2_clicked 함수 선언 - 스쿼트 파일 선택 페이지로 전환
    def ex2_clicked(self):
        selectFi.textlabel.setText("스쿼트 운동 영상을 선택해주세요") # 문구 출력
        selectFi.pixex = QPixmap("squat.jpg")  # 이미지 출력
        selectFi.pixexercise = selectFi.pixex.scaled(500, 300, QtCore.Qt.KeepAspectRatio)  # 이미지 사이즈 설정
        selectFi.ex.setPixmap(selectFi.pixexercise)
        selectEx.close()
        selectFi.show()

    # ex3_clicked 함수 선언 - 플랭크 파일 선택 페이지로 전환
    def ex3_clicked(self):
        selectFi.textlabel.setText("플랭크 운동 영상을 선택해주세요") # 문구 출력
        selectFi.pixex = QPixmap("plank.png")  # 이미지 출력
        selectFi.pixexercise = selectFi.pixex.scaled(500, 300, QtCore.Qt.KeepAspectRatio)  # 이미지 사이즈 설정
        selectFi.ex.setPixmap(selectFi.pixexercise)
        selectEx.close()
        selectFi.show()

    # ex4_clicked 함수 선언 - 런지 파일 선택 페이지로 전환
    def ex4_clicked(self):
        selectFi.textlabel.setText("런지 운동 영상을 선택해주세요") # 문구 출력
        selectFi.pixex = QPixmap("runge.jpg")  # 이미지 출력
        selectFi.pixexercise = selectFi.pixex.scaled(500, 300, QtCore.Qt.KeepAspectRatio)  # 이미지 사이즈 설정
        selectFi.ex.setPixmap(selectFi.pixexercise)
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

# 운동 파일 선택 페이지
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
        icon1 = QtGui.QIcon('home.png')  # 홈버튼 이미지
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
        self.textlabel.setText("운동 영상을 선택해주세요.")
        self.textlabel.setGeometry(QtCore.QRect(140, 60, 600, 50))
        self.textlabel.setStyleSheet("color:\"black\";font: 26pt\"경기천년제목M Medium\";")
        self.textlabel.setAlignment(QtCore.Qt.AlignCenter)

        # 운동 이미지
        self.ex = QtWidgets.QLabel(self)
        self.ex.setGeometry(QtCore.QRect(190, 130, 500, 300))  # 위치 및 사이즈 설정

        self.ex.setText("")
        self.ex.setObjectName("ex")

        # 파일 선택 버튼
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(215, 450, 440, 40))  # 버튼 위치 및 사이즈 설정
        self.pushButton.setText("동영상 파일 불러오기")
        self.pushButton.setStyleSheet("background-color:\"Dodgerblue\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")

        # 버튼 이벤트 - 홈 버튼 클릭 시
        self.homeButton.clicked.connect(self.home_clicked)

        # 버튼 이벤트 - 백 버튼 클릭 시
        self.backButton.clicked.connect(self.back_clicked)

        # 버튼 이벤트 - 파일 선택 클릭 시
        self.pushButton.clicked.connect(self.pushButtonClicked)

    # home_clicked 함수 선언 - 메인 페이지로 돌아감
    def home_clicked(self):
        self.label.setText("") # 파일명 초기화
        selectFi.close()
        homePT.show()

    # back_clicked 함수 선언 - 이전 페이지로 돌아감
    def back_clicked(self):
        self.label.setText("") # 파일명 초기화
        selectFi.close()
        selectEx.show()

    # pushButtonClicked 함수 선언 - 파일 불러오기 창 띄우기
    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "", "Video File(*.avi, *.mp4)")
        filename = fname[0]
        if filename:            # videoToframe.py로 변수 전달
            print(filename)

        else:
            QMessageBox.about(self, "Warning", "파일을 선택하지 않았습니다.")

# How to Use(전체 설명) 페이지
class HowtoUse(object):
    def setupUi(self, how):

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png')  # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        how.setWindowIcon(icon)

        # 창 설정
        how.setObjectName("how")
        how.resize(850, 600)
        how.setStyleSheet("background-color:\"Lavender\";")

        # 홈버튼
        icon1 = QtGui.QIcon('homebutton.png')  # 홈버튼 이미지
        self.homeButton = QtWidgets.QPushButton(how)
        self.homeButton.setGeometry(QtCore.QRect(790, 20, 40, 40))  # 버튼 위치 및 사이즈 설정
        self.homeButton.setIcon(icon1)  # 이미지 설정
        self.homeButton.setIconSize(QtCore.QSize(40, 40))  # 아이콘 사이즈 조정
        self.homeButton.setStyleSheet('QPushButton{border: 0px solid;}')
        # 클릭 시 홈화면으로 이동하도록

        # 이미지
        self.Photo = QtWidgets.QWidget(how)
        self.Photo.setGeometry(QtCore.QRect(150, 90, 550, 408))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"Lavender\";image: url(guide.png);")
        self.Photo.setObjectName("Photo")

        # 문구
        self.selectTitle = QtWidgets.QLabel(how)
        self.selectTitle.setGeometry(QtCore.QRect(90, 20, 670, 60))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")

        # 이전 버튼
        self.preButton = QtWidgets.QPushButton(how)
        self.preButton.setGeometry(QtCore.QRect(220, 510, 200, 40))
        self.preButton.setStyleSheet("background-color:\"Orchid\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.preButton.setObjectName("preButton")

        # 다음 버튼
        self.nextButton = QtWidgets.QPushButton(how)
        self.nextButton.setGeometry(QtCore.QRect(430, 510, 200, 40))
        self.nextButton.setStyleSheet("background-color:\"Orchid\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.nextButton.setObjectName("nextButton")

        self.retranslateUi(how)
        QtCore.QMetaObject.connectSlotsByName(how)

        # 버튼 이벤트 - 홈 버튼 클릭 시
        self.homeButton.clicked.connect(self.home_clicked)

        # 버튼 이벤트 - 다음 버튼 클릭 시
        self.nextButton.clicked.connect(self.next_clicked)

        # 버튼 이벤트 - 이전 버튼 클릭 시
        self.preButton.clicked.connect(self.pre_clicked)

    # home_clicked 함수 선언 - 메인 페이지로 돌아감
    def home_clicked(self):
        how.close()
        homePT.show()

    # next_clicked 함수 선언 - 다음 페이지로 넘어감
    def next_clicked(self):
        how.close()
        how1.show()

    # pre_clicked 함수 선언 - 이전 페이지로 돌아감
    def pre_clicked(self):
        how.close()
        homePT.show()

    def retranslateUi(self, how):
        _translate = QtCore.QCoreApplication.translate
        how.setWindowTitle(_translate("how", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("how", "<html><head/><body><p align=\"center\">혼자서도 운동 자세를 교정할 수 있는 프로그램</p></body></html>"))
        self.preButton.setText(_translate("how", "prev"))
        self.nextButton.setText(_translate("how", "How to Use"))


# How to Use step 1 페이지
class HowtoUse_step1(object):
    def setupUi(self, how1):

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png')  # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        how1.setWindowIcon(icon)

        # 창 설정
        how1.setObjectName("how1")
        how1.resize(850, 600)
        how1.setStyleSheet("background-color:\"Lavender\";")

        # 홈버튼
        icon1 = QtGui.QIcon('home.png')  # 홈버튼 이미지
        self.homeButton = QtWidgets.QPushButton(how1)
        self.homeButton.setGeometry(QtCore.QRect(790, 20, 40, 40))  # 버튼 위치 및 사이즈 설정
        self.homeButton.setIcon(icon1)  # 이미지 설정
        self.homeButton.setIconSize(QtCore.QSize(40, 40))  # 아이콘 사이즈 조정
        self.homeButton.setStyleSheet('QPushButton{border: 0px solid;}')
        # 클릭 시 홈화면으로 이동하도록

        # step 1 이미지
        self.Photo = QtWidgets.QWidget(how1)
        self.Photo.setGeometry(QtCore.QRect(150, 30, 550, 408))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"white\";image: url(step1image.jpg);")
        self.Photo.setObjectName("Photo")

        # step 1 문구
        self.selectTitle = QtWidgets.QLabel(how1)
        self.selectTitle.setGeometry(QtCore.QRect(150, 445, 550, 60))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")

        # 이전 버튼
        self.preButton = QtWidgets.QPushButton(how1)
        self.preButton.setGeometry(QtCore.QRect(220, 510, 200, 40))
        self.preButton.setStyleSheet("background-color:\"Orchid\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.preButton.setObjectName("preButton")

        # 다음 버튼
        self.nextButton = QtWidgets.QPushButton(how1)
        self.nextButton.setGeometry(QtCore.QRect(430, 510, 200, 40))
        self.nextButton.setStyleSheet("background-color:\"Orchid\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.nextButton.setObjectName("nextButton")

        self.retranslateUi(how1)
        QtCore.QMetaObject.connectSlotsByName(how1)

        # 버튼 이벤트 - 홈 버튼 클릭 시
        self.homeButton.clicked.connect(self.home_clicked)

        # 버튼 이벤트 - 다음 버튼 클릭 시
        self.nextButton.clicked.connect(self.next_clicked)

        # 버튼 이벤트 - 이전 버튼 클릭 시
        self.preButton.clicked.connect(self.pre_clicked)

    # home_clicked 함수 선언 - 메인 페이지로 돌아감
    def home_clicked(self):
        how1.close()
        homePT.show()

    # next_clicked 함수 선언 - 다음 페이지로 넘어감
    def next_clicked(self):
        how1.close()
        how2.show()

    # pre_clicked 함수 선언 - 이전 페이지로 돌아감
    def pre_clicked(self):
        how1.close()
        how.show()

    def retranslateUi(self, how1):
        _translate = QtCore.QCoreApplication.translate
        how1.setWindowTitle(_translate("how1", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("how1", "<html><head/><body><p align=\"center\">Step1. 원하는 운동을 선택해주세요.</p></body></html>"))
        self.preButton.setText(_translate("how1", "prev"))
        self.nextButton.setText(_translate("how1", "next"))

# How to Use step 2 페이지
class HowtoUse_step2(object):
    def setupUi(self, how2):

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png')  # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        how2.setWindowIcon(icon)

        # 창 설정
        how2.setObjectName("how2")
        how2.resize(850, 600)
        how2.setStyleSheet("background-color:\"Lavender\";")

        # 홈버튼
        icon1 = QtGui.QIcon('home.png')  # 홈버튼 이미지
        self.homeButton = QtWidgets.QPushButton(how2)
        self.homeButton.setGeometry(QtCore.QRect(790, 20, 40, 40))  # 버튼 위치 및 사이즈 설정
        self.homeButton.setIcon(icon1)  # 이미지 설정
        self.homeButton.setIconSize(QtCore.QSize(40, 40))  # 아이콘 사이즈 조정
        self.homeButton.setStyleSheet('QPushButton{border: 0px solid;}')
        # 클릭 시 홈화면으로 이동하도록

        # step 2 이미지
        self.Photo = QtWidgets.QWidget(how2)
        self.Photo.setGeometry(QtCore.QRect(150, 30, 550, 408))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"white\";image: url(step2image.jpg);")
        self.Photo.setObjectName("Photo")

        # step 2 문구
        self.selectTitle = QtWidgets.QLabel(how2)
        self.selectTitle.setGeometry(QtCore.QRect(150, 445, 550, 60))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")

        # 이전 버튼
        self.preButton = QtWidgets.QPushButton(how2)
        self.preButton.setGeometry(QtCore.QRect(220, 510, 200, 40))
        self.preButton.setStyleSheet("background-color:\"Orchid\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.preButton.setObjectName("preButton")

        # 다음 버튼
        self.nextButton = QtWidgets.QPushButton(how2)
        self.nextButton.setGeometry(QtCore.QRect(430, 510, 200, 40))
        self.nextButton.setStyleSheet("background-color:\"Orchid\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.nextButton.setObjectName("nextButton")

        self.retranslateUi(how2)
        QtCore.QMetaObject.connectSlotsByName(how2)

        # 버튼 이벤트 - 홈 버튼 클릭 시
        self.homeButton.clicked.connect(self.home_clicked)

        # 버튼 이벤트 - 다음 버튼 클릭 시
        self.nextButton.clicked.connect(self.next_clicked)

        # 버튼 이벤트 - 이전 버튼 클릭 시
        self.preButton.clicked.connect(self.pre_clicked)

    # home_clicked 함수 선언 - 메인 페이지로 돌아감
    def home_clicked(self):
        how1.close()
        homePT.show()

    # next_clicked 함수 선언 - 다음 페이지로 넘어감
    def next_clicked(self):
        how2.close()
        how3.show()

    # pre_clicked 함수 선언 - 이전 페이지로 돌아감
    def pre_clicked(self):
        how2.close()
        how1.show()

    def retranslateUi(self, how2):
        _translate = QtCore.QCoreApplication.translate
        how2.setWindowTitle(_translate("how2", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("how2", "<html><head/><body><p align=\"center\">Step2. 해당 운동 영상을 불러와 주세요.</p></body></html>"))
        self.preButton.setText(_translate("how2", "prev"))
        self.nextButton.setText(_translate("how2", "next"))

# How to Use step 3 페이지
class HowtoUse_step3(object):
    def setupUi(self, how3):

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png')  # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        how3.setWindowIcon(icon)

        # 창 설정
        how3.setObjectName("how3")
        how3.resize(850, 600)
        how3.setStyleSheet("background-color:\"Lavender\";")

        # 홈버튼
        icon1 = QtGui.QIcon('home.png')  # 홈버튼 이미지
        self.homeButton = QtWidgets.QPushButton(how3)
        self.homeButton.setGeometry(QtCore.QRect(790, 20, 40, 40))  # 버튼 위치 및 사이즈 설정
        self.homeButton.setIcon(icon1)  # 이미지 설정
        self.homeButton.setIconSize(QtCore.QSize(40, 40))  # 아이콘 사이즈 조정
        self.homeButton.setStyleSheet('QPushButton{border: 0px solid;}')
        # 클릭 시 홈화면으로 이동하도록

        # step 3 이미지
        self.Photo = QtWidgets.QWidget(how3)
        self.Photo.setGeometry(QtCore.QRect(150, 30, 550, 408))
        self.Photo.setAutoFillBackground(False)
        self.Photo.setStyleSheet("background-color:\"white\";image: url(:/exercise1/ex1.png);")
        self.Photo.setObjectName("Photo")

        # step 3 문구
        self.selectTitle = QtWidgets.QLabel(how3)
        self.selectTitle.setGeometry(QtCore.QRect(150, 445, 550, 60))
        self.selectTitle.setStyleSheet("font: 20pt\"경기천년제목M Medium\"; color:\"black\";")
        self.selectTitle.setObjectName("selectTitle")

        # 이전 버튼
        self.preButton = QtWidgets.QPushButton(how3)
        self.preButton.setGeometry(QtCore.QRect(220, 510, 200, 40))
        self.preButton.setStyleSheet("background-color:\"Orchid\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.preButton.setObjectName("preButton")

        # 다음 버튼
        self.nextButton = QtWidgets.QPushButton(how3)
        self.nextButton.setGeometry(QtCore.QRect(430, 510, 200, 40))
        self.nextButton.setStyleSheet("background-color:\"Orchid\"; color:\"white\";font: 16pt\"경기천년제목M Medium\";")
        self.nextButton.setObjectName("nextButton")

        self.retranslateUi(how3)
        QtCore.QMetaObject.connectSlotsByName(how3)

        # 버튼 이벤트 - 홈 버튼 클릭 시
        self.homeButton.clicked.connect(self.home_clicked)

        # 버튼 이벤트 - 다음 버튼 클릭 시
        self.nextButton.clicked.connect(self.next_clicked)

        # 버튼 이벤트 - 이전 버튼 클릭 시
        self.preButton.clicked.connect(self.pre_clicked)

    # home_clicked 함수 선언 - 메인 페이지로 돌아감
    def home_clicked(self):
        selectFi.close()
        homePT.show()

    # next_clicked 함수 선언 - 다음 페이지(운동 선택 페이지)로 넘어감
    def next_clicked(self):
        how3.close()
        selectEx.show()

    # pre_clicked 함수 선언 - 이전 페이지로 돌아감
    def pre_clicked(self):
        how3.close()
        how2.show()

    def retranslateUi(self, how3):
        _translate = QtCore.QCoreApplication.translate
        how3.setWindowTitle(_translate("how3", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectTitle.setText(_translate("how3", "<html><head/><body><p align=\"center\">Step3. 결과를 확인하세요.</p></body></html>"))
        self.preButton.setText(_translate("how3", "prev"))
        self.nextButton.setText(_translate("how3", "start"))

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
    how = QtWidgets.QDialog()
    ui3 = HowtoUse()
    ui3.setupUi(how)

    # step 1 페이지
    how1 = QtWidgets.QDialog()
    ui4 = HowtoUse_step1()
    ui4.setupUi(how1)

    # step 2 페이지
    how2 = QtWidgets.QDialog()
    ui5 = HowtoUse_step2()
    ui5.setupUi(how2)

    # step 3 페이지
    how3 = QtWidgets.QDialog()
    ui6 = HowtoUse_step3()
    ui6.setupUi(how3)

    sys.exit(app.exec_())
