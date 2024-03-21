# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tianmai/workspace/bysj_plus/ui/fuzz.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


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

bysj_path=os.path.dirname(os.path.abspath(__file__))
class Ui_fuzz(object):
    def setupUi(self, fuzz):
        fuzz.setObjectName("fuzz")
        fuzz.resize(250, 200)
        back_button = QPushButton()
        back_button.setIcon(QIcon(bysj_path+"/tools/images/返回.png"))
        back_button.setFixedSize(20,20)
        # back_button.clicked.connect(self.back_button_clicked)
        label = QLabel()
        pixmap = QPixmap(bysj_path+'/tools/images/讨论.png')
        # 调整图片尺寸
        shu = pixmap.scaled(150, 100, Qt.KeepAspectRatio)  
        label.setPixmap(shu)

        test_name = QLabel("请输入测试名称:")
        self.input_name = QLineEdit()
        regex = QRegExp("[A-Za-z0-9_]+")
        validator = QRegExpValidator(regex)
        self.input_name.setValidator(validator)
        self.input_name.setStyleSheet("font-size: 15px; color: #6effe8;")
        completer = QCompleter(tool.get_name())
        self.input_name.setCompleter(completer)

        # 设置选项的样式表，将字体颜色设置为青色
        completer.popup().setStyleSheet("color: #6effe8;")
        # self.input_name.setFixedHeight(30)
        new_fuzz = QPushButton('新建')
        new_fuzz.setStyleSheet("color: #00FF00; border-color: #00FF00")
        continue_fuzz = QPushButton('继续')
        continue_fuzz.setStyleSheet("color: #FFD700; border-color: #FFD700")
        stop_fuzz = QPushButton('停止')
        stop_fuzz.setStyleSheet("color: #FFA500; border-color: #FFA500")
        dele_fuzz = QPushButton('删除')
        dele_fuzz.setStyleSheet("color: #FF0000; border-color: #FF0000")

        new_fuzz.clicked.connect(self.new_fuzz_page)
        continue_fuzz.clicked.connect(self.continue_fuzz_page)
        stop_fuzz.clicked.connect(self.stop_fuzz_page)
        dele_fuzz.clicked.connect(self.dele_fuzz_page)

        layout1 = QHBoxLayout()
        layout1.addWidget(new_fuzz)
        layout1.addWidget(continue_fuzz)
        layout2 = QHBoxLayout()
        layout2.addWidget(stop_fuzz)
        layout2.addWidget(dele_fuzz)

        layout3 = QVBoxLayout()
        # layout3.addWidget(back_button)
        layout3.addWidget(test_name)
        layout4 = QHBoxLayout()
        layout4.addLayout(layout3)
        layout4.addWidget(label)

        layout = QVBoxLayout()
        
        layout.addLayout(layout4)
        layout.addWidget(self.input_name)
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        # layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

    def new_fuzz_page(self):
        pass
    
    def continue_fuzz_page(self):
        name = self.input_name.text()
        if not name:
            _info("错误", "名称不能为空")
            return
        test_list = tool.get_list()
        if not name in test_list:
            if os.path.exists('out/'+name):
                stats = 'out/'+name+'/default/fuzzer_stats'
                if os.path.exists(stats):
                    with open(stats, "r") as fd:
                        lines = fd.readlines()
                        cmd = lines[-1].split(" -- ")[1]
                        tool.run(name, cmd, '-', False, '.', False)
                    return
                else:
                    _info("错误", "请查看 "+stats+' 是否存在')
                    return
            else:
                _info("错误", "没有这个测试,请新建一个")
                return
        else:
            _info("提示", "请先停止测试")
            return

    def stop_fuzz_page(self):
        name = self.input_name.text()
        if not name:
            _info("错误", "名称不能为空")
            return
        test_list = tool.get_list()
        if not name in test_list:
            if os.path.exists('out/'+name):
                _info("提示", "此测试已停止")
                return
            else:
                _info("错误", "没有这个测试,请新建一个")
                return
        stats = 'out/'+name+'/default/fuzzer_stats'
        if os.path.exists(stats):
            with open(stats, "r") as fd:
                lines = fd.readlines()
                afl_pid = int(lines[3].split(":")[1])
                if not psutil.pid_exists(int(afl_pid)):
                    _info("提示", "稍等，正在计算覆盖率")
                    return
                try:
                    # subprocess.run(['kill', str(afl_pid)])
                    subprocess.run(['tmux', 'kill-window', '-t', name])
                    sleep(1)
                    tool.cov_analyse(name)
                except Exception as e:
                    print(e)
                    return
    
        else:
            _info("错误", "请查看 "+stats+' 是否存在')
        return

    def dele_fuzz_page(self):
        name = self.input_name.text()
        if not name:
            _info("错误", "名称不能为空")
            return
        test_list = tool.get_list()
        if name in test_list:
            try:
                subprocess.run(['tmux', 'kill-window', '-t', name])
                sleep(1)
            except Exception as e:
                print(e)
                return
        if os.path.exists('out/'+name):
            try:
                shutil.rmtree('out/'+name)
                _info("提示", "删除成功")
            except Exception as e:
                _info("错误", e)
        else:
            _info("提示", "此测试不存在")
        return

def _info(title, text):
    window = QWidget()
    button=QPushButton('OK')
    button.setFixedSize(60,30)
    tishi=QMessageBox(window)
    if title=='错误':
        tishi.setText("<font color='#ff0000'>"+text+"</font>")
    elif title=='成功':
        tishi.setText("<font color='#00FF00'>"+text+"</font>")
    else:
        tishi.setText("<font color='#FFA500'>"+text+"</font>")
    
    tishi.setWindowTitle(title)
    # tishi.addButton(button, QMessageBox.AcceptRole)
    if len(text)<50:
        tishi.setIcon(QMessageBox.Information)
    # 设置消息框的按钮
    tishi.setStandardButtons(QMessageBox.Ok)
    # 设置消息框的默认按钮
    tishi.setDefaultButton(QMessageBox.Ok)
    tishi.exec_()
    return