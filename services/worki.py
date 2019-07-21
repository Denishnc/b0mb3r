from service import Service


class Worki(Service):
    def send_sms(self):
        self.session.post('https://api.iconjob.co/api/web/v1/verification_code', data={'phone': self.formatted_phone})
