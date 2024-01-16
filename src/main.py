import os
import shutil
import subprocess
from time import sleep
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QIcon, QPixmap,QRegExpValidator
import markdown
import psutil
import tools.tool as tool
from qt_material import apply_stylesheet
import webbrowser

from Ui_fuzz import Ui_fuzz,_info
from Ui_minifuzz import Ui_minifuzz
from Ui_new import Ui_new_2
from Ui_show import Ui_show
from Ui_analyse import Ui_analyse
from Ui_result import Ui_result




class fuzzPage(QWidget, Ui_fuzz):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def new_fuzz_page(self):
        self.name = self.input_name.text()
        test_list = tool.get_list()
        if not self.name:
            _info("错误", "名称不能为空")
            return
        if os.path.exists('out/'+self.name):
            _info("错误", "名称重复")
            return
        main_window.switch(1)

class newPage(QWidget, Ui_new_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def back_button_c(self):
        main_window.switch(0)

class showPage(QWidget, Ui_show):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def crash_show(self,type1:str):
        name=self.input_name.currentText()
        if not name:
            _info("错误","没有测试，请先新建一个测试")
            return
        self.crash_path='out/'+name+'/'+type1
        if os.path.exists(self.crash_path) and tool.get_md(self.crash_path):
            self.md_list=tool.get_md(self.crash_path)
            main_window.switch(4)
        else:
            _info("错误","此测试没有产生缺陷信息\n1.可能没有进行分析\n2.超时分析没有结果\n3.没有产生缺陷")

class analysePage(QWidget, Ui_analyse):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class resultPage(QWidget, Ui_result):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def back(self):
        main_window.switch(2)

bysj_path=os.path.dirname(os.path.abspath(__file__))

class MainWidget(QWidget, Ui_minifuzz):
    """
    主窗口
    """
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(bysj_path+"/tools/images/d.png"))
        self.setupUi(self)
        # 实例化一个堆叠布局
        self.qsl = QStackedLayout(self.frame)
        # 实例化分页面
        self.fuzz_page = fuzzPage()
        self.new_page = newPage()
        self.show_page = showPage()
        self.analyse_page = analysePage()
        self.result_page = resultPage()
        
        self.qsl.addWidget(self.fuzz_page)
        self.qsl.addWidget(self.new_page)
        self.qsl.addWidget(self.show_page)
        self.qsl.addWidget(self.analyse_page)
        self.qsl.addWidget(self.result_page)
        self.controller()

    def controller(self):
        self.fuzz.clicked.connect(self.switch)
        self.show1.clicked.connect(self.switch)
        self.analyse.clicked.connect(self.switch)


    def switch(self,ind):
        self.show_page.shuaxin()
        self.analyse_page.shuaxin()
        sender = self.sender().objectName()
        index = {
            "fuzz": 0,
            "show1": 2,
            "analyse": 3,
        }
        # print(ind)
        if ind==1:
            self.new_page.get_text(self.fuzz_page.name)
            self.qsl.setCurrentIndex(ind)
        elif ind==4:
            self.result_page.get_md_list(self.show_page.md_list)
            self.result_page.get_crash_path(self.show_page.crash_path)
            self.result_page.shuaxin()
            self.qsl.setCurrentIndex(ind)
        else:
            self.qsl.setCurrentIndex(index[sender])

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    main_window = MainWidget()
    main_window.show()

    app.exec_()