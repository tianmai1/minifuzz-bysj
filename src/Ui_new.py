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

class Ui_new_2(object):
    def setupUi(self, fuzz):
        fuzz.setObjectName("new")
        fuzz.resize(250, 220)
        label_program = QLabel("执行命令:")
        # label_program.setStyleSheet('color: cyan;')
        self.input_program = QLineEdit()
        self.input_program.setStyleSheet("font-size: 15px; color: #6effe8;")
        #self.input_program.setText("../../codedoc/codedoc @@")
        self.input_program.setPlaceholderText("例如：./test @@")

        label_testcase = QLabel("测试用例:")
        # label_testcase.setStyleSheet('color: cyan;')
        self.input_testcase = QLineEdit()
        self.input_testcase.setStyleSheet("font-size: 15px; color: #6effe8;")
        #self.input_testcase.setText(bysj_path+"/test/in")
        self.input_testcase.setPlaceholderText("文件夹")

        label_name = QLabel("目标源码路径:")
        # label_name.setStyleSheet('color: cyan;')
        self.input_name = QLineEdit()
        self.input_name.setStyleSheet("font-size: 15px; color: #6effe8;")
        #self.input_name.setText(bysj_path+"/test/codedoc")
        self.input_name.setPlaceholderText("默认为'.'")
        # 创建可勾选项
        self.coverage_checkbox = QCheckBox("启动覆盖率监控")

        # 创建开始按钮
        start_button = QPushButton("开始")
        start_button.setFixedSize(60, 30)
        # 设置返回按钮的样式
        back_button = QPushButton("返回")
        # back_button.setIcon(QIcon("source/返回.png"))
        back_button.setFixedSize(60, 30)
        back_button.setObjectName("fuzz")
        # 连接按钮的点击事件到相应的槽函数
        start_button.clicked.connect(self.start_button_clicked)
        back_button.clicked.connect(self.back_button_clicked)

        # 创建水平布局，并将返回按钮和开始按钮添加到布局中
        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(start_button)
        layout_buttons.addWidget(back_button)
        layout_buttons.setAlignment(Qt.AlignHCenter)

        name = QHBoxLayout()
        name.addWidget(label_name)
        name.addWidget(self.input_name)
        program = QHBoxLayout()
        program.addWidget(label_program)
        program.addWidget(self.input_program)
        testcase = QHBoxLayout()
        testcase.addWidget(label_testcase)
        testcase.addWidget(self.input_testcase)

        # 创建垂直布局，并将标签、输入框、可勾选项和按钮布局添加到垂直布局中
        layout = QVBoxLayout()
        # layout.addWidget(back_button)

        layout.addLayout(program)
        layout.addLayout(testcase)
        layout.addLayout(name)
        layout.addWidget(self.coverage_checkbox)
        layout.addLayout(layout_buttons)
        self.setLayout(layout)

    def get_text(self,name):
        self.text=name
        # print(self.text)

    def start_button_clicked(self):
        src = self.input_name.text()
        program = self.input_program.text()
        testcase = self.input_testcase.text()
        coverage_enabled = self.coverage_checkbox.isChecked()
        info = tool.run(self.text, program, testcase, coverage_enabled, src)
        if info != '':
            _info("错误", info)

    def back_button_clicked(self):
        pass