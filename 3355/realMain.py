from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import selectExercise
import selectFile


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
    ui2 = selectExercise.Ui_selectExercise()
    ui2.setupUi(selectEx)

    # 파일 선택 페이지
    window = selectFile.MyWindow()

    sys.exit(app.exec_())