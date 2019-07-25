from service import Service


class DoZarplati(Service):
    def send_sms(self):
        if self.country_code == 'ru':
            self.session.post('https://online-api.dozarplati.com/rpc',
                              json={'id': 1, 'jsonrpc': '2.0', 'method': 'auth.login',
                                    'params': {'phoneNumber': self.formatted_phone}})
