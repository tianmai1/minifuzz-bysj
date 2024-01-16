# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tianmai/workspace/bysj_plus/ui/minifuzz.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_minifuzz(object):
    def setupUi(self, minifuzz):
        minifuzz.setObjectName("minifuzz")
        minifuzz.resize(329, 200)
        font = QtGui.QFont()
        font.setKerning(True)
        minifuzz.setFont(font)
        self.fuzz = QtWidgets.QPushButton(minifuzz)
        self.fuzz.setGeometry(QtCore.QRect(0, 0, 71, 30))
        self.fuzz.setObjectName("fuzz")
        self.show1 = QtWidgets.QPushButton(minifuzz)
        self.show1.setGeometry(QtCore.QRect(0, 30, 71, 30))
        self.show1.setObjectName("show1")
        self.analyse = QtWidgets.QPushButton(minifuzz)
        self.analyse.setGeometry(QtCore.QRect(0, 60, 71, 31))
        self.analyse.setObjectName("analyse")
        self.frame = QtWidgets.QFrame(minifuzz)
        self.frame.setGeometry(QtCore.QRect(70, 0, 251, 201))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(minifuzz)
        self.label.setGeometry(QtCore.QRect(0, 130, 71, 51))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/tianmai/workspace/bysj_plus/ui/../images/蓝色别墅.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame.raise_()
        self.label.raise_()
        self.fuzz.raise_()
        self.show1.raise_()
        self.analyse.raise_()

        self.retranslateUi(minifuzz)
        QtCore.QMetaObject.connectSlotsByName(minifuzz)

    def retranslateUi(self, minifuzz):
        _translate = QtCore.QCoreApplication.translate
        minifuzz.setWindowTitle(_translate("minifuzz", "MiniFuzz"))
        self.fuzz.setText(_translate("minifuzz", "测试"))
        self.show1.setText(_translate("minifuzz", "展示"))
        self.analyse.setText(_translate("minifuzz", "分析"))
