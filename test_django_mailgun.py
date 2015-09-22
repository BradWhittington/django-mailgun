from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.core.mail import EmailMessage

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


def setUp():
    mb = MailgunBackend(fail_silently=True)
    message = EmailMessage()
    return (mb, message)


def check_output_value(mb, message, test_input, expected_output):
    for k, v in test_input.iteritems():
        message.extra_headers[k] = v
    output = mb._map_smtp_headers_to_api_parameters(message)
    for extra_header in expected_output:
        assert extra_header in output


def test_extra_headers_map():
    mb, message = setUp()
    test_input = {
        'X-Mailgun-Tag': ['Tag 1', 'Tag 2'],
        'X-Mailgun-Campaign-Id': "1",
        'X-Mailgun-Dkim': 'yes',
        'X-Mailgun-Deliver-By': 'Thu, 13 Oct 2011 18:02:00 GMT',
        'X-Mailgun-Drop-Message': 'yes',
        'X-Mailgun-Track': 'yes',
        'X-Mailgun-Track-Clicks': 'htmlonly',
        'X-Mailgun-Track-Opens': 'no',
        'X-Mailgun-Variables': 'my_message_id: 123',
    }
    expected_output = [
        ('o:tag', 'Tag 1'),
        ('o:tag', 'Tag 2'),
        ('o:campaign', '1'),
        ('o:dkim', 'yes'),
        ('o:deliverytime', 'Thu, 13 Oct 2011 18:02:00 GMT'),
        ('o:testmode', 'yes'),
        ('o:tracking', 'yes'),
        ('o:tracking-clicks', 'htmlonly'),
        ('o:tracking-opens', 'no'),
        ('v:my-var', 'my_message_id: 123'),
    ]
    check_output_value(mb, message, test_input, expected_output)
