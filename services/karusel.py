from service import Service


class Karusel(Service):
    def send_sms(self):
        self.session.post('https://app.karusel.ru/api/v1/phone/', data={'phone': self.formatted_phone})
