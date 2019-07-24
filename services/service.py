import os.path
from datetime import datetime

import requests
from fake_useragent import UserAgent
from urllib3.exceptions import InsecureRequestWarning


class Service:
    user_agent = UserAgent()

    def __init__(self, phone, country_data, sms_text='Произошёл троллинг'):
        self.phone = phone
        self.country_code = country_data[0]
        self.phone_code = country_data[1]
        self.sms_text = sms_text if sms_text != '' else 'Произошёл троллинг'
        self.formatted_phone = self.phone_code + self.phone
        self.session = requests.Session()

        if os.path.isfile('debug'):
            self.session_get = self.session.get
            self.session_post = self.session.post
            self.session.get = self.get
            self.session.post = self.post

        self.session.headers = {'User-Agent': self.generate_random_user_agent()}
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    @staticmethod
    def _log_request(name, message):
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {name}: {message}')

    def get(self, *args, **kwargs):
        request = self.session_get(*args, **kwargs)
        logging_text = request.text
        if len(logging_text) > 500:
            if '<!doctype html>' in logging_text.lower():
                logging_text = f'Response too long to display ({len(logging_text)} characters) and is HTML'
            else:
                logging_text = f'Response too long to display ({len(logging_text)} characters) and is not HTML'
        self._log_request(type(self).__name__, logging_text.replace('\n', ''))
        return request

    def post(self, *args, **kwargs):
        request = self.session_post(*args, **kwargs)
        logging_text = request.text
        if len(logging_text) > 500:
            if '<!doctype html>' in logging_text.lower():
                logging_text = f'Response too long to display ({len(logging_text)} characters) and is HTML'
            else:
                logging_text = f'Response too long to display ({len(logging_text)} characters) and is not HTML'
        self._log_request(type(self).__name__, logging_text.replace('\n', ''))
        return request

    @staticmethod
    def generate_random_user_agent():
        return Service.user_agent.random
