from PyQt5 import QtCore, QtGui, QtWidgets
import os
import tools.tool as tool
from Ui_fuzz  import _info

bysj_path=os.path.dirname(os.path.abspath(__file__))
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
        self.input_name.addItems(tool.get_name())
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
        self.input_num = QtWidgets.QSpinBox(analyse)
        self.input_num.setGeometry(QtCore.QRect(130, 50, 111, 35))
        self.input_num.setObjectName("input_num")
        self.input_num.setMinimum(1)
        self.input_num.setMaximum(20)
        self.input_num.setSingleStep(2)
        self.input_num.setStyleSheet("color: #6effe8;")
        default_value = 4
        self.input_num.setValue(default_value)
        self.show_txt_3 = QtWidgets.QLabel(analyse)
        self.show_txt_3.setGeometry(QtCore.QRect(10, 90, 51, 35))
        self.show_txt_3.setObjectName("show_txt_3")
        self.input_analyse = QtWidgets.QComboBox(analyse)
        self.input_analyse.setGeometry(QtCore.QRect(90, 90, 151, 35))
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
        self.pushButton_2 = QtWidgets.QPushButton(analyse)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 150, 61, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(analyse)
        self.label.setGeometry(QtCore.QRect(-5, 100, 111, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(bysj_path+"/tools/images/兴奋.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(analyse)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 150, 61, 30))
        self.pushButton_3.setObjectName("analyse_plus")

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
        self.pushButton_2.clicked.connect(self.pushButton_clicked)
        self.pushButton_3.setText(_translate("analyse", "高级"))
        self.pushButton_3.clicked.connect(self.analyse_plus_clicked)

    def analyse_plus_clicked(self):
        pass

    def pushButton_clicked(self):
        name=self.input_name.currentText()
        if not name:
            _info("错误","请先新建一个测试")
            return
        txt=self.input_analyse.currentText()
        if txt=="崩溃分析":
            self.crash_analyse(name)
        elif txt=="超时分析":
            self.hangs_analyse(name)

    def crash_analyse(self,name):
        num = self.input_num.value()
        title,info=tool.crash_analyzed(name,num,"crashes")
        _info(title,info)
        pass

    def hangs_analyse(self,name):
        num = self.input_num.value()
        title,info=tool.crash_analyzed(name,num,"hangs")
        _info(title,info)
        pass

    def shuaxin(self):
        self.input_name.clear()
        self.input_name.addItems(tool.get_name())
