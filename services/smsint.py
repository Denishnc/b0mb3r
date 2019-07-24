from service import Service


class SmsInt(Service):
    def send_sms(self):
        self.session.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': self.sms_text, 'phone': self.formatted_phone})
