from service import Service


class WifiMetro(Service):
    def send_sms(self):
        self.session.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': self.formatted_phone},
                          headers={'App-ID': 'cabinet'})
