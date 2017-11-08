#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base


class Account(Base):
    requestHost = 'account.api.qcloud.com'


def main():
    action = 'AddProject'
    config = {
        'Region': 'sh',
        'secretId': 'AKIDPglgT5ZwBF7nHZLZJrDONAW2QcdSGZql',
        'secretKey': '000',
        'method': 'get'
    }
    params = {}
    service = Account(config)
    print(service.call(action, params))


if (__name__ == '__main__'):
    main()
