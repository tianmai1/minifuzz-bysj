# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tianmai/workspace/bysj_plus/ui/show.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_show1(object):
    def setupUi(self, show1):
        show1.setObjectName("show1")
        show1.resize(250, 200)
        self.test_name = QtWidgets.QLabel(show1)
        self.test_name.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.test_name.setObjectName("test_name")
        self.input_name = QtWidgets.QComboBox(show1)
        self.input_name.setGeometry(QtCore.QRect(90, 10, 151, 31))
        self.input_name.setStyleSheet("QComboBox {\"\n"
"                                    \"combobox-popup: 0;\\n\"  \n"
"                                    \"font-size:15px; \"\n"
"                                    \"color: #6effe8;\\n\"\n"
"                                    \"line-height:24px; \"}\n"
"")
        self.input_name.setMaxVisibleItems(3)
        self.input_name.setObjectName("input_name")
        self.input_name.addItem("")
        self.input_name.addItem("")
        self.input_name.addItem("")
        self.show_txt = QtWidgets.QLabel(show1)
        self.show_txt.setGeometry(QtCore.QRect(10, 45, 81, 31))
        self.show_txt.setObjectName("show_txt")
        self.input_txt = QtWidgets.QComboBox(show1)
        self.input_txt.setGeometry(QtCore.QRect(90, 45, 151, 31))
        self.input_txt.setStyleSheet("QComboBox {\"\n"
"                                    \"combobox-popup: 0;\\n\"  \n"
"                                    \"font-size:15px; \"\n"
"                                    \"color: #6effe8;\\n\"\n"
"                                    \"line-height:24px; \"}\n"
"")
        self.input_txt.setMaxVisibleItems(3)
        self.input_txt.setObjectName("input_txt")
        self.input_txt.addItem("")
        self.input_txt.addItem("")
        self.input_txt.addItem("")
        self.input_txt.addItem("")
        self.pushButton = QtWidgets.QPushButton(show1)
        self.pushButton.setGeometry(QtCore.QRect(160, 150, 71, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(show1)
        self.label.setGeometry(QtCore.QRect(0, 80, 161, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/tianmai/workspace/bysj_plus/ui/../images/和朋友玩耍.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(show1)
        QtCore.QMetaObject.connectSlotsByName(show1)

    def retranslateUi(self, show1):
        _translate = QtCore.QCoreApplication.translate
        show1.setWindowTitle(_translate("show1", "show"))
        self.test_name.setText(_translate("show1", "测试名称："))
        self.input_name.setItemText(0, _translate("show1", "新建项目"))
        self.input_name.setItemText(1, _translate("show1", "新建项目"))
        self.input_name.setItemText(2, _translate("show1", "新建项目"))
        self.show_txt.setText(_translate("show1", "查看内容："))
        self.input_txt.setItemText(0, _translate("show1", "fuzz过程"))
        self.input_txt.setItemText(1, _translate("show1", "覆盖率"))
        self.input_txt.setItemText(2, _translate("show1", "崩溃分析"))
        self.input_txt.setItemText(3, _translate("show1", "超时分析"))
        self.pushButton.setText(_translate("show1", "确认"))
