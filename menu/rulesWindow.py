# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rules.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class RulesWindow(object):
    def __init__(self):
        self.label_4 = None
        self.label_3 = None
        self.label_2 = None
        self.label = None

    def setup_ui(self, rules_dialog):
        rules_dialog.setObjectName("Dialog")
        rules_dialog.resize(400, 300)
        rules_dialog.setStyleSheet("background-color: rgb(79, 80, 78);")
        self.label = QtWidgets.QLabel(rules_dialog)
        self.label.setGeometry(QtCore.QRect(90, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(rules_dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 341, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(15)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(253, 201, 100);")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(rules_dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 341, 59))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(242, 95, 92);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(rules_dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 341, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(253, 201, 100);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslate_ui(rules_dialog)
        QtCore.QMetaObject.connectSlotsByName(rules_dialog)

    def retranslate_ui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "How to play?"))
        self.label_2.setText(_translate("Dialog", "\"You need move a numbers to the same number. A new number will be created there\""))
        self.label_3.setText(_translate("Dialog", "Tap the first number then tap the second number has the same value"))
        self.label_4.setText(_translate("Dialog", "Try to get \"12\" to win the game!"))
