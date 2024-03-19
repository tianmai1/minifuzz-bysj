import os
from PyQt5 import QtCore, QtGui, QtWidgets
import tools.tool as tool
from Ui_fuzz  import _info

bysj_path=os.path.dirname(os.path.abspath(__file__))
current_dir = os.getcwd()

class Ui_new_2(object):
    def setupUi(self, new):
        new.setObjectName("new")
        new.resize(250, 200)
        self.label_name = QtWidgets.QLabel(new)
        self.label_name.setGeometry(QtCore.QRect(10, 85, 111, 33))
        self.label_name.setObjectName("label_name")
        self.source_name = QtWidgets.QLineEdit(new)
        self.source_name.setGeometry(QtCore.QRect(110, 85, 111, 33))
        self.source_name.setObjectName("source_name")
        self.back_button = QtWidgets.QPushButton(new)
        self.back_button.setGeometry(QtCore.QRect(130, 160, 60, 30))
        self.back_button.setObjectName("fuzz")
        self.source_path_button = QtWidgets.QToolButton(new)
        self.source_path_button.setGeometry(QtCore.QRect(220, 90, 26, 24))
        self.source_path_button.setObjectName("source_path_button")
        self.start_button = QtWidgets.QPushButton(new)
        self.start_button.setGeometry(QtCore.QRect(60, 160, 60, 30))
        self.start_button.setObjectName("start_button")
        self.cmd_name = QtWidgets.QLineEdit(new)
        self.cmd_name.setGeometry(QtCore.QRect(80, 5, 141, 33))
        self.cmd_name.setObjectName("cmd_name")
        self.label_testcase = QtWidgets.QLabel(new)
        self.label_testcase.setGeometry(QtCore.QRect(10, 45, 81, 33))
        self.label_testcase.setObjectName("label_testcase")
        self.label_program = QtWidgets.QLabel(new)
        self.label_program.setGeometry(QtCore.QRect(10, 5, 81, 33))
        self.label_program.setObjectName("label_program")
        self.input_testcase = QtWidgets.QLineEdit(new)
        self.input_testcase.setGeometry(QtCore.QRect(80, 45, 141, 33))
        self.input_testcase.setObjectName("input_testcase")
        self.testcase_path_button = QtWidgets.QToolButton(new)
        self.testcase_path_button.setGeometry(QtCore.QRect(220, 50, 26, 24))
        self.testcase_path_button.setObjectName("testcase_path_button")
        self.coverage_checkbox = QtWidgets.QCheckBox(new)
        self.coverage_checkbox.setGeometry(QtCore.QRect(10, 125, 131, 23))
        self.coverage_checkbox.setObjectName("coverage_checkbox")
        self.program_path_button = QtWidgets.QToolButton(new)
        self.program_path_button.setGeometry(QtCore.QRect(220, 10, 26, 24))
        self.program_path_button.setObjectName("program_path_button")

        self.source_name.setStyleSheet("font-size: 15px; color: #6effe8;")
        self.source_name.setPlaceholderText("默认为'.'")
        self.cmd_name.setStyleSheet("font-size: 15px; color: #6effe8;")
        self.cmd_name.setPlaceholderText("例如：./test @@")
        self.input_testcase.setStyleSheet("font-size: 15px; color: #6effe8;")
        self.input_testcase.setPlaceholderText("文件夹")
        self.start_button.clicked.connect(self.start_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)
        self.testcase_path_button.clicked.connect(self.msg_testcase)
        self.source_path_button.clicked.connect(self.msg_source)
        self.program_path_button.clicked.connect(self.msg_program)

        self.retranslateUi(new)
        QtCore.QMetaObject.connectSlotsByName(new)

    def retranslateUi(self, new):
        _translate = QtCore.QCoreApplication.translate
        new.setWindowTitle(_translate("new", "new"))
        self.label_name.setText(_translate("new", "目标源码路径："))
        self.back_button.setText(_translate("new", "返回"))
        self.source_path_button.setText(_translate("new", "📂"))
        self.start_button.setText(_translate("new", "开始"))
        self.label_testcase.setText(_translate("new", "测试用例："))
        self.label_program.setText(_translate("new", "执行命令："))
        self.testcase_path_button.setText(_translate("new", "📂"))
        self.coverage_checkbox.setText(_translate("new", "启动覆盖率监控"))
        self.program_path_button.setText(_translate("new", "📂"))

    def get_text(self,name):
        self.text=name

    def msg_testcase(self,Filepath):
        m = QtWidgets.QFileDialog.getExistingDirectory(None,"测试用例文件夹",current_dir)
        self.input_testcase.setText(m)

    def msg_source(self,Filepath):
        m = QtWidgets.QFileDialog.getExistingDirectory(None,"源码文件夹",current_dir)
        self.source_name.setText(m)

    def msg_program(self,Filepath):
        m = QtWidgets.QFileDialog.getOpenFileName(None,  "目标文件","./")
        self.cmd_name.setText(m[0])   
        # print(m) 

    def start_button_clicked(self):
        src = self.source_name.text()
        program = self.cmd_name.text()
        testcase = self.input_testcase.text()
        coverage_enabled = self.coverage_checkbox.isChecked()
        info = tool.run(self.text, program, testcase, coverage_enabled, src)
        if info != '':
            _info("错误", info)

    def back_button_clicked(self):
        pass