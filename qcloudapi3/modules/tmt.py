#!/usr/bin/python
# -*- coding: utf-8 -*-

from .base import Base


class Tmt(Base):
    requestHost = 'tmt.api.qcloud.com'


def main():
    action = 'TextTranslate'
    config = {
        'Region': 'gz',
        'secretId': '123',
        'secretKey': '000',
        'method': 'get'
    }
    params = {
        "content": "123",
    }
    service = Tmt(config)
    print(service.call(action, params))


if __name__ == '__main__':
    main()
