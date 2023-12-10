import re


def is_valid_email(email):
    """
    Function for verify is str is email
    :param:
    :return: True or False
    """
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return bool(re.match(email_pattern, email))


def is_valid_phone_number(phone_number):
    """
    Function  for validating a phone number
    :param phone_number:
    :return: True or False
    """
    phone_pattern = re.compile(r"^\+?[0-9]{1,4}[\s\-]?\(?\d{1,4}\)?[\s\-]?\d{1,10}$")
    return bool(re.match(phone_pattern, phone_number))
