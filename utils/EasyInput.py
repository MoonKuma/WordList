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
        return_list = list()
        if len(time_limit) > 0 and int(time_limit[0]) > 0:
            pass
            # return self.__input_and_check_hold(input_str, accept_list, int(time_limit[0]))
        else:
            return self.__input(input_str, accept_list, return_list)

    def __input_and_check_hold(self, input_str, accept_list, time):
        # no longer used
        # thread could be used to end function but unable to escape from the input gui
        return_list = list()
        t = threading.Thread(target=self.__input, args=(input_str, accept_list, return_list, ))
        t.start()
        t.join(time)
        if len(return_list) == 0:
            log = 'Time out, limited time:' + str(time)
            print(log)
            return False
        else:
            return return_list[0]

    def __accept(self, accept_list, test_word):
        test_word = test_word.lower()
        for word in accept_list:
            if test_word == word.lower():
                return True
        return False

    def __input(self, input_str, accept_list, return_list):
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
        return_list.append(receive_str)
        return receive_str


# test
if __name__ == '__main__':
    obj = EasyInput()
    word_dict = obj.input_and_check('test input:\n', ['A', 'b', 'c'], 10)
