# -*- coding: utf-8 -*-
import json
import urllib

import log


def get(url, data=None, timeout=5):
    '''
    向服务端发送一个get的请求
    return: json
    '''
    if data:
        url += '?' + urllib.urlencode(data)
    result = {}
    try:
        f = urllib.urlopen(url)
    except Exception as e:
        log.print_log(__file__, 'Exception: ', e)
    else:
        result = f.read()
        result = result.decode('utf-8')
        result = json.loads(result)
        f.close()
    return result


def post(url, data, timeout=5, ensure_ascii=True):
    '''
    向服务端发送一个post的请求
    return: json
    '''
    data = json.dumps(data, ensure_ascii=ensure_ascii)
    data = data.encode('utf-8')
    result = {}
    try:
        f = urllib.urlopen(url, data, timeout)
    except Exception as e:
        log.print_log(__file__, 'Exception: ', e)
    else:
        result = f.read()
        result = result.decode('utf-8')
        result = json.loads(result)
        if not f.closed:
            f.close()
    return result
