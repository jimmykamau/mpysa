import mpysa


class BaseMPesa(object):
    """Base class for most requests"""

    def __init__(self, oauth_token, https_url):
        self.oauth_token = oauth_token
        self.https_url = https_url
        self.base_values = {
            "SecurityCredential": mpysa.SECURITY_CREDENTIAL,
            "PartyA": mpysa.BUSINESS_SHORTCODE,
            "QueueTimeOutURL": mpysa.BASE_RESPONSE_ENDPOINT,
            "ResultURL": mpysa.BASE_RESPONSE_ENDPOINT
        }

    def get_b2c_values(
            self, command_id, amount, receiver_msisdn, remarks,
            timeout_url, response_url, occasion):
        b2c_extras = {
            "InitiatorName": mpysa.INITIATOR_NAME,
            "CommandID": command_id,
            "Amount": amount,
            "PartyB": receiver_msisdn,
            "Remarks": remarks,
            "QueueTimeOutURL": timeout_url,
            "ResultURL": response_url,
            "Occassion": occasion
        }
        return dict(self.base_values, **b2c_extras)

    def get_b2b_values(
            self, command_id, receiver_id_type, amount,
            receiver_account_number, transaction_reference,
            remarks, timeout_url, response_url):
        b2b_extras = {
            "Initiator": mpysa.INITIATOR_NAME,
            "CommandID": command_id,
            "SenderIdentifierType": "4",
            "RecieverIdentifierType": receiver_id_type,
            "Amount": amount,
            "PartyB": receiver_account_number,
            "AccountReference": transaction_reference,
            "Remarks": remarks,
            "QueueTimeOutURL": timeout_url,
            "ResultURL": response_url
        }
        return dict(self.base_values, **b2b_extras)
