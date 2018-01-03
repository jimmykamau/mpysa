import json
import requests
import pympesa


class B2C(object):
    """Class for making Mpesa transactions from company to client (B2C)"""

    def __init__(
            self, oauth_token, base_url=pympesa.BASE_MPESA_URL):
        self.oauth_token = oauth_token
        self.https_url = base_url + "/mpesa/b2c/v1/paymentrequest"

    def make_payment(
            self, command_id, amount, receiver_msisdn, remarks,
            timeout_url=pympesa.BASE_RESPONSE_ENDPOINT,
            response_url=pympesa.BASE_RESPONSE_ENDPOINT,
            occasion=None):
        values = {
            "InitiatorName": pympesa.INITIATOR_NAME,
            "SecurityCredential": pympesa.SECURITY_CREDENTIAL,
            "CommandID": command_id,
            "Amount": amount,
            "PartyA": pympesa.BUSINESS_SHORTCODE,
            "PartyB": receiver_msisdn,
            "Remarks": remarks,
            "QueueTimeOutURL": timeout_url,
            "ResultURL": response_url,
            "Occassion": occasion
        }
        return requests.post(
            self.https_url,
            headers={
                "Authorization": "Bearer {}".format(
                    self.oauth_token),
                "Content-Type": "application/json"},
            data=json.dumps(values))
