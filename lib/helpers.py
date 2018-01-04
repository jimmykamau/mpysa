import base64


def generate_auth_string(consumer_key, consumer_secret):
    auth_string = consumer_key + ":" + consumer_secret
    return base64.b64encode(auth_string.encode('utf-8'))


def get_id_type(id_string):
    if id_string == "Phone number":
        return "1"
    if id_string == "Till number":
        return "2"
    if id_string == "Organization":
        return "4"
