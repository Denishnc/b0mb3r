from service import Service


class TotoPizza(Service):
    def send_sms(self):
        phone = f'+{self.phone[0]} ({self.phone[1:4]}) {self.phone[4:7]}-{self.phone[7:9]}-{self.phone[9:11]}'
        self.session.post('https://totopizza.ru/gus-crystal/',
                          data={'PHONE': phone, 'AUTH_FORM': 'Y', 'LOGIN': 'Продолжить'}, verify=False)
