import unittest
from tests.setup_tests import BaseTest


class TestAuthorization(BaseTest):
    """Test OAuthRequest"""

    def test_get_access_token(self):
        self.assertEqual(
            200,
            self.access_token_response.status_code,
            msg="Cannot get access token from endpoint")
        self.assertGreater(
            len(self.access_token), 0,
            msg="Access token not being returned")


if __name__ == "__main__":
    unittest.main()
