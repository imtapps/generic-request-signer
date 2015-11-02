import six

if six.PY3:
    from urllib.request import Request
else:
    from urllib2 import Request

from generic_request_signer.exceptions import HttpMethodNotAllowed


class Request(Request, object):

    http_method_names = ['get', 'post', 'put', 'delete', 'patch', 'head', 'options', 'trace']

    def __init__(self, http_method, url, data, *args, **kwargs):
        method_lower = http_method.lower()
        if method_lower not in self.http_method_names:
            raise HttpMethodNotAllowed
        self.http_method = http_method
        super(Request, self).__init__(url, data, *args, **kwargs)

    def get_method(self):
        return self.http_method
