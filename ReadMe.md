@Author : MoonKuma
@Date  : 2018/10/8 10:39
@Contact me : https://github.com/MoonKuma or search 'MoonKuma' at WeChat 

# Word List

## Abstract

1. Used for recall test over customized word list. 
2. Capable of remembering testing result and arranging review over those unfamiliar/new-adding ones
3. You can also add different word pattern and select them inside the program (like here: test_word_list/gre_word)
4. Compatible for both Windows/Linux environment

## Environment Required

1. Python 3

2. Signal or msvcrt depending on platform type for controlling input:

   ```python
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
   ```

## Adds/Modify words list

1. File patten

   ```
   # file patten : AAA
   # file name(original) : AAA.txt
   # file name(saved) : AAA@2018-11-11.txt
   ```

2. Program will automatically load the lasted version for each file patten

3. Program will detected the modification of original file name and adding new words in current saving

## Getting Start

1. Running the StartLarning.py in cmd-window(terminal) to start program
2. Running directly in IDE(like PyCharm) may cause problems (input with time limit)



