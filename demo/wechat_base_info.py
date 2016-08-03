# -*- coding: utf-8 -*-
import datetime
import configparser

import log
import http_request

config = configparser.ConfigParser()
config.read('./demo/config.txt')


def update_access_token():
    '''
    更新access token
    '''
    url = config['url']['token']
    data = {
        'grant_type': 'client_credential',
        'appid': config['wechat.info']['appid'],
        'secret': config['wechat.info']['appsecret'],
    }
    result = http_request.get(url, data)
    now = datetime.datetime.now()
    config['wechat'] = {
        'access_token': result['access_token'],
        'expires_time': now + datetime.timedelta(hours=2),
        'update_time': now,
    }
    with open('./demo/config.txt', 'w') as configfile:
        config.write(configfile)
    log.print_log('access_token: ', result['access_token'])

# update_access_token()
