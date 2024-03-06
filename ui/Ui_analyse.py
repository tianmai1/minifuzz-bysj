# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tianmai/workspace/bysj_plus/minifuzz-bysj/ui/analyse.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_analyse(object):
    def setupUi(self, analyse):
        analyse.setObjectName("analyse")
        analyse.resize(250, 200)
        self.test_name = QtWidgets.QLabel(analyse)
        self.test_name.setGeometry(QtCore.QRect(10, 10, 81, 35))
        self.test_name.setObjectName("test_name")
        self.show_txt_2 = QtWidgets.QLabel(analyse)
        self.show_txt_2.setGeometry(QtCore.QRect(10, 50, 101, 35))
        self.show_txt_2.setObjectName("show_txt_2")
        self.input_name = QtWidgets.QComboBox(analyse)
        self.input_name.setGeometry(QtCore.QRect(90, 10, 151, 35))
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
        self.input_num = QtWidgets.QSpinBox(analyse)
        self.input_num.setGeometry(QtCore.QRect(130, 50, 111, 35))
        self.input_num.setObjectName("input_num")
        self.show_txt_3 = QtWidgets.QLabel(analyse)
        self.show_txt_3.setGeometry(QtCore.QRect(10, 90, 51, 35))
        self.show_txt_3.setObjectName("show_txt_3")
        self.input_analyse = QtWidgets.QComboBox(analyse)
        self.input_analyse.setGeometry(QtCore.QRect(90, 90, 151, 35))
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
        self.pushButton_2 = QtWidgets.QPushButton(analyse)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 150, 61, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(analyse)
        self.label.setGeometry(QtCore.QRect(-5, 100, 111, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/tianmai/workspace/bysj_plus/minifuzz-bysj/ui/../src/tools/images/兴奋.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(analyse)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 150, 61, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(analyse)
        QtCore.QMetaObject.connectSlotsByName(analyse)

    def retranslateUi(self, analyse):
        _translate = QtCore.QCoreApplication.translate
        analyse.setWindowTitle(_translate("analyse", "analyse"))
        self.test_name.setText(_translate("analyse", "测试名称："))
        self.show_txt_2.setText(_translate("analyse", "设置进程数:"))
        self.input_name.setItemText(0, _translate("analyse", "新建项目"))
        self.input_name.setItemText(1, _translate("analyse", "新建项目"))
        self.input_name.setItemText(2, _translate("analyse", "新建项目"))
        self.show_txt_3.setText(_translate("analyse", "类型:"))
        self.input_analyse.setItemText(0, _translate("analyse", "崩溃分析"))
        self.input_analyse.setItemText(1, _translate("analyse", "超时分析"))
        self.pushButton_2.setText(_translate("analyse", "确认"))
        self.pushButton_3.setText(_translate("analyse", "高级"))
