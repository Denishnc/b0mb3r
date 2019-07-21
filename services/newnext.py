from service import Service


class NewNext(Service):
    def send_sms(self):
        self.session.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
            'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': self.formatted_phone,
                       'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {'
                                                                       '\n  registration(client: $client) {'
                                                                       '\n    token\n    __typename\n  }\n}\n'})
