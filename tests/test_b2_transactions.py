import unittest

import mpysa
from mpysa.b2 import B2C, B2B

from tests.setup_tests import BaseTest


class TestB2C(BaseTest):
    """Test B2C"""

    def setUp(self):
        self.b2c_transaction = B2C(self.access_token)
        self.b2c_payment = self.b2c_transaction.make_payment(
            "PromotionPayment", "10", "254708374149", "Test B2C",
            mpysa.BASE_RESPONSE_ENDPOINT + "/b2c/timeout",
            mpysa.BASE_RESPONSE_ENDPOINT + "/b2c/result")

    def test_create_b2c_transaction(self):
        self.assertEqual(
            200,
            self.b2c_payment.status_code,
            msg="Error while creating b2c transaction")
        self.assertTrue(
            self.b2c_payment.json()["ConversationID"],
            msg="B2C payment not being made successfully")


class TestB2B(BaseTest):
    """Test B2B"""

    def setUp(self):
        self.b2b_transaction = B2B(self.access_token)
        self.b2b_payment = self.b2b_transaction.make_payment(
            "BusinessPayBill", "Organization",
            "10", "600000", "TestABC123", "Testing B2B",
            mpysa.BASE_RESPONSE_ENDPOINT + "/b2b/timeout",
            mpysa.BASE_RESPONSE_ENDPOINT + "/b2b/result")

    def test_create_b2b_transaction(self):
        self.assertEqual(
            200,
            self.b2b_payment.status_code,
            msg="Error while creating b2b_payment transaction")
        self.assertTrue(
            self.b2b_payment.json()["ConversationID"],
            msg="B2B payment not being made successfully")


if __name__ == "__main__":
    unittest.main()
