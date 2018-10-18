#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : recall.py
# @Author: MoonKuma
# @Date  : 2018/10/17
# @Desc  : Recall test

from utils.generate_test_list import generate_test_list
from utils.record_result import record_result
from utils.EasyInput import EasyInput


def recall(total_word_dict, current_word_dict, test_num, pass_rate, recall_time_limit):
    input_unit = EasyInput()
    current_word_list = generate_test_list(total_word_dict, test_num)
    msg = 'Start recall test with ' + str(len(current_word_list)) + ' words.'
    print(msg)
    msg = 'You need to press Enter in less than ' + str(recall_time_limit) + ' second(s) to confirm recognition of each word'
    print(msg)
    accept_list = ['Enter']
    msg = 'Press [Enter] to start...\n'
    input_unit.input_and_check(msg, accept_list, 0)
    for word in current_word_list:
        result = recall_test(total_word_dict, word, input_unit, recall_time_limit)
        record_result(word, result, current_word_dict, total_word_dict, pass_rate)
    msg = 'You have finished! press [Enter] to continue...\n'
    input_unit.input_and_check(msg, accept_list, 0)

def recall_test(total_word_dict, word, input_unit, recall_time_limit):
    accept_list = ['Enter']
    msg = word + '\n'
    answer = input_unit.input_and_check(msg, accept_list, 'Delay', recall_time_limit)
    if answer == 'Enter':
        return 1
    elif answer == 'Delay':
        msg = word + ':' + total_word_dict[word]['trans'] + '\n'
        while True:
            answer = input_unit.input_and_check(msg, accept_list, '0')
            if answer == 'Enter':
                break
        return 0