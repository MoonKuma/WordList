#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : generate_test_list.py
# @Author: MoonKuma
# @Date  : 2018/10/17
# @Desc  : generate test list based on value of each words

import random


def generate_test_list(word_dict, list_length):
    # word, trans, status(1 = pass, 0 = not pass), test_times, correct_times
    word_list = list()
    len_word = len(word_dict.keys())
    if len_word <= list_length:
        msg = 'Current length of word dict:' + str(len_word) + ' is smaller than ' + str(list_length) +  ', all words will be tested this time'
        print(msg)
        for word in word_dict.keys():
            word_list.append(word)
        return word_list
    else:
        # 80% from the lowest value
        # 20% from random select
        num2 = int(list_length*0.2)
        num1 = list_length - num2
        value_dict = dict()
        for word in word_dict.keys():
            value = word_value(word_dict[word])
            value_dict[word] = value
            word_list.append(word)
        word_list = sorted(word_list, key=lambda x:value_dict[x])
        word_list = word_list[0:num1]
        rest_list = list()
        for word in word_dict.keys():
            if word not in word_list:
                rest_list.append(word)
        random.shuffle(rest_list)
        rest_list = rest_list[0:num2]
        sum_list = word_list + rest_list
        return sum_list


def word_value(word_detail_dict):
    value = 0
    status = word_detail_dict['status']
    test_times = word_detail_dict['test_times']
    correct_times = word_detail_dict['correct_times']
    if status == 1:
        value = 1
    elif test_times == 0:
        value = 0.5
    elif test_times > 0:
        value = float(correct_times)/test_times
    return value
