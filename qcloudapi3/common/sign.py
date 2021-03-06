#!/usr/bin/python
# -*- coding: utf-8 -*-

import binascii
import hashlib
import hmac


class Sign:
    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey

    def make(self, requestHost, requestUri, params, method='GET'):
        paramsList = {}
        for param_key in params:
            if method == 'post' and str(params[param_key])[0:1] == "@":
                continue
            paramsList[param_key] = params[param_key]
        srcStr = method.upper() + requestHost + requestUri + '?' + "&".join(
            k.replace("_", ".") + "=" + str(paramsList[k])
            for k in sorted(paramsList.keys()))
        hashed = hmac.new(self.secretKey.encode(), srcStr.encode(), hashlib.sha1)
        return binascii.b2a_base64(hashed.digest())[:-1]


def main():
    secretId = 123
    secretKey = 'xxx'
    params = {}
    sign = Sign(secretId, secretKey)
    print(sign.make('https://cvm.api.qcloud.com', '/v2/index.php', params))


if __name__ == '__main__':
    main()
