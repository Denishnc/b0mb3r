from service import Service


class FastMoney(Service):
    def send_sms(self):
        if self.country_code == 'ru':
            self.session.post('https://fastmoney.ru/auth/registration',
                              data={'RegistrationForm[username]': '+' + self.formatted_phone,
                                    'RegistrationForm[password]': '12345', 'RegistrationForm[confirmPassword]': '12345',
                                    'yt0': 'Регистрация'})
