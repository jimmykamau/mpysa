import unittest

import mpysa
from mpysa.c2 import C2B

from tests.setup_tests import BaseTest


class TestC2B(BaseTest):
    """Test C2B"""

    def setUp(self):
        self.c2b_transaction = C2B(self.access_token)

    def test_register_url(self):
        self.register_url_response = self.c2b_transaction.register_url(
            mpysa.BASE_RESPONSE_ENDPOINT + "/c2b/confirmation",
            mpysa.BASE_RESPONSE_ENDPOINT + "/c2b/validation")
        print(self.register_url_response.json()["ConversationID"])
        self.assertEqual(
            200,
            self.register_url_response.status_code,
            msg="Error while registering C2B url")
        self.assertEqual(
            "success",
            self.register_url_response.json()["ResponseDescription"],
            msg="C2B url not being registered successfully")


if __name__ == "__main__":
    unittest.main()
