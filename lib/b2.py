import json
import requests
import mpysa
from mpysa.base_mpesa import BaseMPesa


class B2C(BaseMPesa):
    """Class for making Mpesa transactions from company to client (B2C)"""

    def __init__(
            self, oauth_token, base_url=mpysa.BASE_MPESA_URL):
        super().__init__()
        self.oauth_token = oauth_token
        self.https_url = base_url + "/mpesa/b2c/v1/paymentrequest"

    def make_payment(
            self, command_id, amount, receiver_msisdn, remarks,
            timeout_url=mpysa.BASE_RESPONSE_ENDPOINT + "/b2b/timeout",
            response_url=mpysa.BASE_RESPONSE_ENDPOINT + "/b2b/result",
            occasion=None):
        values = self.get_b2c_values(
            command_id, amount, receiver_msisdn, remarks,
            timeout_url, response_url, occasion)
        return requests.post(
            self.https_url,
            headers={
                "Authorization": "Bearer {}".format(
                    self.oauth_token),
                "Content-Type": "application/json"},
            data=json.dumps(values))
