from service import Service


class Tinkoff(Service):
    def send_sms(self):
        self.session.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + self.formatted_phone})
