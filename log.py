import os
import sys
import datetime


def printLog(fileName, *params):
    '''
    自定义打印log日志
    '''
    now = datetime.datetime.now()
    fileName = os.path.split(fileName)[1]
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    line = f.f_lineno
    s = ''
    s += '[' + now.strftime('%Y-%m-%d %H:%M:%S') + ' '
    s += fileName + ' '
    s += 'line:' + str(line) + ']:\t'
    for param in params:
        s += str(param)
    print(s)
    try:
        with open('log.txt', 'a') as f:
            f.write(s + '\n')
    except Exception as e:
        print(e)

# 输出格式类似：
# [2016-06-30 15:12:07 note.py line 153]: add_book - action: commit rollback
