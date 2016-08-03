# -*- coding: utf-8 -*-
import os
import sys
import datetime


def print_log(*params):
    '''
    自定义打印log日志
    '''
    now = datetime.datetime.now()
    try:
        raise Exception
    except:
        traceback_frame = sys.exc_info()[2].tb_frame.f_back
    line = traceback_frame.f_lineno
    file_path = str(traceback_frame.f_code.co_filename)
    file_name = os.path.split(file_path)[-1]
    s = ''
    s += '[' + now.strftime('%Y-%m-%d %H:%M:%S') + ' '
    s += file_name + ' '
    s += 'line ' + str(line) + ']:\t'
    for param in params:
        s += str(param)
    print(s)
    with open('log', mode='a') as f:
        f.write(s + '\n')
        f.flush()

# 输出格式类似：
# [2016-06-30 15:12:07 note.py line 153]: add_book - action: commit rollback
