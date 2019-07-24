import inspect
import logging
import os
import socket
import sys
import threading
import webbrowser

from flask import Flask, request, render_template, abort

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


def run_service(service_class, module_, phone, country_code, phone_code, sms_text, type_):
    if type_ == 'call':
        getattr(module_, service_class)(phone, [country_code, phone_code], sms_text).send_call()
    else:
        getattr(module_, service_class)(phone, [country_code, phone_code], sms_text).send_sms()
    sys.exit()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', sms=len(service_classes))


@app.route('/sms', methods=['POST'])
def start():
    try:
        phone = request.form['phone']
        count = request.form['count']
        country_code = request.form['country']
        phone_code = country_codes[country_code]
        send_calls = request.form['call']
        sms_text = request.form['smsText']
        send_calls_bool = True if send_calls == 'true' else False

        for _ in range(int(count)):
            for module_, service_class in service_classes.items():
                try:
                    _ = getattr(module_, service_class).send_call
                    if send_calls_bool:
                        threading.Thread(target=run_service,
                                         args=(service_class, module_, phone, country_code, phone_code, sms_text,
                                               'call')).start()
                except AttributeError:
                    threading.Thread(target=run_service,
                                     args=(service_class, module_, phone, country_code, phone_code, sms_text,
                                           'sms')).start()
        return '(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧'
    except (ValueError, KeyError):
        abort(400)


if not bool(os.environ.get('PORT')):
    print(' * Listening on http://' + get_ip() + ':8080/')
    webbrowser.open('http://' + get_ip() + ':8080/', new=2, autoraise=True)
    app.run(host='0.0.0.0', port=8080, threaded=True)
