from service import Service


class RuTube(Service):
    def send_sms(self):
        self.session.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + self.formatted_phone})
