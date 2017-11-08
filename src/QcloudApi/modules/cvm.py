#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base


class Cvm(Base):
    requestHost = 'cvm.api.qcloud.com'


def main():
    action = 'DescribeInstances'
    config = {
        'Region': 'sh',
        'secretId': 'AKIDPglgT5ZwBF7nHZLZJrDONAW2QcdSGZql',
        'secretKey': '000',
        'method': 'get'
    }
    params = {}
    service = Cvm(config)
    print(service.call(action, params))


if (__name__ == '__main__'):
    main()