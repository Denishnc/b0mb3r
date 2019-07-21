from service import Service


class TaxiSeven(Service):
    def send_sms(self):
        self.session.post('http://taxiseven.ru/auth/register', data={'phone': self.formatted_phone})
