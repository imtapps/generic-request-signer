import six
import json
import decimal

try:
    from apysigner import DefaultJSONEncoder
except ImportError:
    from datetime import datetime

    class DefaultJSONEncoder(json.JSONEncoder):
        """
        JSONEncoder subclass that knows how to encode date/time and decimal types.
        """
        def default(self, o):
            if isinstance(o, (datetime.datetime, datetime.date, datetime.time)):
                return o.isoformat()
            elif isinstance(o, decimal.Decimal):
                return str(o)
            else:
                return super(DefaultJSONEncoder, self).default(o)

if six.PY3:
    import urllib.request as urllib
else:
    import urllib2 as urllib

from generic_request_signer import response, factory


class Client(object):

    def __init__(self, api_credentials):
        self.api_credentials = api_credentials

    def get_factory(self, files):
        if files:
            return factory.MultipartSignedRequestFactory
        return factory.SignedRequestFactory

    def _get_response(self, http_method, endpoint, data=None, files=None, timeout=15, **request_kwargs):
        headers = request_kwargs.get("headers", {})
        if not isinstance(data, str) and headers.get("Content-Type") == "application/json":
            data = json.dumps(data, default=DefaultJSONEncoder, sort_keys=True)
        try:
            http_response = urllib.urlopen(
                self._get_request(http_method, endpoint, data, files, **request_kwargs), timeout=timeout)
        except urllib.HTTPError as e:
            http_response = e
        return response.Response(http_response)

    def _get_request(self, http_method, endpoint, data=None, files=None, **request_kwargs):
        factory_class = self.get_factory(files)
        request_factory = factory_class(http_method, self._client_id, self._private_key, data, files)
        service_url = self._get_service_url(endpoint)
        return request_factory.create_request(service_url, **request_kwargs)

    def _get_service_url(self, endpoint):
        return self._base_url + endpoint

    @property
    def _base_url(self):
        return self.api_credentials.base_url

    @property
    def _client_id(self):
        return self.api_credentials.client_id

    @property
    def _private_key(self):
        return self.api_credentials.private_key
