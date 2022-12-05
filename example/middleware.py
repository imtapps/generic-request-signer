from client import FlaskAuthClient


class AuthMiddleware(object):

    def __init__(self, app):
        self.app = app.wsgi_app
        self.client = FlaskAuthClient(app.config)

    def __call__(self, environ, start_response):
        request = environ.get('PATH_INFO')
        if request == '/':
            self.client.verify(dict(username='foo', password='bar'))
        return self.app(environ, start_response)
