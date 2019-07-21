from service import Service


class S7(Service):
    def send_sms(self):
        self.session.get('https://www.s7.ru/dotCMS/priority/ajaxEnrollment',
                         params={'dispatch': 'shortEnrollmentByPhone', 'mobilePhone.countryCode': self.phone_code,
                                 'mobilePhone.areaCode': self.phone[1:4], 'mobilePhone.localNumber': self.phone[4:-1]})
