from service import Service


class Tanuki(Service):
    def send_sms(self):
        phone = f'(+{self.phone_code}){self.formatted_phone[1:-1]}'
        self.session.post('https://www.tanuki.ru/api/', json={
            'header': {'version': '2.0', 'userId': '1', 'debugMode': True,
                       'agent': {'device': 'desktop', 'version': '1'}, 'langId': '1', 'cityId': '1', 'dbgValue': ''},
            'method': {'name': 'sendSmsCode'}, 'data': {'phone': phone, 'type': 1}})
