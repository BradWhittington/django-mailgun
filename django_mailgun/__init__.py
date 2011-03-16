from django.conf import settings
from mailgun import Mailgun, MailgunMessage
from django.core.mail.backends.base import BaseEmailBackend

class MailgunBackend(BaseEmailBackend):
    """A Django Email backend that uses mailgun.
    """

    def __init__(self, fail_silently=False, *args, **kwargs):
        super(MailgunBackend, self).__init__(fail_silently=fail_silently, *args,
                                         **kwargs)

        self._access_key = getattr(settings, 'MAILGUN_ACCESS_KEY', None)
        self._server_name = getattr(settings, 'MAILGUN_SERVER_NAME', '')
        Mailgun.init(self._access_key)

    def open(self):
        """Stub for open connection, all sends are done over HTTP POSTs
        """
        pass

    def close(self):
        """Close any open HTTP connections to the API server.
        """
        pass

    def send_messages(self, email_messages):
        """Sends one or more EmailMessage objects and returns the number of
        email messages sent.
        """
        if not email_messages:
            return

        num_sent = 0
        for message in email_messages:
            try:
                response = MailgunMessage.send_raw(
                    sender=message.from_email,
                    recipients=message.recipients(),
                    mime_body=message.message().as_string(),
                    servername=self._server_name
                )

                #TODO: mailgun's send_raw doesn't return the response, which would be useful for the following:
                #message.extra_headers['Message-Id'] = send_result['MessageId']

                num_sent += 1
            except Exception, e:
                if not self.fail_silently:
                    raise
                pass

        return num_sent

