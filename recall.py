#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : recall.py
# @Author: MoonKuma
# @Date  : 2018/10/17
# @Desc  : Recall test

from utils.generate_test_list import generate_test_list
from utils.record_result import record_result
from utils.EasyInput import EasyInput
from utils.Tools import simulate_switch
import re
import time

test_word_num = 0
test_time_length = 1
input_unit = EasyInput()
count = 1

def recall(total_word_dict, current_word_dict, test_num, pass_rate, recall_time_limit):
    global test_word_num
    global test_time_length
    global input_unit
    global count
    count = 1
    test_word_num = test_num
    test_time_length = recall_time_limit
    msg = 'You need to press Enter in less than ' + str(recall_time_limit) + ' second(s) to confirm recognition of each word'
    print(msg)
    msg = 'Anticipated test words number:' + str(test_word_num)
    print(msg)
    accept_list = ['Enter', '1', '2']
    msg = 'Press [Enter] to start...\n[1].Reset numbers of words, [2].Reset time limit\n'
    while True:
        answer = input_unit.input_and_check(msg, accept_list, 0)
        simulate_switch(answer, '1', __reset_num, max_number=len(total_word_dict.keys()))
        simulate_switch(answer, '2', __reset_time)
        if answer == 'Enter':
            break
    current_word_list = generate_test_list(total_word_dict, test_word_num)
    msg = 'Start recall test with ' + str(len(current_word_list)) + ' words.'
    print(msg)
    for word in current_word_list:
        result = __recall_test(total_word_dict, word, test_time_length)
        record_result(word, result, current_word_dict, total_word_dict, pass_rate)
    msg = 'You have finished! press [Enter] to continue...\n'
    input_unit.input_and_check(msg, accept_list, 0)
    return [test_word_num, test_time_length]

def __recall_test(total_word_dict, word, recall_time_limit):
    global input_unit
    global count
    accept_list = ['Enter']
    msg = '--(ready)--' + str(count) + '--'
    print(msg)
    count += 1
    time.sleep(0.5)
    msg = word
    answer = input_unit.input_and_check(msg, accept_list, 'Delay', recall_time_limit)
    if answer == 'Enter':
        msg = '[v]:' + word + ':' + total_word_dict[word]['trans']
        print(msg)
        return 1
    elif answer == 'Delay':
        msg = '[x]:' + word + ':' + total_word_dict[word]['trans']
        while True:
            answer = input_unit.input_and_check(msg, accept_list, '0')
            if answer == 'Enter':
                break
        return 0


def __reset_num(max_number):
    global test_word_num
    global input_unit
    pattern = re.compile(r'^[1-9]+[0-9]?$')
    msg = 'Set new test number (max ' + str(max_number) + ')\n'
    answer = input_unit.input_without_check(msg)
    if pattern.match(answer):
        if int(answer) > max_number:
            answer = max_number
        test_word_num = int(answer)
        msg = 'Succeed! Test numbers reset to ' + str(test_word_num)
        print(msg)
        return
    else:
        print('Input is not a number')


def __reset_time():
    global test_word_num
    global test_time_length
    global input_unit
    pattern = re.compile(r'^[0-9]+\.[0-9]+$')
    answer = input_unit.input_without_check('Set new test time (max 10)\n')
    if pattern.match(answer):
        if float(answer) > 10:
            answer = 10
        test_time_length = float(answer)
        msg = 'Succeed! Test time reset to ' + str(test_time_length)
        print(msg)
        return
    else:
        print('Input is not a number')