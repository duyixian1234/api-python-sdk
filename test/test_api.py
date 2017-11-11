from functools import partial
from json import loads

import urllib3

from qcloudapi3 import Api

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def call(service, action, params):
    response = service.call(action, params).encode('latin-1').decode('unicode_escape')
    return loads(response)


def make(_module, _config):
    return Api(_module, _config)


config = {
    'Region': 'sh',
    'secretId': 'your secretId',
    'secretKey': 'your secretKey',
    'method': 'post'
}
textSentiment = partial(call, make('wenzhi', config), 'TextSentiment')


def test_neg_sentiment():
    response = textSentiment({'content': '你妈死了'})
    assert response['positive'] < response['negative'], '消极语句判断错误'
    print('消极语句判断正确')


def test_pos_sentiment():
    response = textSentiment({'content': '恭喜你，你的母亲的病治好了'})
    assert response['positive'] > response['negative'], '积极语句判断错误'


def test_neu_sentiment():
    response = textSentiment({'content': '你的母亲逝世了'})
    assert response['positive'] - response['negative'] < 0.1, '中性语句判断错误'
