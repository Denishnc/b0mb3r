import random
import string

from service import Service


class VoxImplant(Service):
    def send_sms(self):
        name = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        self.session.post('https://api-ru-manage.voximplant.com/api/AddAccount',
                          data={'region': 'eu', 'account_name': name, 'language_code': 'en',
                                'account_email': name + '@gmail.com', 'account_password': name})
        self.session.post('https://api-ru-manage.voximplant.com/api/SendActivationCode',
                          data={'phone': self.formatted_phone, 'account_email': name + '@gmail.com'})
