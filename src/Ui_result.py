# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tianmai/workspace/bysj_plus/ui/result.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import os
from PyQt5 import QtCore, QtGui, QtWidgets
import markdown
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRegExp

class MarkdownDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(889, 519)
        layout = QVBoxLayout()

        self.text_edit = QPlainTextEdit()
        layout.addWidget(self.text_edit)

        self.setLayout(layout)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

    def set_markdown_content(self, content):
        # html = markdown.markdown(content)
        # self.text_edit.setHtml(content)
        self.text_edit.setPlainText(content)
    
class Ui_result(object):
    def setupUi(self, result):
        result.setObjectName("result")
        result.resize(250, 200)
        self.listWidget = QtWidgets.QListWidget(result)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 230, 111))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.md_list=[]
        self.crash_path=''
        self.listWidget.addItems([])
        self.listWidget.setStyleSheet('''
 
                                        QListWidget::item::selected{ color:#6effe8; background:#4f5b62;}
                                        QListWidget::Item {
                                        color:#6effe8;
                                        padding: 0px;
                                        selection-color: #6effe8;
                                        selection-background-color: #4f5b62;
                                        }
                                      
                                        QScrollBar:vertical {
                                        width: 6px;
                                        height: 100px;
                                        background-color: transparent; 
                                        }

                                        QScrollBar::handle:vertical {
                                        border-radius: 3px; 
                                        background: #6effe8;
                                        }

                                      ''')
        self.label_2 = QtWidgets.QLabel(result)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 141, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(result)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 160, 71, 30))
        self.pushButton_2.setObjectName("show1")


        self.retranslateUi(result)
        QtCore.QMetaObject.connectSlotsByName(result)
        self.listWidget.itemDoubleClicked.connect(self.handle_item_double_clicked)
    def retranslateUi(self, result):
        _translate = QtCore.QCoreApplication.translate
        result.setWindowTitle(_translate("result", "result"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("result", "分析结果如下:"))
        self.pushButton_2.setText(_translate("result", "返回"))
        self.pushButton_2.clicked.connect(self.back)

    def handle_item_double_clicked(self, item):
        self.md_path=os.path.join(self.crash_path,item.text())
        with open(self.md_path, "r", encoding="utf-8") as file:
            markdown_text = file.read()

        dialog = MarkdownDialog(self)
        dialog.setWindowTitle(self.md_path)
        dialog.set_markdown_content(markdown_text)
        dialog.exec_()

    

    def shuaxin(self):
        self.listWidget.clear()
        self.listWidget.addItems(self.md_list)
    def get_md_list(self,md_list):
        self.md_list=md_list
    def get_crash_path(self,crash_path):
        self.crash_path=crash_path
    def back(self):
        pass
