# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tianmai/workspace/bysj_plus/ui/result.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_result(object):
    def setupUi(self, result):
        result.setObjectName("result")
        result.resize(250, 200)
        self.listWidget = QtWidgets.QListWidget(result)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 230, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(True)
        font.setKerning(False)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_2 = QtWidgets.QLabel(result)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 141, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(result)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 160, 71, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(result)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 160, 71, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(result)
        QtCore.QMetaObject.connectSlotsByName(result)

    def retranslateUi(self, result):
        _translate = QtCore.QCoreApplication.translate
        result.setWindowTitle(_translate("result", "result"))
        self.listWidget.setSortingEnabled(False)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(1)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(2)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(3)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(4)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(5)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(6)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(7)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(8)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(9)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(10)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(11)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(12)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(13)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(14)
        item.setText(_translate("result", "新建项目"))
        item = self.listWidget.item(15)
        item.setText(_translate("result", "新建项目"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("result", "crash分析结果如下:"))
        self.pushButton_2.setText(_translate("result", "返回"))
        self.pushButton_3.setText(_translate("result", "确认"))