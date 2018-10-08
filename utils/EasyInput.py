#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : EasyInput.py
# @Author: MoonKuma
# @Date  : 2018/10/8
# @Desc  : Accept keyboard input and check correctness

import threading

class EasyInput(object):

    def __init__(self):
        return

    def input_and_check(self, input_str, accept_list, *time_limit):
        if len(time_limit) > 0 and int(time_limit[0]) > 0:
            self.__input_and_check_thread(input_str, accept_list, int(time_limit[0]))
        else:
            receive_str = raw_input(input_str)
            while True:
                if not self.__accept(accept_list, receive_str):
                    string = 'Input not acceptable. Legal input includes:' + accept_list[0]
                    if len(accept_list) > 1:
                        for index in range(1, len(accept_list)):
                            string = string + ',' + str(accept_list[index])
                    print(string)
                    receive_str = raw_input(input_str)
                else:
                    break
            return receive_str

    def __input_and_check_thread(self, input_str, accept_list, time):
        return

    def __accept(self, accept_list, test_word):
        test_word = test_word.lower()
        for word in accept_list:
            if test_word == word.lower():
                return True
        return False


# test
if __name__ == '__main__':
    obj = EasyInput()
    word_dict = obj.input_and_check('test input:\n', ['A', 'b', 'c'])
