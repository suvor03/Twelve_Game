# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist

from game.game import Game
from menu.rulesWindow import RulesWindow


class StartMenu(object):
    def __init__(self):
        self.ui = None
        self.rulesWindow = None
        self.rulesButton = None
        self.offMusic = None
        self.onMusic = None
        self.label = None
        self.startButton = None
        self.nameOfGame = None
        self.centralwidget = None
        self.playlist = QMediaPlaylist()
        self.media_player = QMediaPlayer()

    def setup_ui(self, main_window):
        main_window.setObjectName("Menu")
        main_window.resize(800, 600)
        main_window.setStyleSheet("background-color: rgb(79, 80, 78);")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.nameOfGame = QtWidgets.QLabel(self.centralwidget)
        self.nameOfGame.setGeometry(QtCore.QRect(180, 10, 441, 151))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(120)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.nameOfGame.setFont(font)
        self.nameOfGame.setStyleSheet("color: rgb(242, 95, 92);")
        self.nameOfGame.setAlignment(QtCore.Qt.AlignCenter)
        self.nameOfGame.setObjectName("nameOfGame")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(290, 220, 241, 121))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color: rgb(255, 224, 102);\n"
                                       "color: rgb(80, 81, 79);\n""")
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.start_game)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 380, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(229, 199, 91);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.onMusic = QtWidgets.QRadioButton(self.centralwidget)
        self.onMusic.setGeometry(QtCore.QRect(340, 420, 51, 17))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.onMusic.setFont(font)
        self.onMusic.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.onMusic.setObjectName("onMusic")
        self.onMusic.toggled.connect(self.toggle_music)

        self.offMusic = QtWidgets.QRadioButton(self.centralwidget)
        self.offMusic.setGeometry(QtCore.QRect(420, 420, 51, 17))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.offMusic.setFont(font)
        self.offMusic.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.offMusic.setObjectName("offMusic")
        self.offMusic.toggled.connect(self.toggle_music)

        self.rulesButton = QtWidgets.QPushButton(self.centralwidget)
        self.rulesButton.setGeometry(QtCore.QRect(340, 490, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.rulesButton.setFont(font)
        self.rulesButton.setStyleSheet("background-color: rgb(231, 201, 92);")
        self.rulesButton.setObjectName("rulesButton")
        self.rulesButton.clicked.connect(self.show_rules)

        main_window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameOfGame.setText(_translate("MainWindow", "twelve"))
        self.startButton.setText(_translate("MainWindow", "start"))
        self.label.setText(_translate("MainWindow", "Music"))
        self.onMusic.setText(_translate("MainWindow", "On"))
        self.offMusic.setText(_translate("MainWindow", "Off"))
        self.rulesButton.setText(_translate("MainWindow", "rules"))

    @staticmethod
    def start_game():
        game = Game()
        game.show()
        start_window.hide()

    def toggle_music(self):
        if self.onMusic.isChecked():
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('./music.mp3')))
            self.media_player.setPlaylist(self.playlist)
            self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
            self.media_player.play()
        else:
            self.media_player.stop()

    def show_rules(self):
        self.rulesWindow = QtWidgets.QDialog()
        self.ui = RulesWindow()
        self.ui.setup_ui(self.rulesWindow)
        self.rulesWindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    start_window = QtWidgets.QMainWindow()
    ui = StartMenu()
    ui.setup_ui(start_window)
    start_window.show()
    sys.exit(app.exec_())