import multiprocessing

bind = "0.0.0.0:80"
workers = 1
reload = True
# daemon = True
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"
pythonpath = "/pitrix/conf,/pitrix/lib/pitrix-webconsole,/pitrix/lib/pitrix-webconsole/mysite"
