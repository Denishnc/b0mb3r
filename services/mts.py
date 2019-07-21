from service import Service


class MTS(Service):
    def send_sms(self):
        self.session.post('https://api.mtstv.ru/v1/users', data={'msisdn': self.formatted_phone})
