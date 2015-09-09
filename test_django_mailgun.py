from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

from django_mailgun import MailgunBackend
from pytest import raises


def test_no_configuration():

    with raises(ImproperlyConfigured):
        MailgunBackend()


def test_configuration():
    settings.configure(
        MAILGUN_ACCESS_KEY=123,
        MAILGUN_SERVER_NAME='abc'
    )
    MailgunBackend()


def test_marker_methods():
    # Already configured
    mb = MailgunBackend()
    assert mb.open() is None
    assert mb.close() is None
