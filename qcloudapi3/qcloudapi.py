#!/usr/bin/python
# -*- coding: utf-8 -*-


class Api:
    def __init__(self, _module, config):
        self.module = _module
        self.config = config

    @staticmethod
    def _factory(_module, config):
        if _module == 'cvm':
            from .modules import cvm
            service = cvm.Cvm(config)
        elif _module == 'scf':
            from .modules import scf
            service = scf.Scf(config)
        elif _module == 'wenzhi':
            from .modules import wenzhi
            service = wenzhi.Wenzhi(config)
        elif _module == 'tmt':
            from .modules import tmt
            service = tmt.Tmt(config)
        elif _module == 'account':
            from .modules import account
            service = account.Account(config)
        elif _module == 'cmq':
            from .modules import cmq
            service = cmq.Cmq(config)
        else:
            raise ValueError
        return service

    def setSecretId(self, secretId):
        self.config['secretId'] = secretId

    def setSecretKey(self, secretKey):
        self.config['secretKey'] = secretKey

    def setRequestMethod(self, method):
        self.config['method'] = method

    def setRegion(self, region):
        self.config['region'] = region

    def generateUrl(self, action, params):
        service = self._factory(self.module, self.config)
        return service.generateUrl(action, params)

    def call(self, action, params):
        service = self._factory(self.module, self.config)

        methods = dir(service)
        for method in methods:
            if method == action:
                func = getattr(service, action)
                return func(params)

        return service.call(action, params)


def main():
    _module = 'wenzhi'
    action = 'TextSentiment'
    config = {
        'Region': 'gz',
        'secretId': '000',
        'secretKey': '111',
        'method': 'post'
    }
    params = {
        "content": "所有人都很差劲。",
    }
    service = Api(_module, config)
    print('URL:\n' + service.generateUrl(action, params))
    print(service.call(action, params))


if __name__ == '__main__':
    main()
