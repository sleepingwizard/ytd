# -*- coding: utf-8 -*-

import sys
import os
import re
#import youtube_dl
from pytube import YouTube
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Set up the main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(919, 581)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: #ffffff;")

        # Create the central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create the main frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 571, 581))
        self.frame.setStyleSheet("background-color: #ff0000;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Widget 2: Enter Youtube Video URL
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(30, 30, 481, 201))
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 80, 421, 87))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: #ffffff;")
        self.plainTextEdit.setObjectName("plainTextEdit")

        # Widget 3: Directory
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setGeometry(QtCore.QRect(30, 250, 481, 131))
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: #ffffff;")
        self.lineEdit.setObjectName("lineEdit")
        self.directory = os.path.join(os.path.expanduser("~"), "Downloads")
        self.lineEdit.setText(self.directory)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(360, 70, 81, 31))
        self.pushButton.setStyleSheet("background-color: #ffffff;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change_directory)

        # Widget 4: Download
        self.widget_4 = QtWidgets.QWidget(self.frame)
        self.widget_4.setGeometry(QtCore.QRect(30, 400, 481, 131))
        self.widget_4.setObjectName("widget_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #ffffff;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.download_videos)
        self.progressBar = QtWidgets.QProgressBar(self.widget_4)
        self.progressBar.setGeometry(QtCore.QRect(120, 90, 251, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        # Set up the second frame
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(570, 0, 351, 581))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: #fff330;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        # Labels for the second frame
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 90, 311, 111))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(48)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(70, 200, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(48)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(48)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Additional widgets for the second frame
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(0, 280, 351, 121))
        self.widget.setObjectName("widget")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(20, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
        self.label_4.setObjectName("label_4")

        self.widget_5 = QtWidgets.QWidget(self.frame_2)
        self.widget_5.setGeometry(QtCore.QRect(0, 420, 351, 141))
        self.widget_5.setObjectName("widget_5")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_4.setGeometry(QtCore.QRect(220, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
        self.label_7.setObjectName("label_7")
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_5.setGeometry(QtCore.QRect(220, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_6.setGeometry(QtCore.QRect(30, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_6.setObjectName("radioButton_6")

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Enter Youtube Video URL"))
        self.pushButton.setText(_translate("MainWindow", "Change Directory"))
        self.label_6.setText(_translate("MainWindow", "Directory"))
        self.pushButton_2.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "YouTube"))
        self.label_2.setText(_translate("MainWindow", "Video"))
        self.label_3.setText(_translate("MainWindow", "Convert"))
        self.radioButton.setText(_translate("MainWindow", "Video(.mp4)"))
        self.radioButton_2.setText(_translate("MainWindow", "Audio (.mp3)"))
        self.label_4.setText(_translate("MainWindow", "Convert To"))
        self.radioButton_3.setText(_translate("MainWindow", "144p"))
        self.radioButton_4.setText(_translate("MainWindow", "240p"))
        self.label_7.setText(_translate("MainWindow", "Quality"))
        self.radioButton_5.setText(_translate("MainWindow", "720p"))
        self.radioButton_6.setText(_translate("MainWindow", "1080p"))

    def change_directory(self):
        directory = QFileDialog.getExistingDirectory(None, "Select Directory", self.directory, QFileDialog.ShowDirsOnly)

        if directory:
            self.directory = directory

        self.lineEdit.setText(directory)

    def download_videos(self):
        # Get the text from the QPlainTextEdit
        text = self.plainTextEdit.toPlainText()
        
        # Split the text into separate lines, URLs, or by comma
        urls = re.split(r'[\n, ]+', text)
        print (urls)
        
        if not urls:
            QMessageBox.warning(self.centralwidget, "Error", "Please enter valid YouTube video URL(s).")
            return

        # Check if the download directory exists, and create it if it doesn't
        if not os.path.exists(self.directory):
            try:
                os.makedirs(self.directory)
            except OSError as e:
                QMessageBox.critical(self.centralwidget, "Error", f"Failed to create download directory: {str(e)}")
                return

        # Download each video
        for url in urls:
            try:
                yt = YouTube(url)
                stream = yt.streams.get_highest_resolution()
                # Get the quality of the video
                quality = stream.resolution or "Unknown"
                # Construct the file name with quality prefix
                file_name = f"{quality}_{yt.title}.{stream.subtype}"
                
                stream.download(output_path=self.directory, filename=re.sub(r'[<>:"/\\|?*]', '_', file_name))

                QMessageBox.information(self.centralwidget, "Download Complete", "Video downloaded successfully!")
            except Exception as e:
                print(str(e))
                QMessageBox.critical(self.centralwidget, "Error", f"An error occurred: {str(e)}")

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            # Update progress bar
            progress = int(d['_percent_str'].strip('%'))
            self.progressBar.setValue(progress)

        elif d['status'] == 'finished':
            # Download completed
            QMessageBox.information(self.centralwidget, "Download Complete", "Video downloaded successfully!")


    def get_selected_quality(self):
        if self.radioButton_3.isChecked():
            return 'bestvideo[height<=144]+bestaudio/best[height<=144]'
        elif self.radioButton_4.isChecked():
            return 'bestvideo[height<=240]+bestaudio/best[height<=240]'
        elif self.radioButton_5.isChecked():
            return 'bestvideo[height<=720]+bestaudio/best[height<=720]'
        elif self.radioButton_6.isChecked():
            return 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
        else:
            return 'best'


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
