#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : EasyFile.py
# @Author: MoonKuma
# @Date  : 2018/10/8
# @Desc  : Easy file read/write


import os


class EasyFile(object):

    def __init__(self):
        return

    def current_path(self):
        return os.path.abspath('.')

    def current_file_list(self):
        return os.listdir('.')

    def get_file_list(self, relative_path):
        return os.listdir(relative_path)

    def get_file_head(self, file_name):
        return file_name[0:file_name.rfind('.')]

    def get_file_type(self, file_name):
        return file_name[file_name.rfind('.'):]

    def file_not_exist(self, file_name):
        return not os.path.exists(file_name)
