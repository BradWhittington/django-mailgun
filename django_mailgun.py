from __future__ import unicode_literals

import requests
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import sanitize_address

from requests.packages.urllib3.filepost import encode_multipart_formdata


class MailgunAPIError(Exception):
    pass


class MailgunBackend(BaseEmailBackend):
    """A Django Email backend that uses mailgun.
    """

    def __init__(self, fail_silently=False, *args, **kwargs):
        access_key, server_name = (kwargs.pop('access_key', None),
                                   kwargs.pop('server_name', None))

        super(MailgunBackend, self).__init__(
            fail_silently=fail_silently,
            *args, **kwargs)

        try:
            self._access_key = access_key or getattr(settings, 'MAILGUN_ACCESS_KEY')
            self._server_name = server_name or getattr(settings, 'MAILGUN_SERVER_NAME')
        except AttributeError:
            if fail_silently:
                self._access_key, self._server_name = None
            else:
                raise

        self._api_url = "https://api.mailgun.net/v3/%s/" % self._server_name

    def open(self):
        """Stub for open connection, all sends are done over HTTP POSTs
        """
        pass

    def close(self):
        """Close any open HTTP connections to the API server.
        """
        pass

    def _send(self, email_message):
        """A helper method that does the actual sending."""
        if not email_message.recipients():
            return False
        from_email = sanitize_address(email_message.from_email, email_message.encoding)
        recipients = [sanitize_address(addr, email_message.encoding)
                      for addr in email_message.recipients()]

        try:

            post_data = []
            post_data.append(('to', (",".join(recipients)),))
            post_data.append(('text', email_message.body,))
            post_data.append(('subject', email_message.subject,))
            post_data.append(('from', from_email,))
            # get our recipient variables if they were passed in
            recipient_variables = email_message.extra_headers.pop('recipient_variables', None)
            if recipient_variables is not None:
                post_data.append(('recipient-variables', recipient_variables, ))

            if hasattr(email_message, 'alternatives') and email_message.alternatives:
                for alt in email_message.alternatives:
                    if alt[1] == 'text/html':
                        post_data.append(('html', alt[0],))
                        break

            if email_message.attachments:
                for attachment in email_message.attachments:
                    post_data.append(('attachment', (attachment[0], attachment[1],)))
                content, header = encode_multipart_formdata(post_data)
                headers = {'Content-Type': header}
            else:
                content = post_data
                headers = None

            response = requests.post(self._api_url + "messages",
                auth=("api", self._access_key),
                data=content, headers=headers)
        except:
            if not self.fail_silently:
                raise
            return False

        if response.status_code != 200:
            if not self.fail_silently:
                raise MailgunAPIError(response)
            return False

        return True

    def send_messages(self, email_messages):
        """Sends one or more EmailMessage objects and returns the number of
        email messages sent.
        """
        if not email_messages:
            return

        num_sent = 0
        for message in email_messages:
            if self._send(message):
                num_sent += 1

        return num_sent
