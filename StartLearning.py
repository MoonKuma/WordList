#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : StartLearning.py
# @Author: MoonKuma
# @Date  : 2018/10/8
# @Desc  : Entrance of all functions:
#          [1]. Set file patten
#          [2]. Recall (press [enter] within limited time)
#          [3]. Single choice([A]:meaning1,[B]:meaning2, [C]:meaning3, [D]:meaning4)
#          [4]. Flashcard([H]:hold, [H]:pass)
#          [5]. Report result([T]total,[C]current)
#          [6]. Quit(([Y/N]))

from utils import EasyInput, WordListFile
from utils.Tools import simulate_switch, system_time
from recall import recall


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
        message = '****Main Function Panel****\n***Select a function***\n*[1].Set file patten\n*[2].Recall\n*[3].Report\n*[4].Save&Quit\n'
        while True:
            answer = self.easy_input.input_and_check(message, acceptable_input, 0)
            simulate_switch(answer, '1', self.set_file_patten)
            simulate_switch(answer, '2', self.recall_test)
            simulate_switch(answer, '3', self.report_current_result)
            simulate_switch(answer, '4', self.save_and_quit)
            if answer == '4':
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
                self.__report_result(self.word_dict_tmp, 'Current test result')
                self.word_length = new_num
                self.recall_time_limit = new_time
            else:
                break
        pass

    def report_current_result(self):
        # report results from word_dict_tmp
        message = '***Select a result to report***\n*[1]. Current test\n*[2]. Total condition\n*[3]. Return\n'
        acceptable_input = ['1', '2', '3']
        while True:
            answer = self.easy_input.input_and_check(message, acceptable_input, 0)
            simulate_switch(answer, '1', self.__report_result, report_word_dict=self.word_dict_tmp, message='Result for current test')
            simulate_switch(answer, '2', self.__report_result, report_word_dict=self.word_dict, message='Result for total test')
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
    def __report_result(self, report_word_dict, message):
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
        [length, untested, passed, accuracy_dict, incorrect_list] = self.__dict_detail(report_word_dict)
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
        for word in incorrect_list:
            test_time = report_word_dict[word]['test_times']
            accuracy = 0
            if test_time != 0:
                accuracy = int(100*report_word_dict[word]['correct_times']/float(test_time))
            msg += str(word) + ':' + self.word_dict[word]['trans'] + '(' + str(accuracy) + '%)\n'
        print(msg)
        accept_list = ['Enter']
        msg = 'Press [Enter] to continue...\n'
        self.easy_input.input_and_check(msg, accept_list, 0)
        msg = '**************************************'
        print(msg)
        return 1

    def __get_legal_file_patten(self):
        # legal file pattens in resource
        return self.file_reader.get_current_pattens()

    def __load_word_dict(self):
        self.file_reader.set_file_patten(self.file_patten)
        return self.file_reader.open_latest_file()

    def __save_word_dict(self):
        self.file_reader.save_test_result(self.word_dict)

    def __dict_detail(self, word_dict):
        # word, trans, status(1 = pass, 0 = not pass), test_times, correct_times
        length = 0
        untested = 0
        passed = 0
        accuracy_dict = dict()  # 0%, 0%~25%, 25%~50%, 50%~75%, 75%~100%, 100%
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


# test
if __name__ == '__main__':
    StartLearning().main_screen_direct()









