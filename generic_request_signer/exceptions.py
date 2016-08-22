import six


class WebException(Exception):
    """
    Base Exception for client errors
    """

    def __init__(self, message):
        self.message = message
        if six.PY3:
            super().__init__()
        else:
            super(WebException, self).__init__()


class HttpMethodNotAllowed(Exception):
    pass
