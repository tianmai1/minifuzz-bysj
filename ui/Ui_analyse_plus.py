# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tianmai/workspace/bysj_plus/minifuzz-bysj/ui/analyse_plus.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_analyse_plus(object):
    def setupUi(self, analyse_plus):
        analyse_plus.setObjectName("analyse_plus")
        analyse_plus.resize(250, 200)
        self.in_path = QtWidgets.QLabel(analyse_plus)
        self.in_path.setGeometry(QtCore.QRect(10, 10, 81, 30))
        self.in_path.setObjectName("in_path")
        self.out_path = QtWidgets.QLabel(analyse_plus)
        self.out_path.setGeometry(QtCore.QRect(10, 80, 71, 30))
        self.out_path.setObjectName("out_path")
        self.show_txt_3 = QtWidgets.QLabel(analyse_plus)
        self.show_txt_3.setGeometry(QtCore.QRect(10, 115, 51, 30))
        self.show_txt_3.setObjectName("show_txt_3")
        self.input_analyse = QtWidgets.QComboBox(analyse_plus)
        self.input_analyse.setGeometry(QtCore.QRect(90, 115, 151, 35))
        self.input_analyse.setStyleSheet("QComboBox {\"\n"
"                                    \"combobox-popup: 0;\\n\"  \n"
"                                    \"font-size:15px; \"\n"
"                                    \"color: #6effe8;\\n\"\n"
"                                    \"line-height:24px; \"}\n"
"")
        self.input_analyse.setMaxVisibleItems(3)
        self.input_analyse.setObjectName("input_analyse")
        self.input_analyse.addItem("")
        self.input_analyse.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(analyse_plus)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 160, 71, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.in_path_input = QtWidgets.QLineEdit(analyse_plus)
        self.in_path_input.setGeometry(QtCore.QRect(90, 10, 151, 30))
        self.in_path_input.setObjectName("in_path_input")
        self.cmd_input = QtWidgets.QLineEdit(analyse_plus)
        self.cmd_input.setGeometry(QtCore.QRect(90, 45, 151, 30))
        self.cmd_input.setObjectName("cmd_input")
        self.cmd = QtWidgets.QLabel(analyse_plus)
        self.cmd.setGeometry(QtCore.QRect(10, 45, 81, 30))
        self.cmd.setObjectName("cmd")
        self.out_path_input = QtWidgets.QLineEdit(analyse_plus)
        self.out_path_input.setGeometry(QtCore.QRect(90, 80, 151, 30))
        self.out_path_input.setObjectName("out_path_input")
        self.pushButton_3 = QtWidgets.QPushButton(analyse_plus)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 160, 71, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(analyse_plus)
        QtCore.QMetaObject.connectSlotsByName(analyse_plus)

    def retranslateUi(self, analyse_plus):
        _translate = QtCore.QCoreApplication.translate
        analyse_plus.setWindowTitle(_translate("analyse_plus", "analyse_plus"))
        self.in_path.setText(_translate("analyse_plus", "crash目录:"))
        self.out_path.setText(_translate("analyse_plus", "输出目录："))
        self.show_txt_3.setText(_translate("analyse_plus", "类型:"))
        self.input_analyse.setItemText(0, _translate("analyse_plus", "崩溃分析"))
        self.input_analyse.setItemText(1, _translate("analyse_plus", "超时分析"))
        self.pushButton_2.setText(_translate("analyse_plus", "返回"))
        self.cmd.setText(_translate("analyse_plus", "运行命令："))
        self.pushButton_3.setText(_translate("analyse_plus", "确认"))
