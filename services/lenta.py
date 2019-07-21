from service import Service


class Lenta(Service):
    def send_sms(self):
        self.session.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                          json={'phone': '+' + self.formatted_phone})
