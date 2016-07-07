import json
import urllib.parse
import urllib.request

import log


# 向服务端发送一个get的请求
def get(url, data=None, timeout=5):
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


# 向服务端发送一个post的请求
def post(url, data, timeout=2, ensure_ascii=True):
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
