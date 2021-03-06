#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : WordListFile.py
# @Author: MoonKuma
# @Date  : 2018/10/8
# @Desc  : Open/Save file list

from utils.EasyFile import EasyFile
import time
import copy


class WordListFile(EasyFile):

    def __init__(self, resource_path):
        super(WordListFile, self).__init__()
        self.resource_path = resource_path
        self.file_patten = 'test_word_list'
        return

    def set_file_patten(self, new_patten):
        self.file_patten = new_patten

    def get_current_pattens(self):
        file_list = self.get_file_list(self.resource_path)
        patten_list = list()
        for file_name in file_list:
            file_head = self.get_file_head(file_name)
            file_head = file_head.split('@')
            head_name = file_head[0]
            if head_name not in patten_list:
                patten_list.append(head_name)
        patten_list = sorted(patten_list)
        return patten_list

    def open_latest_file(self):
        # word, trans, status(1 = pass, 0 = not pass), test_times, correct_times
        file_list = self.get_file_list(self.resource_path)
        file_accept = ''
        max_time = ''
        separator = ''
        file_type = '.txt'
        file_dict = dict()
        for file_name in file_list:
            file_head = self.get_file_head(file_name)
            file_type = self.get_file_type(file_name)
            file_head = file_head.split('@')
            head_name = file_head[0]
            if self.file_patten == head_name and file_type == '.txt':
                file_accept = self.file_patten
                if len(file_head) == 2 and file_head[1] > max_time:
                    max_time = file_head[1]
                    separator = '@'
        if file_accept != '':
            file_accept_name = self.resource_path + '/' + file_accept + separator + max_time + file_type
            self.__dissect_files(file_dict, file_accept_name)
        else:
            print('No word list is found')
        # original word repair
        word_dict_temp = dict()
        file_accept_name = self.resource_path + '/' + file_accept + file_type
        self.__dissect_files(word_dict_temp, file_accept_name)
        for word in word_dict_temp.keys():
            if word not in file_dict.keys():
                msg = 'Adding new word from original:' + word
                print(msg)
                file_dict[word] = dict()
                file_dict[word]['word'] = word
                file_dict[word]['trans'] = word_dict_temp[word]['trans']
                file_dict[word]['status'] = 0
                file_dict[word]['test_times'] = 0
                file_dict[word]['correct_times'] = 0
        key_set = copy.copy(file_dict)
        for word in key_set.keys():
            if word not in word_dict_temp.keys():
                msg = 'Remove word based on original:' + word
                print(msg)
                file_dict.pop(word)
        return file_dict

    def save_test_result(self, word_dict):
        # word, trans, status(1 = pass, 0 = not pass), test_times, correct_times
        time_stamp = time.localtime()
        save_name = self.resource_path + '/' + self.file_patten + '@' + time.strftime("%Y-%m-%d", time_stamp) + '.txt'
        if len(word_dict.keys()) > 0:
            if self.file_not_exist(save_name):
                log = 'New file, save_name:' + save_name
                print(log)
            else:
                log = 'Duplicated name (automatically overwrite), save_name:' + save_name
                print(log)
            file_save = open(save_name, 'w', encoding='utf-8')
            try:
                # do something
                for word in word_dict:
                    str2wri = word_dict[word]['word'] + ' ' + word_dict[word]['trans'] + ' ' + str(
                        word_dict[word]['status']) + ' ' + str(word_dict[word]['test_times']) + ' ' + str(
                        word_dict[word]['correct_times']) + '\n'
                    file_save.write(str2wri)
                print('Result file saved!')
            finally:
                file_save.close()
        else:
            log = 'Word diction is empty, len(word_dict.keys()):' + str(len(word_dict.keys()))
            print(log)


    # Private Method
    def __dissect_files(self, file_dict, file_accept):
        file_op = open(file_accept, 'r', encoding='utf-8')
        try:
            for line in file_op.readlines():
                line = line.strip()
                line_array = line.split(' ')
                word = None
                trans = None
                status = 0
                test_times = 0
                correct_times = 0
                if len(line_array) >= 2:
                    word = line_array[0]
                    trans = line_array[1]
                    if len(line_array) == 5:
                        status = int(line_array[2])
                        test_times = int(line_array[3])
                        correct_times = int(line_array[4])
                if word is not None:
                    file_dict[word] = dict()
                    file_dict[word]['word'] = word
                    file_dict[word]['trans'] = trans
                    file_dict[word]['status'] = status
                    file_dict[word]['test_times'] = test_times
                    file_dict[word]['correct_times'] = correct_times
            if len(file_dict) > 0:
                log = 'Load Success from file:' + file_accept
                print(log)
        finally:
            file_op.close()

# test
if __name__ == '__main__':
    obj = WordListFile('../resource')
    word_dict = obj.open_latest_file()
    obj.save_test_result(word_dict)


