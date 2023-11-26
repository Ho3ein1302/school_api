import re
import os

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def check_phone(value: str) -> str:
    """
    Validate the phone number based on Iranian format
    :param: a string
    :return: True/False
    """
    patter1 = re.compile("^9\d{9}$")
    patter2 = re.compile("^09\d{9}$")
    patter3 = re.compile("^00989\d{9}$")
    patter4 = re.compile("^\+989\d{9}$")

    if bool(patter1.match(value)):
        return "0" + value
    if bool(patter2.match(value)):
        return value
    if bool(patter3.match(value)):
        return "0" + value[4:]
    if bool(patter4.match(value)):
        return "0" + value[3:]

    raise ValidationError(_('The phone number is not valid'))


def check_code_meli(value: str) -> bool:
    return bool(value.isnumeric() and len(value) == 10)


def check_landline_number(value: str):
    if len(value) == 11 and value.startswith('0'):
        return str(value)

    raise ValidationError(_('landline_phone should be 11 character and start with 0'))


def check_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.zip']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
