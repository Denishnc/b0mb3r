from service import Service


class Sunlight(Service):
    def send_sms(self):
        self.session.options('https://api.sunlight.net/v3/customers/authorization/')
        self.session.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': self.formatted_phone})
