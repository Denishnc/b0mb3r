from service import Service


class Gorzdrav(Service):
    def send_sms(self):
        phone = f'{self.phone[1:4]}) {self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}'
        self.session.post('https://gorzdrav.org/login/register/sms/send', data={'phone': phone})
