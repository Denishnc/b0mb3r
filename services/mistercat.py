from service import Service


class MisterCat(Service):
    def send_sms(self):
        if self.country_code == 'ua':
            self.session.post('https://mistercat.com.ua/index.php',
                              params={'option': 'com_ksenmart', 'view': 'profile', 'task': 'profile.sms_auth',
                                      'tmpl': 'ksenmart'},
                              data={'phone': self.formatted_phone, 'type': 'send'})
