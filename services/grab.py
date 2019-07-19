from service import Service


class Grab(Service):
    def send_sms(self):
        self.session.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': self.phone, 'countryCode': 'ru', 'name': 'Grab', 'email': 'Grab'})
