#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Wenzhi(Base):
    requestHost = 'wenzhi.api.qcloud.com'

def main():
    action = 'TextSentiment'
    config = {
        'Region': 'gz',
        'secretId': 'AKIDPglgT5ZwBF7nHZLZJrDONAW2QcdSGZql',
        'secretKey': '000',
        'method': 'get'
    }
    params = {
        "content" : "123",
    }
    service = Wenzhi(config)
    print(service.call(action, params))

if (__name__ == '__main__'):
    main()
