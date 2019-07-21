from service import Service


class Rabota(Service):
    def send_sms(self):
        self.session.post('https://www.rabota.ru/remind', data={'credential': self.formatted_phone})
