#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Tools.py
# @Author: MoonKuma
# @Date  : 2018/10/8
# @Desc  : Some tools

import time


def simulate_switch(test_value, accept_value, func, *args, **kwargs):
    # *args is used for sending in tuple (which will be regarded as one arguments, and hence require further dissection
    # like xxx = args[0], xxxx = args[1], or for value in args,...)
    # **kwargs is used to identify each variable specified by their name like dict = my_dict, trans = my_trans
    if test_value == accept_value:
            func(*args, **kwargs)


def system_time():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))



