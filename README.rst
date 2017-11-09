qcloudapi3
----------
qcloudapi3是为了让Python3开发者能够在自己的代码里更快捷方便的使用腾讯云的API而开发的Python库。

Example
=======
>>>from QcloudApi import QcloudApi
>>>_module = 'wenzhi'
>>>action = 'TextSentiment'
>>>config = {
>>>    'Region': 'gz',
>>>    'secretId': '123',
>>>    'secretKey': '000',
>>>    'method': 'post'
>>>}
>>> params = {
>>>     "content": "所有人都很差劲。",
>>>}
>>>service = QcloudApi(_module, config)
>>>print('URL:\n' + service.generateUrl(action, params))
>>>print(service.call(action, params))
URL:
https://wenzhi.api.qcloud.com/v2/index.php
{"code":0,"message":"","codeDesc":"Success","positive":0.048611093312502,"negative":0.95138889551163}

Install
=======
code::shell
pip install qcloudapi3

Author
======
Yixian Du