kill -9 `cat gunicorn.pid`
gunicorn app:app -b 127.0.0.1:5002 --worker-class gevent --workers 2 --timeout 240 --daemon --access-logfile access.log --error-logfile error.log --capture-output --pid gunicorn.pid
