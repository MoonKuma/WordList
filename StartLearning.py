#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : StartLearning.py
# @Author: MoonKuma
# @Date  : 2018/10/8
# @Desc  : Entrance of all functions:
#          [1]. Set file patten
#          [2]. Recall ([A]: know, [B]:forget)
#          [3]. Single choice([A]:meaning1,[B]:meaning2, [C]:meaning3, [D]:meaning4)
#          [4]. Flashcard([H]:hold, [H]:pass)
#          [5]. Report result([T]total,[C]current)
#          [6]. Quit(([Y/N]))

from utils import EasyInput, WordListFile


class StartLearning(object):

    def __init__(self):
        # local parameters
        self.resource_path = '.resource/'
        self.word_dict = dict()  # original word list
        self.word_dict_tmp = dict()  # empty word list for recording and reporting performance each time
        self.file_patten = 'test_word_list'
        # initial
        self.file_reader = WordListFile.WordListFile(self.resource_path)
        return

    def topic_direct(self):
        # first UI interface
        pass

    def set_file_patten(self):
        # set file patten
        pass

    def report_current_result(self):
        # report results from word_dict_tmp
        pass

    # private methods:
    def __get_legal_file_patten(self):
        # legal file pattens in resource
        return self.file_reader.get_current_pattens()

    def __load_word_dict(self):
        self.file_reader.set_file_patten(self.file_patten)
        return self.file_reader.open_latest_file()

    def __save_word_dict(self):
        self.file_reader.save_test_result(self.word_dict)

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
        pass