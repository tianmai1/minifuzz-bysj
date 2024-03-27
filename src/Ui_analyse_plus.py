from PyQt5 import QtCore,QtWidgets
import os
import tools.tool as tool
from Ui_fuzz  import _info


current_dir = os.getcwd()
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
        self.input_analyse.setStyleSheet("QComboBox {"
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
        self.input_analyse.setMaxVisibleItems(3)
        self.input_analyse.setObjectName("input_analyse")
        self.input_analyse.addItem("")
        self.input_analyse.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(analyse_plus)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 160, 60, 30))
        self.pushButton_2.setObjectName("analyse")
        self.in_path_input = QtWidgets.QLineEdit(analyse_plus)
        self.in_path_input.setGeometry(QtCore.QRect(80, 10, 141, 30))
        self.in_path_input.setObjectName("in_path_input")
        self.cmd_input = QtWidgets.QLineEdit(analyse_plus)
        self.cmd_input.setGeometry(QtCore.QRect(80, 45, 141, 30))
        self.cmd_input.setObjectName("cmd_input")
        self.cmd = QtWidgets.QLabel(analyse_plus)
        self.cmd.setGeometry(QtCore.QRect(10, 45, 81, 30))
        self.cmd.setObjectName("cmd")
        self.out_path_input = QtWidgets.QLineEdit(analyse_plus)
        self.out_path_input.setGeometry(QtCore.QRect(80, 80, 141, 30))
        self.out_path_input.setObjectName("out_path_input")
        self.pushButton_3 = QtWidgets.QPushButton(analyse_plus)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 160, 60, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.crash_path_button = QtWidgets.QToolButton(analyse_plus)
        self.crash_path_button.setGeometry(QtCore.QRect(220, 15, 26, 24))
        self.crash_path_button.setObjectName("crash_path_button")
        self.out_path_button = QtWidgets.QToolButton(analyse_plus)
        self.out_path_button.setGeometry(QtCore.QRect(220, 85, 26, 24))
        self.out_path_button.setObjectName("out_path_button")
        self.program_path_button = QtWidgets.QToolButton(analyse_plus)
        self.program_path_button.setGeometry(QtCore.QRect(220, 50, 26, 24))
        self.program_path_button.setObjectName("program_path_button")

        self.in_path_input.setStyleSheet("font-size: 15px; color: #6effe8;")
        self.cmd_input.setStyleSheet("font-size: 15px; color: #6effe8;")
        self.out_path_input.setStyleSheet("font-size: 15px; color: #6effe8;")

        self.retranslateUi(analyse_plus)
        QtCore.QMetaObject.connectSlotsByName(analyse_plus)

    def retranslateUi(self, analyse_plus):
        _translate = QtCore.QCoreApplication.translate
        analyse_plus.setWindowTitle(_translate("analyse_plus", "analyse_plus"))
        self.in_path.setText(_translate("analyse_plus", "crash目录："))
        self.out_path.setText(_translate("analyse_plus", "输出目录："))
        self.show_txt_3.setText(_translate("analyse_plus", "类型:"))
        self.input_analyse.setItemText(0, _translate("analyse_plus", "崩溃分析"))
        self.input_analyse.setItemText(1, _translate("analyse_plus", "超时分析"))
        self.pushButton_2.setText(_translate("analyse_plus", "返回"))
        self.pushButton_2.clicked.connect(self.back_button_clicked)
        self.cmd.setText(_translate("analyse_plus", "运行命令："))
        self.pushButton_3.setText(_translate("analyse_plus", "确认"))
        self.pushButton_3.clicked.connect(self.button3_clicked)
        self.crash_path_button.setText(_translate("analyse_plus", "📂"))
        self.out_path_button.setText(_translate("analyse_plus", "📂"))
        self.program_path_button.setText(_translate("analyse_plus", "📂"))
        self.crash_path_button.clicked.connect(self.msg_crash)
        self.out_path_button.clicked.connect(self.msg_out)
        self.program_path_button.clicked.connect(self.msg_program)

    def msg_crash(self,Filepath):
        m = QtWidgets.QFileDialog.getExistingDirectory(None,"测试用例文件夹",current_dir)
        self.in_path_input.setText(m)

    def msg_out(self,Filepath):
        m = QtWidgets.QFileDialog.getExistingDirectory(None,"源码文件夹",current_dir)
        self.out_path_input.setText(m)

    def msg_program(self,Filepath):
        m = QtWidgets.QFileDialog.getOpenFileName(None,  "目标文件","./")
        self.cmd_input.setText(m[0])   

    def back_button_clicked(self):
        pass

    def button3_clicked(self):
        in_path = self.in_path_input.text()
        out_path = self.out_path_input.text()
        cmd = self.cmd_input.text()
        command=[]
        is_crash=False
        if not (in_path and out_path and cmd):
            _info("错误","选项不能为空")
            return
        if not os.path.isdir(in_path):
            _info("错误",in_path+"目录不存在 或 不是个目录")
            return
        in_files=tool.get_file_name(in_path)
        if len(in_files)==0:
            _info("错误",in_path+"目录没有文件")
            return
        if os.path.isdir(out_path) and len(tool.get_file_name(out_path)):
            _info("错误",out_path+"目录不为空")
            return
        if '@@' in cmd:
            os.makedirs(out_path,exist_ok=True)
            for in_file in in_files:
                command.append(cmd.replace("@@",os.path.join(in_path, in_file)))
            if self.input_analyse.currentText()=="崩溃分析":
                is_crash=True
            is_ok,e=tool.run_thread(command,out_path,is_crash)
            if is_ok:
                _info("成功","分析结束!")
            else:
                _info("错误",e)
        else:
            _info("错误","运行命令少了@@")
            return