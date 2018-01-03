import unittest
from pympesa.authorization import OAuthRequest


class BaseTest(unittest.TestCase):
    """Base test class"""

    """https://gist.github.com/twolfson/13f5f5784f67fd49b245"""
    @classmethod
    def setUpClass(cls):
        """On inherited classes, run our `setUp` method"""
        if cls is not BaseTest and cls.setUp is not BaseTest.setUp:
            orig_setUp = cls.setUp

            def setUpOverride(self, *args, **kwargs):
                BaseTest.setUp(self)
                return orig_setUp(self, *args, **kwargs)
            cls.setUp = setUpOverride

    def setUp(self):
        self.oauthrequest = OAuthRequest()
        self.access_token_response = self.oauthrequest.get_access_token()
        self.access_token = self.access_token_response.json()["access_token"]
