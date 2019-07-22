from service import Service


class Gorzdrav(Service):
    def send_sms(self):
        if self.country_code == 'ru':
            phone = f'{self.formatted_phone[1:4]}) {self.formatted_phone[4:7]}-{self.formatted_phone[7:9]}-{self.formatted_phone[9:11]}'
            self.session.post('https://gorzdrav.org/login/register/sms/send', data={'phone': phone})
