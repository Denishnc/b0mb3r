from service import Service


class MVideo(Service):
    def send_sms(self):
        phone = f'{self.phone[1:4]}-{self.phone[4:11]}'
        self.session.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={'pageName': 'registerPrivateUserPhoneVerification'}, data={'phone': phone})
