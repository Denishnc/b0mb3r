from service import Service


class BelkaCar(Service):
    def send_sms(self):
        self.session.post('https://belkacar.ru/get-confirmation-code',
                          data={'phone': self.formatted_phone})
