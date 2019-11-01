# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectFile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import *

class Ui_selectVideo(object):
    def setupUi(self, selectVideo):
        selectVideo.setObjectName("selectVideo")
        selectVideo.setEnabled(False)
        selectVideo.resize(850, 600)
        selectVideo.setStyleSheet("background-color:\"Aliceblue\";")

        # 아이콘
        icon = QtGui.QIcon()
        pixicon = QPixmap('heart.png') # 아이콘에 이미지 삽입
        icon.addPixmap(QtGui.QPixmap(pixicon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectVideo.setWindowIcon(icon)

        self.selectVideoTitle = QtWidgets.QLabel(selectVideo)
        self.selectVideoTitle.setGeometry(QtCore.QRect(200, 220, 450, 60))
        self.selectVideoTitle.setStyleSheet("color:\"Black\"; font: 57 26pt \"경기천년제목M Medium\";")
        self.selectVideoTitle.setObjectName("selectVideoTitle")
        self.openFileButton = QtWidgets.QPushButton(selectVideo)
        self.openFileButton.setGeometry(QtCore.QRect(250, 300, 350, 40))
        self.openFileButton.setStyleSheet("background-color:\"Dodgerblue\"; color:\"White\";font: 18pt \"경기천년제목M Medium\";")
        self.openFileButton.setObjectName("openFileButton")

        self.retranslateUi(selectVideo)
        QtCore.QMetaObject.connectSlotsByName(selectVideo)

        self.openFileButton.clicked.connect(self.openFile())

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(parent=selectVideo,
                                                  caption="Select file to open",
                                                  directory="",
                                                  filter="video(*.mp4, *.m4a, *.wav)",
                                                  initialFilter="video(*.mp4, *.m4a, *.wav)",
                                                  options=)
        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.statusBar.showMessage(fileName)
            self.play()

    def retranslateUi(self, selectVideo):
        _translate = QtCore.QCoreApplication.translate
        selectVideo.setWindowTitle(_translate("selectVideo", "HomePT와 함께 하는 올바른 홈트레이닝 라이프"))
        self.selectVideoTitle.setText(_translate("selectVideo", "<html><head/><body><p align=\"center\">운동 영상을 선택해주세요.</p></body></html>"))
        self.openFileButton.setText(_translate("selectVideo", "open video file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectVideo = QtWidgets.QDialog()
    ui = Ui_selectVideo()
    ui.setupUi(selectVideo)
    selectVideo.show()
    sys.exit(app.exec_())

