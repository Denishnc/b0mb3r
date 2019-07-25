from service import Service


class PsWallet(Service):
    def send_sms(self):
        if self.country_code == 'ru':
            self.session.get('https://api.pswallet.ru/system/smsCode',
                             params={'mobile': self.formatted_phone, 'type': '0'})
