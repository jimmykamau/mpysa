import pympesa


class BaseMPesa(object):
    """Base class for most requests"""

    def __init__(self):
        self.base_values = {
            "SecurityCredential": pympesa.SECURITY_CREDENTIAL,
            "PartyA": pympesa.BUSINESS_SHORTCODE,
            "QueueTimeOutURL": pympesa.BASE_RESPONSE_ENDPOINT,
            "ResultURL": pympesa.BASE_RESPONSE_ENDPOINT
        }

    def get_b2c_values(
            self, command_id, amount, receiver_msisdn, remarks,
            timeout_url, response_url, occasion):
        b2c_extras = {
            "InitiatorName": pympesa.INITIATOR_NAME,
            "CommandID": command_id,
            "Amount": amount,
            "PartyB": receiver_msisdn,
            "Remarks": remarks,
            "QueueTimeOutURL": timeout_url,
            "ResultURL": response_url,
            "Occassion": occasion
        }
        return dict(self.base_values, **b2c_extras)
