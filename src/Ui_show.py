from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil
import subprocess
from time import sleep
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QIcon, QPixmap,QRegExpValidator
import psutil
import tools.tool as tool
from qt_material import apply_stylesheet
import webbrowser
from Ui_fuzz  import _info


bysj_path=os.path.dirname(os.path.abspath(__file__))
class Ui_show(object):
    def setupUi(self, show1):
        show1.setObjectName("show1")
        show1.resize(250, 200)
        self.test_name = QtWidgets.QLabel(show1)
        self.test_name.setGeometry(QtCore.QRect(10, 10, 81, 35))
        self.test_name.setObjectName("test_name")
        self.input_name = QtWidgets.QComboBox(show1)
        self.input_name.setGeometry(QtCore.QRect(90, 10, 151, 35))
        self.input_name.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.input_name.setStyleSheet("QComboBox {"
                                    "combobox-popup: 0;\n"  # 滚动条设置必需
                                    "font-size:15px; "
                                    "color: #6effe8;\n"
                                    "line-height:24px; }\n"

                                    "QComboBox QAbstractItemView {"  # 下拉选项样式
                                    "color:#6effe8; "
                                    "background: transparent; "
                                    "selection-color: #6effe8;"
                                    "selection-background-color: #4f5b62;"
                                    "}\n"

                                    "QComboBox QAbstractScrollArea QScrollBar:vertical {"  # 滚动条样式
                                    "width: 6px;\n"
                                    "height: 100px;"
                                    "background-color: transparent;  }\n"

                                    "QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"  # 滚动条样式
                                    "border-radius: 3px;   "
                                    "background: #6effe8;}\n"
                                    
                                    )
        self.input_name.setMaxVisibleItems(4)
        self.input_name.setObjectName("input_name")
        self.input_name.addItems(tool.get_name())
        self.show_txt = QtWidgets.QLabel(show1)
        self.show_txt.setGeometry(QtCore.QRect(10, 50, 81, 35))
        self.show_txt.setObjectName("show_txt")
        self.input_txt = QtWidgets.QComboBox(show1)
        self.input_txt.setGeometry(QtCore.QRect(90, 50, 151, 35))
        self.input_txt.setStyleSheet("QComboBox {"
                                    "combobox-popup: 0;\n"  # 滚动条设置必需
                                    "font-size:15px; "
                                    "color: #6effe8;\n"
                                    "line-height:24px; }\n"

                                    "QComboBox QAbstractItemView {"  # 下拉选项样式
                                    "color:#6effe8; "
                                    "background: transparent; "
                                    "selection-color: #6effe8;"
                                    "selection-background-color: #4f5b62;"
                                    "}\n"
                                    )
        self.input_txt.setMaxVisibleItems(4)
        self.input_txt.setObjectName("input_txt")
        self.input_txt.addItem("fuzz过程")
        self.input_txt.addItem("覆盖率")
        self.input_txt.addItem("崩溃分析结果")
        self.input_txt.addItem("超时分析结果")
        self.pushButton = QtWidgets.QPushButton(show1)
        self.pushButton.setGeometry(QtCore.QRect(160, 150, 71, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(show1)
        self.label.setGeometry(QtCore.QRect(0, 60, 161, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(bysj_path+"/tools/images/和朋友玩耍.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.retranslateUi(show1)
        QtCore.QMetaObject.connectSlotsByName(show1)

    def retranslateUi(self, show1):
        _translate = QtCore.QCoreApplication.translate
        show1.setWindowTitle(_translate("show1", "show"))
        self.test_name.setText(_translate("show1", "测试名称："))
        self.show_txt.setText(_translate("show1", "查看内容："))
        self.pushButton.setText(_translate("show1", "确认"))

    def pushButton_clicked(self):
        name=self.input_name.currentText()
        if not name:
            _info("错误","请先新建一个测试")
            return
        txt=self.input_txt.currentText()
        if txt=="fuzz过程":
            self.fuzz_show()
        elif txt=="覆盖率":
            self.cov_show()
        elif txt=="崩溃分析结果":
            self.crash_show("crashes")
        elif txt=="超时分析结果":
            self.crash_show("hangs")

    def fuzz_show(self):
        name = self.input_name.currentText()
        test_list = tool.get_list()
        index='out/'+name+"/cov/web/index.html"
        cov_path='out/'+name+"/cov"
        if name in test_list:
            command = "tmux at -t "+name
            size = '162'
            tool.cmd(command, size)
            
        else:
            _info("提示", "此测试已经停止运行")
        return

    def crash_show(self,type:str):
        pass

    def cov_show(self):
        name = self.input_name.currentText()
        index="out/"+name+"/cov/web/index.html"
        if os.path.exists(index):
            webbrowser.open(index)
        else:
            _info("错误","此测试不存在或没有生成覆盖率信息")
            try:
                shutil.rmtree("out/"+name+"/cov")
            except:
                pass
        return  
    
    def shuaxin(self):
        self.input_name.clear()
        self.input_name.addItems(tool.get_name())