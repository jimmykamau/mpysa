import unittest
from pympesa.b2 import B2C

from tests.setup_tests import BaseTest


class TestB2C(BaseTest):
    """Test B2C"""

    def setUp(self):
        self.b2c_transaction = B2C(self.access_token)
        self.b2c_payment = self.b2c_transaction.make_payment(
            "PromotionPayment", "10", "254708374149", "Test B2C")

    def test_create_b2c_transaction(self):
        self.assertEqual(
            200,
            self.b2c_payment.status_code,
            msg="Error while creating b2c transaction")
        self.assertTrue(
            self.b2c_payment.json()["ConversationID"],
            msg="B2C payment not being made successfully")


if __name__ == "__main__":
    unittest.main()
