# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tianmai/workspace/bysj_plus/ui/fuzz.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fuzz(object):
    def setupUi(self, fuzz):
        fuzz.setObjectName("fuzz")
        fuzz.resize(250, 220)
        self.pushButton = QtWidgets.QPushButton(fuzz)
        self.pushButton.setGeometry(QtCore.QRect(20, 100, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(fuzz)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 100, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(fuzz)
        QtCore.QMetaObject.connectSlotsByName(fuzz)

    def retranslateUi(self, fuzz):
        _translate = QtCore.QCoreApplication.translate
        fuzz.setWindowTitle(_translate("fuzz", "fuzz"))
        self.pushButton.setText(_translate("fuzz", "新建"))
        self.pushButton_2.setText(_translate("fuzz", "PushButton"))
