from service import Service


class Ostin(Service):
    def send_sms(self):
        if self.country_code == 'ru':
            phone = f' {self.phone[0]} ({self.phone[1:4]}){self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}'
            self.session.get('https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp',
                             params={'type': 'sendConfirmCode', 'phoneNumber': phone})
