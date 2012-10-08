from generic_request_signer.client import Client
from backend import FlaskSettingsApiCredentialsBackend


class FlaskAuthClient(Client):
    domain_settings_name = 'EXAMPLE_CLIENT_DOMAIN'
    client_id_settings_name = 'EXAMPLE_CLIENT_ID'
    private_key_settings_name = 'EXAMPLE_PRIVATE_KEY'

    def __init__(self, config):
        api_credentials = FlaskSettingsApiCredentialsBackend(self, config)
        super(FlaskAuthClient, self).__init__(api_credentials)

    def verify(self, data):
        return self._get_response('GET', '/verify', data)
