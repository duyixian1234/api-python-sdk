#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base


class Scf(Base):
    requestHost = 'scf.api.qcloud.com'


def main():
    action = 'InvokeFunction'
    config = {
        'Region': 'sh',
        'secretId': 'AKIDPglgT5ZwBF7nHZLZJrDONAW2QcdSGZql',
        'secretKey': '000',
        'method': 'get'
    }
    params = {'functionName': 'add', 'param': '{"a":1,"b":2}'}
    params1 = {'functionName':'date'}
    service = Scf(config)
    print(service.call(action, params1))


if (__name__ == '__main__'):
    main()
