from .base import Base


class Cmq(Base):
    requestHost = 'cmq-queue-sh.api.qcloud.com'

def main():
    action = 'SendMessage'
    config = {
        'Region': 'gz',
        'secretId': '123',
        'secretKey': '000',
        'method': 'get'
    }
    params = {
        "content": "123",
    }
    service = Cmq(config)
    print(service.call(action, params))


if __name__ == '__main__':
    main()
