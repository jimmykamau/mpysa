import requests

import mpysa
from mpysa.helpers import generate_auth_string


class OAuthRequest(object):
    """
    Authorization class that makes the OAuth request
    to get the OAuth token
    """

    def __init__(
            self,
            consumer_key=mpysa.CONSUMER_KEY,
            consumer_secret=mpysa.CONSUMER_SECRET,
            base_url=mpysa.BASE_MPESA_URL):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.https_url = base_url + \
            "oauth/v1/generate?grant_type=client_credentials"

    def get_access_token(self):
        return requests.get(
            self.https_url,
            headers={
                "Authorization": "Basic {}".format(
                    generate_auth_string(self).decode('utf-8')),
                "Content-Type": "application/json"})
