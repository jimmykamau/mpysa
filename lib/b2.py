import mpysa
from mpysa.base_mpesa import BaseMPesa
from mpysa.helpers import get_id_type, make_post_request


class B2C(BaseMPesa):
    """Class for making Mpesa transactions from company to client (B2C)"""

    def __init__(
            self, oauth_token, base_url=mpysa.BASE_MPESA_URL):
        super().__init__(
            oauth_token, base_url + "/mpesa/b2c/v1/paymentrequest")

    def make_payment(
            self, command_id, amount, receiver_msisdn, remarks,
            timeout_url=mpysa.BASE_RESPONSE_ENDPOINT,
            response_url=mpysa.BASE_RESPONSE_ENDPOINT,
            occasion=None):
        values = self.get_b2c_values(
            command_id, amount, receiver_msisdn, remarks,
            timeout_url, response_url, occasion)
        return make_post_request(self.https_url, self.oauth_token, values)


class B2B(BaseMPesa):
    """Class for making Mpesa transactions from one company to another (B2B)"""

    def __init__(
            self, oauth_token, base_url=mpysa.BASE_MPESA_URL):
        super().__init__(
            oauth_token, base_url + "/mpesa/b2b/v1/paymentrequest")

    def make_payment(
            self, command_id, receiver_id_type, amount,
            receiver_account_number, transaction_reference, remarks,
            timeout_url=mpysa.BASE_RESPONSE_ENDPOINT,
            response_url=mpysa.BASE_RESPONSE_ENDPOINT):
        values = self.get_b2b_values(
            command_id, get_id_type(receiver_id_type), amount,
            receiver_account_number, transaction_reference,
            remarks, timeout_url, response_url)
        return make_post_request(self.https_url, self.oauth_token, values)
