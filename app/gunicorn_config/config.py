import socket

wsgi_app = 'app.wsgi:application'
loglevel = 'debug'
workers = 2
bind = '0.0.0.0:8000'
# accesslog = errorlog = '/var/log/gunicorn.log'
# capture_output = True
forwarded_allow_ips = '127.0.0.1'


def on_starting(server):
    print("STARTING GUNICORN")
    ip_nginx = socket.gethostbyname('nginx')
    print(ip_nginx)
    global forwarded_allow_ips
    forwarded_allow_ips += f',{ip_nginx}'
    print(forwarded_allow_ips)
