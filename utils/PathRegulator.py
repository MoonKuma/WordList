#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : PathRegulator.py
# @Author: MoonKuma
# @Date  : 2018/11/22
# @Desc  : show path structure and so on

import os


def show_path_structure(path_local, current_level=0):
    level_str = ''
    for i in range(0, current_level):
        level_str = level_str + '--'
    if os.path.exists(path_local):
        dir_list = os.listdir(path_local)
        dir_list = sorted(dir_list)
        for dir_name in dir_list:
            msg = level_str + dir_name
            print(msg)
            new_path = path_local + '/' + dir_name
            if os.path.isdir(new_path) and dir_name != ".svn" and dir_name != ".idea":
                show_path_structure(new_path, current_level+1)
    else:
        msg = '[Error]path: ' + str(path_local) + ' not exists'
        print(msg)


# test main
if __name__ == '__main__':
    show_path_structure('E:\\战争策略组运营工作\\现代海战\\数据分析\\数据统计标准化工作文档', 0)

