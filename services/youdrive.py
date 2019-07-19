from service import Service


class YouDrive(Service):
    def send_sms(self):
        self.session.post('http://youdrive.today/signup/phone', data={'phone': self.phone[1:], 'phone_code': '7'})
