import mpysa
from mpysa.base_mpesa import BaseMPesa
from mpysa.helpers import make_post_request


class C2B(BaseMPesa):
    """
    Class to register URL for Validation/Confirmation and
    Simulate transaction
    """

    def __init__(
            self, oauth_token, base_url=mpysa.BASE_MPESA_URL):
        super().__init__(
            oauth_token, base_url)

    def register_url(
            self, confirmation_url=mpysa.BASE_RESPONSE_ENDPOINT,
            validation_url=mpysa.BASE_RESPONSE_ENDPOINT):
        values = self.get_c2b_register_url_values(
            confirmation_url, validation_url)
        request_url = self.https_url + "/mpesa/c2b/v1/registerurl"
        return make_post_request(request_url, self.oauth_token, values)
