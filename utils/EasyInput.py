#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : EasyInput.py
# @Author: MoonKuma
# @Date  : 2018/10/8
# @Desc  : Accept keyboard input and check correctness, the input func with time count is system-depended

import threading
import time
import sys
import platform
system_type = platform.system()
if system_type == 'Linux':
    import signal
elif system_type == 'Windows':
    import msvcrt  # one can not import msvcrt in linux system
else:
    error_msg = 'Unrecognized System Type:' + system_type
    print(error_msg)
    raise RuntimeError(error_msg)


class AlarmException(Exception):
    pass


class EasyInput(object):

    def __init__(self):
        self.system_type = platform.system()
        return

    def input_without_check(self, input_str, default_return=0, *time_limit):
        if len(time_limit) > 0 and int(time_limit[0]) > 0:
            return self.__input_and_check_limit_time(input_str, int(time_limit[0]), default_return)
        else:
            return raw_input(input_str)

    def input_and_check(self, input_str, accept_list, default_return, *time_limit):
        if len(time_limit) > 0 and int(time_limit[0]) > 0:
            return self.__input_hold(input_str, accept_list, int(time_limit[0]), default_return)
        else:
            return self.__input(input_str, accept_list)

    def __alarmHandler(signum, frame): # this is required in linux - signal method
        raise AlarmException

    def __accept(self, accept_list, test_word):
        test_word = test_word.lower()
        for word in accept_list:
            if test_word == word.lower():
                return True
        string = 'Input not acceptable. Legal input includes:' + accept_list[0]
        if len(accept_list) > 1:
            for index in range(1, len(accept_list)):
                string = string + ',' + str(accept_list[index])
        print(string)
        return False

    def __input(self, input_str, accept_list):
        receive_str = raw_input(input_str)
        while True:
            if not self.__accept(accept_list, receive_str):
                receive_str = raw_input(input_str)
            else:
                break
        return receive_str

    def __input_hold(self, input_str, accept_list, time_count, default_return):
        receive_str = self.__input_and_check_limit_time(input_str, time_count, default_return)
        while True:
            if receive_str == default_return or self.__accept(accept_list, receive_str):
                break
            else:
                receive_str = self.__input_and_check_limit_time(input_str, time_count, default_return)
        return receive_str

    def __input_and_check_limit_time(self, input_str, time_count, default_return):
        if self.system_type == 'Linux':
            return self.__linux_input(input_str, default_return, time_count)
        elif self.system_type == 'Windows':
            return self.__windows_input(input_str, default_return, time_count)

    def __windows_input(self, input_str, default, time_count):
        start_time = time.time()
        sys.stdout.write('%s' % input_str)
        sys.stdout.flush()
        input_rec = ''
        while True:
            ini = msvcrt.kbhit()
            try:
                if ini:
                    key_input = msvcrt.getche()
                    if ord(key_input) == 13:  # enter_key
                        break
                    elif ord(key_input) >= 32:
                        input_rec += key_input.decode()
            except:
                pass
            if len(input_rec) == 0 and time.time() - start_time > time_count:
                break
        print ('')  # needed to move to next line
        if len(input_rec) > 0:
            return input_rec + ''
        else:
            print '\nPrompt timeout. Continuing...'
            return default

    def __linux_input(self, input_str, default, time_count):
        # Resolved only under python(linux)
        signal.signal(signal.SIGALRM, self.__alarmHandler)
        signal.alarm(time_count)
        try:
            text = raw_input(input_str)
            signal.alarm(0)
            return text
        except AlarmException:
            print '\nPrompt timeout. Continuing...'
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return default

    # Blamed method:
    def __input_and_check_thread(self, input_str, accept_list, time_count):
        # no longer used
        # thread could be used to end function but unable to escape from the input(a build in func) gui
        return_list = list()
        t = threading.Thread(target=self.__input, args=(input_str, accept_list, ))
        t.start()
        t.join(time_count)
        if len(return_list) == 0:
            log = 'Time out, limited time:' + str(time_count)
            print(log)
            return False
        else:
            return return_list[0]


# test
if __name__ == '__main__':
    obj = EasyInput()
    word_dict = obj.input_and_check('test input:\n', ['A', 'b', 'c'], 'empty', 10)
    print 'word_dict:', str(word_dict)
