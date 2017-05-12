# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from web.webapp import create_app

# using gevent wsgi server to host flask app
if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    print("http server port : %u" % port)

    http_server = WSGIServer(('127.0.0.1', port), create_app())
    http_server.serve_forever()