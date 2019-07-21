from service import Service


class Tinder(Service):
    def send_sms(self):
        self.session.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': self.formatted_phone})
