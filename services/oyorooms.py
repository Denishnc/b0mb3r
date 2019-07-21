from service import Service


class OyoRooms(Service):
    def send_sms(self):
        self.session.get('https://www.oyorooms.com/api/pwa/generateotp',
                         params={'phone': self.phone[1:], 'country_code': '+' + self.formatted_phone})
