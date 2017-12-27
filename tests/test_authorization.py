import unittest
import pympesa


class TestAuthorization(unittest.TestCase):
    """docstring for TestAuthorization"""

    def setUp(self):
        self.base_url = pympesa.BASE_URL
        self.consumer_key = pympesa.CONSUMER_KEY
        self.consumer_secret = pympesa.CONSUMER_SECRET
        self.oauthrequest = pympesa.authorization.OAuthRequest(
            self.consumer_key, self.consumer_secret, self.base_url)
        self.access_token = self.oauthrequest.get_access_token()

    def test_get_access_token(self):
        self.assertEqual(
            200,
            self.access_token.status_code,
            msg="Cannot get access token from endpoint")
        self.assertTrue(
            self.access_token.json()["access_token"],
            msg="Access token not being returned")


if __name__ == "__main__":
    unittest.main()
