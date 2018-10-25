#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : StartLearning.py
# @Author: MoonKuma
# @Date  : 2018/10/8
# @Desc  : Entrance of all functions:
#          [1]. Set file patten
#          [2]. Recall (press [enter] within limited time)
#          [3]. Multiple-choice(select 1/4 meanings)
#          [3]. Report result(total/current)
#          [4]. Quit

from utils import EasyInput, WordListFile
from utils.Tools import simulate_switch
from recall import recall
from report import report_result
import platform
system_type = platform.system()
if system_type == 'Linux':
    import io
    import sys
    msg = '[Caution] You are running this on a linux system, the speed will be relative slow for tampering with the standard output'
    print(msg)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # necessary for printing chinese characters in Linux

class StartLearning(object):

    def __init__(self):
        # local parameters
        self.resource_path = './resource'
        self.word_dict = dict()  # original word list
        self.word_dict_tmp = dict()  # empty word list for recording and reporting performance each time
        self.word_length = 10
        self.pass_rate = 0.8
        self.recall_time_limit = 3
        # functions
        self.file_reader = WordListFile.WordListFile(self.resource_path)
        self.easy_input = EasyInput.EasyInput()
        # initial
        self.file_patten = 'gre_word'
        self.word_dict = self.__load_word_dict()

        return

    def main_screen_direct(self):
        acceptable_input = ['1', '2', '3', '4', '5', '6']
        message = '****Main Function Panel****\n***Select a function***\n*[1].Set file patten\n*[2].Recall\n*[3].Multiple-choice\n*[4].Report\n*[5].Save&Quit\n'
        while True:
            answer = self.easy_input.input_and_check(message, acceptable_input, 0)
            simulate_switch(answer, '1', self.set_file_patten)
            simulate_switch(answer, '2', self.recall_test)
            simulate_switch(answer, '3', self.multiple_choice_test)
            simulate_switch(answer, '4', self.report_current_result)
            simulate_switch(answer, '5', self.save_and_quit)
            if answer == '5':
                break
        msg = 'Thanks for participant'
        print(msg)
        return 0

    def set_file_patten(self):
        # set file patten
        print_msg = 'Current patten: ' + self.file_patten
        print(print_msg)
        patten_list = self.__get_legal_file_patten()
        accept_list = list()
        message = '***Select a patten***\n'
        patten_num = 1
        for patten in patten_list:
            message += '*[' + str(patten_num) + '].' + patten + '*\n'
            accept_list.append(str(patten_num))
        file_patten_num = self.easy_input.input_and_check(message, accept_list, 0)
        self.file_patten = patten_list[int(file_patten_num) - 1]
        print_msg = 'Current patten: ' + self.file_patten
        print(print_msg)
        self.word_dict = self.__load_word_dict()
        return 0

    def recall_test(self):
        # recall test
        message = '***Start a recall test, Continue?***\n*[Enter]. Yes\n*[R]. Return\n'
        acceptable_input = ['Enter', 'R']
        while True:
            answer = self.easy_input.input_and_check(message, acceptable_input, 0)
            if answer == 'Enter':
                [new_num, new_time] = recall(self.word_dict, self.word_dict_tmp, self.word_length, self.pass_rate, self.recall_time_limit)
                report_result(self.word_dict_tmp, self.word_dict, 'Current test result')
                self.word_length = new_num
                self.recall_time_limit = new_time
            else:
                break
        pass

    def multiple_choice_test(self):
        # multiple_choice_test
        print('Nothing happens here')
        pass


    def report_current_result(self):
        # report results from word_dict_tmp
        message = '***Select a result to report***\n*[1]. Current test\n*[2]. Total condition\n*[3]. Return\n'
        acceptable_input = ['1', '2', '3']
        while True:
            answer = self.easy_input.input_and_check(message, acceptable_input, 0)
            simulate_switch(answer, '1', report_result, report_word_dict=self.word_dict_tmp, total_word_dict=self.word_dict, message='Result for current test')
            simulate_switch(answer, '2', report_result, report_word_dict=self.word_dict, total_word_dict=self.word_dict, message='Result for total test')
            if answer == '3':
                break
        return 1

    def save_and_quit(self):
        # quit
        msg = '****Save and quit now!****\n****Thanks for participating!****'
        print(msg)
        self.__save_word_dict()
        return 1


    # private methods:
    def __get_legal_file_patten(self):
        # legal file pattens in resource
        return self.file_reader.get_current_pattens()

    def __load_word_dict(self):
        self.file_reader.set_file_patten(self.file_patten)
        return self.file_reader.open_latest_file()

    def __save_word_dict(self):
        self.file_reader.save_test_result(self.word_dict)


# test
if __name__ == '__main__':
    StartLearning().main_screen_direct()









