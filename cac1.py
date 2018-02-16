# import requests
# import selenium
# from bs4 import BeautifulSoup
# import sys
# import pprint
# from pydash import py_
# from threading import Timer
# import time
# import datetime
# import inspect
# import subprocess
# import select
# from splinter import Browser
# import re
# from pathlib import Path
# from enum import Enum
# import os
# import random, string
# from slugify import slugify
# import hashlib

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout, QVBoxLayout, QTextEdit,
                             QPushButton, QFormLayout, QLineEdit, QApplication)

# from splinter.exceptions import ElementDoesNotExist
#
# from captcha_solver import CaptchaSolver



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        vbox = QVBoxLayout()

        fbox = QFormLayout()


        lbl = QLabel(self)
        lbl.setText('qq')
        self.captcha_apikey_edit = QLineEdit(self)

        fbox.addRow(lbl, self.captcha_apikey_edit)


        lbl = QLabel(self)
        lbl.setText('qq12')
        self.num = QLineEdit(self)

        fbox.addRow(lbl, self.num)


        vbox.addLayout(fbox)


        self.start_btn = QPushButton('Start!', self)
        self.start_btn.clicked[bool].connect(self.run)

        vbox.addWidget(self.start_btn)


        self.log_area = QTextEdit()

        vbox.addWidget(self.log_area)


        self.setLayout(vbox)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()


    def run(self):
        self.log_area.append('Azaza')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())