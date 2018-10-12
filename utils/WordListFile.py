#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : WordListFile.py
# @Author: MoonKuma
# @Date  : 2018/10/8
# @Desc  : Open/Save file list

from EasyFile import EasyFile
import time


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
        if file_accept != '':
            file_accept = self.resource_path + '/' + file_accept + '@' + max_time + file_type
            file_op = open(file_accept, 'r')
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
                    if word is not None and word not in file_dict.keys():
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
        else:
            print('No word list is found')
        return file_dict

    def save_test_result(self, word_dict):
        # word, trans, status(1 = pass, 0 = not pass), test_times, correct_times
        time_stamp = time.localtime()
        save_name = self.resource_path + '/' + self.file_patten + '@' + time.strftime("%Y-%m-%d_", time_stamp) + str(int(time.time())) + '.txt'
        if len(word_dict.keys()) > 0:
            if self.file_not_exist(save_name):
                file_save = open(save_name, 'w')
                try:
                    # do something
                    for word in word_dict:
                        str2wri = word_dict[word]['word'] + ' ' + word_dict[word]['trans'] + ' ' + str(word_dict[word]['status']) + ' ' + str(word_dict[word]['test_times']) + ' ' + str(word_dict[word]['correct_times']) + '\n'
                        file_save.write(str2wri)
                finally:
                    file_save.close()
            else:
                log = 'Duplicated name, save_name:' + save_name
                print(log)
        else:
            log = 'Word diction is empty, len(word_dict.keys()):' + str(len(word_dict.keys()))
            print(log)


# test
if __name__ == '__main__':
    obj = WordListFile('../resource')
    word_dict = obj.open_latest_file()
    obj.save_test_result(word_dict)


