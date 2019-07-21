from service import Service


class PrivetMir(Service):
    def send_sms(self):
        if self.country_code == 'ru':
            phone = f'+{self.phone[0]} ({self.phone[1:4]}){self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}'
            self.session.post('https://api-user.privetmir.ru/api/send-code',
                              data={'approve1': 'on', 'approve2': 'on', 'checkApproves': 'Y', 'checkExist': 'Y',
                                    'login': phone, 'scope': 'register-user'})
