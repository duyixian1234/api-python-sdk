from qcloudapi3 import Api


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
