from django.core.exceptions import ImproperlyConfigured

from django_mailgun import MailgunBackend
from pytest import raises


def test_configuration():
    with raises(ImproperlyConfigured):
        MailgunBackend()
