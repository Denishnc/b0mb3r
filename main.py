import inspect
import logging
import os
import socket
import sys
import webbrowser

from flask import Flask, request, render_template

country_codes = {'ru': '7', 'ua': '380', 'kz': '7', 'by': '375'}

services = os.listdir('services')
service_classes = {}
sys.path.insert(0, 'services')

for service in services:
    if service.endswith('.py') and service != 'service.py':
        module = __import__(service[:-3])
        for member in inspect.getmembers(module, inspect.isclass):
            if member[1].__module__ == module.__name__:
                service_classes[module] = member[0]

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.CRITICAL)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', sms=len(service_classes))


@app.route('/sms', methods=['POST'])
def start():
    phone = request.form['phone']
    count = request.form['count']
    country_code = request.form['country']
    phone_code = country_codes[country_code]
    for _ in range(int(count)):
        for module_, service_class in service_classes.items():
            getattr(module_, service_class)(phone, [country_code, phone_code]).send_sms()
    return '(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧'


if not bool(os.environ.get('PORT')):
    print(' * Listening on http://' + get_ip() + ':8080/')
    webbrowser.open('http://' + get_ip() + ':8080/')
    app.run(host='0.0.0.0', port=8080, threaded=True)
