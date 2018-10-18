#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : record_result.py
# @Author: MoonKuma
# @Date  : 2018/10/17
# @Desc  : record test result


def record_result(word, result, current_dict, total_word_dict, pass_rate):
    # change counts
    # word, trans, status(1 = pass, 0 = not pass), test_times, correct_times
    if word not in current_dict:
        current_dict[word] = dict()
    current_dict[word]['test_times'] = current_dict[word].setdefault('test_times', 0) + 1
    total_word_dict[word]['test_times'] = total_word_dict[word].setdefault('test_times', 0) + 1
    current_dict[word]['correct_times'] = current_dict[word].setdefault('correct_times', 0)
    total_word_dict[word]['correct_times'] = total_word_dict[word].setdefault('correct_times', 0)
    current_dict[word]['status'] = current_dict[word].setdefault('status', 0)
    total_word_dict[word]['status'] = total_word_dict[word].setdefault('status', 0)
    if result == 1:
        current_dict[word]['correct_times'] = current_dict[word].setdefault('correct_times', 0) + 1
        total_word_dict[word]['correct_times'] = total_word_dict[word].setdefault('correct_times', 0) + 1
    # sift pass
    pass_rate1 = float(current_dict[word]['correct_times'])/current_dict[word]['test_times']
    pass_rate2 = float(total_word_dict[word]['correct_times'])/total_word_dict[word]['test_times']
    if current_dict[word]['test_times'] > 10 and pass_rate1 > pass_rate:
        current_dict[word]['status'] = 1
    if total_word_dict[word]['test_times'] > 20 and pass_rate2 > pass_rate:
        total_word_dict[word]['status'] = 1
    return 1
