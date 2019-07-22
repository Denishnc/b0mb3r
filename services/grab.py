from service import Service


class Grab(Service):
    def send_sms(self):
        self.session.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': self.formatted_phone, 'countryCode': self.country_code, 'name': 'Grab',
                                'email': 'Grab'})
