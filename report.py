#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : report.py
# @Author: MoonKuma
# @Date  : 2018/10/24
# @Desc  : report result

import time
import collections
from utils.Tools import system_time
import utils.EasyInput as EasyInput

def report_result(report_word_dict, total_word_dict, message):
    # --Sample--
    # Title : 'Report results about current test'
    # Report time : 2018-10-12 17:50:22
    # Total words : 100
    # Accuracy Table:
    #     0% : 14(14%)
    #     0%~25% : 27(27%)
    #     25%~50% : 11(11%)
    #     50%~75% : 15(15%)
    #     75%~100% : 10(10%)
    #     100% : 23(23%)
    # Worst top 20:
    #     AddProp 增加道具
    #     AddShip 添加战舰
    #     AddVipExp 增加Vip经验
    msg = '**************************************'
    print(msg)
    msg = 'Title: ' + message
    print(msg)
    msg = 'Report time: ' + system_time()
    print(msg)
    [length, untested, passed, accuracy_dict, incorrect_list] = __dict_detail(report_word_dict)
    msg = 'Total words: ' + str(length)
    print(msg)
    msg = 'Untested words: ' + str(untested)
    print(msg)
    msg = 'Passed words: ' + str(passed)
    print(msg)
    msg = 'Accuracy: \n'
    for rate in accuracy_dict:
        msg = msg + str(rate) + ' : ' + str(accuracy_dict[rate]) + '\n'
    print(msg)
    msg = 'Top incorrect: \n'
    print(msg)
    for word in incorrect_list:
        test_time = report_word_dict[word]['test_times']
        accuracy = 0
        if test_time != 0:
            accuracy = int(100 * report_word_dict[word]['correct_times'] / float(test_time))
        msg = str(word) + ':' + total_word_dict[word]['trans'] + '(' + str(accuracy) + '%)'
        print(msg)
        time.sleep(0.1)
    accept_list = ['Enter']
    msg = 'Press [Enter] to continue...\n'
    EasyInput.EasyInput().input_and_check(msg, accept_list, 0)
    msg = '**************************************'
    print(msg)
    return 1


def __dict_detail(word_dict):
    # word, trans, status(1 = pass, 0 = not pass), test_times, correct_times
    length = 0
    untested = 0
    passed = 0
    accuracy_dict = collections.OrderedDict()  # 0%, 0%~25%, 25%~50%, 50%~75%, 75%~100%, 100%
    tmp_acc_dict = dict()
    incorrect_list = list()
    for word in word_dict:
        length += 1
        if word_dict[word]['status'] == 1:
            passed += 1
        if word_dict[word]['test_times'] == 0:
            untested += 1
        else:
            accuracy = float(word_dict[word]['correct_times'])/word_dict[word]['test_times']
            if accuracy == 0:
                accuracy_dict['%0'] = accuracy_dict.setdefault('%0',0) + 1
            if 0.25 >= accuracy > 0:
                accuracy_dict['0%~25%'] = accuracy_dict.setdefault('0%~25%',0) + 1
            if 0.5 >= accuracy > 0.25:
                accuracy_dict['25%~50%'] = accuracy_dict.setdefault('25%~50%',0) + 1
            if 0.75 >= accuracy > 0.5:
                accuracy_dict['50%~75%'] = accuracy_dict.setdefault('50%~75%',0) + 1
            if 1 > accuracy > 0.75:
                accuracy_dict['50%~75%'] = accuracy_dict.setdefault('50%~75%',0) + 1
            if accuracy == 1:
                accuracy_dict['100%'] = accuracy_dict.setdefault('100%',0) + 1
            if accuracy < 1:
                incorrect_list.append(word)
            tmp_acc_dict[word] = accuracy
    incorrect_list = sorted(incorrect_list, key=lambda x:tmp_acc_dict.setdefault(x, 0))
    if len(incorrect_list) > 20:
        incorrect_list = incorrect_list[0:20]
    return [length, untested, passed, accuracy_dict, incorrect_list]