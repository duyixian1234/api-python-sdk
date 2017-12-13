class Parameter:
    def __init__(self):
        self._action = ''
        self._params = {}
    def action(self, _action):
        self._action=  _action
        return self
    def params(self, _params):
        self._params = _params
        return self
    def run(self, service):
        return service.call(self._action, self._params)