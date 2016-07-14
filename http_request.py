import json
import urllib.parse
import urllib.request

import log


def get(url, data=None, timeout=5):
    '''
    向服务端发送一个get的请求
    return: json
    '''
    if data:
        url += '?' + urllib.parse.urlencode(data)
    result = {}
    try:
        f = urllib.request.urlopen(url, timeout=timeout)
    except Exception as e:
        log.printLog(__file__, 'Exception: ', e)
    else:
        result = f.read()
        result = result.decode('utf-8')
        result = json.loads(result)
        if not f.closed:
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
        f = urllib.request.urlopen(url, data, timeout)
    except Exception as e:
        log.printLog(__file__, 'Exception: ', e)
    else:
        result = f.read()
        result = result.decode('utf-8')
        result = json.loads(result)
        if not f.closed:
            f.close()
    return result
