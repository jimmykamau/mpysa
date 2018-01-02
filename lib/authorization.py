import base64
import requests


class OAuthRequest(object):
    """
    Authorization class that makes the OAuth request
    to get the OAuth token
    """

    consumer_key = None
    consumer_secret = None
    base_url = None
    https_url = None

    def __init__(
            self,
            consumer_key,
            consumer_secret,
            base_url):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.base_url = base_url
        self.https_url = base_url + \
            "oauth/v1/generate?grant_type=client_credentials"

    def generate_auth_string(self, arg):
        auth_string = self.consumer_key + ":" + self.consumer_secret
        return base64.b64encode(auth_string.encode('utf-8'))

    def get_access_token(self):
        return requests.get(
            self.https_url,
            headers={
                "Authorization": "Basic {}".format(
                    self.generate_auth_string(self).decode('utf-8')),
                "Content-Type": "application/json"})
