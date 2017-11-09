#!/usr/bin/python
# -*- coding: utf-8 -*-

from .base import Base


class Scf(Base):
    requestHost = 'scf.api.qcloud.com'


def main():
    action = 'InvokeFunction'
    config = {
        'Region': 'sh',
        'secretId': '123',
        'secretKey': '000',
        'method': 'get'
    }
    params1 = {'functionName': 'date'}
    service = Scf(config)
    print(service.call(action, params1))


if __name__ == '__main__':
    main()
