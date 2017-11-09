#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
import os
import random
import sys
import time
import warnings

from ..common import Request

warnings.filterwarnings("ignore")

sys.path.append(os.path.split(os.path.realpath(__file__))[0] + os.sep + '..')


class Base:
    debug = 0
    requestHost = ''
    requestUri = '/v2/index.php'
    _params = {}

    def __init__(self, config):
        self.secretId = config['secretId']
        self.secretKey = config['secretKey']
        self.defaultRegion = config['Region']
        self.method = config['method']

    def _checkParams(self, action, params):
        self._params = copy.deepcopy(params)
        self._params['Action'] = action[0].upper() + action[1:]

        if 'Region' not in self._params:
            self._params['Region'] = self.defaultRegion

        if 'SecretId' not in self._params:
            self._params['SecretId'] = self.secretId

        if 'Nonce' not in self._params:
            self._params['Nonce'] = random.randint(1, 10000)

        if 'Timestamp' not in self._params:
            self._params['Timestamp'] = int(time.time())

        return self._params

    def generateUrl(self, action, params):
        self._checkParams(action, params)
        request = Request(self.secretId, self.secretKey)
        return request.generateUrl(self.requestHost, self.requestUri, self._params, self.method)

    def call(self, action, params, files=None):
        if files is None:
            files = {}
        self._checkParams(action, params)
        request = Request(self.secretId, self.secretKey)
        return request.send(self.requestHost, self.requestUri, self._params, files, self.method, self.debug)


def main():
    action = 'DescribeInstances'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get',
    }
    params = {}
    base = Base(config)
    print(base.call(action, params))


if __name__ == '__main__':
    main()
