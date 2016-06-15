# -*- coding: utf-8 -*-

import os

from flask import Flask


def walk_dir(_dir, )

def walk_dir(_dir, file_info, top_down=True):
    for root, dirs, files in os.walk(_dir, top_down):
        for name in files:
            print(os.path.join(name))
            file_info.write(os.path.join(root, name) + '\n')
        for name in dirs:
            print(os.path.join(name))
            file_info.write(' ' + os.path.join(root, name) + '\n')
        _dir = raw_input('please input the path:')
    _dir = r'G:\codes\python\file_info'
    file_info = open('list2.txt', 'w')
    walk_dir(_dir, file_info)
    file_info.close()

app = Flask(__name__)

# 根据包名注册蓝图，迭代注册蓝图，除了common包之外
modules = []