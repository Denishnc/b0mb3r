from service import Service


class Optima(Service):
    def send_sms(self):
        if self.country_code == 'ua':
            self.session.post('https://online.optima.taxi/user/get-code', data={'phone': self.formatted_phone})
