import random
import string

from service import Service


class Aramba(Service):
    def send_sms(self):
        name = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        self.session.post('http://www.aramba.ru/core.php',
                          data={'act': 'codeRequest', 'phone': '+' + self.formatted_phone, 'l': name, 'p': name,
                                'name': name, 'email': name + '@gmail.com'})
