==============
Django-Mailgun
==============
A Django email backend for use with Mailgun


Overview
=================
Django-Mailgun is a drop-in mail backend for Django_.

Getting going
=============

Install django-mailgun::

    pip install django-mailgun

Add the following to your ``settings.py``::

    EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
    MAILGUN_ACCESS_KEY = 'ACCESS-KEY'
    MAILGUN_SERVER_NAME = 'SERVER-NAME'

Replace ``ACCESS-KEY`` with the "API-KEY" value from your Mailgun account details and
``SERVER-NAME`` with the last part of your "API Base URL"
(eg. https://api.mailgun.net/v3/**<your_server_name>**), also found in your Mailgun
account details.

Now, when you use ``django.core.mail.send_mail``, Mailgun will send the messages.

.. _Builtin Email Error Reporting: http://docs.djangoproject.com/en/1.2/howto/error-reporting/
.. _Django: http://djangoproject.com
.. _Mailgun: http://mailgun.net

Extra features
=================

Passing user-specific data
--------------------------

Mailgun also includes the ability to send emails to a group of recipients via a single
API call (https://documentation.mailgun.com/user_manual.html#batch-sending).  To make use of this,
you need to pass Recipient Variables along with your API call.  To do so with Django-Mailgun,
add a valid JSON string to the ``extra_headers`` attribute of ``EmailMessage`` and Django-Mailgun will
remove the string from the headers and send it appropriately.  For example::

    email = EmailMessage('Hi!', 'Cool message for %recipient.first_name%', 'admin@example.com', [joe@example.com, jane@example.com])
    email.extra_headers['recipient_variables'] = '{"joe@example.com":{"first_name":"Joe"}, "jane@example.com":{"first_name":"Jane"}}'
    email.send()

When Jane receives her email, its body should read 'Cool message for Jane', and Joe will see
'Cool message for Joe'.

Analytics and other tracking features
-------------------------------------

Mailgun provides the ability to track certain events that concern your emails. The
API exposes these options (see https://documentation.mailgun.com/api-sending.html#sending).  These
options can also be passed to Mailgun's SMTP server (see "Passing Sending Options" under
https://documentation.mailgun.com/user_manual.html#sending-via-smtp). If you add
any of the SMTP options to the ``extra_headers`` attribute of ``EmailMessage``, Django-Mailgun
will map those values over to the appropriate API parameter. For example::

    email = EmailMessage('Hi!', 'Cool message for Joe', 'admin@example.com', [joe@example.com])
    email.extra_headers['X-Mailgun-Tag'] = ['Tag 1', 'Tag 2']
    email.send()

When the email is sent, it will be tagged with 'Tag 1' and 'Tag 2'. You can provide a string for
any value, or a list or tuple that contains strings for options that can take multiple values.

Attaching data to messages
--------------------------

When sending, you can attach data to your messages by passing custom data to X-Mailgun-Variables header
(see https://documentation.mailgun.com/user_manual.html#attaching-data-to-messages).
Data should be formatted as JSON, and it will be included in any webhook event releated to the email
containing the custom data. For example::

    email = EmailMessage('Hi!', 'Cool message for Joe', 'admin@example.com', [joe@example.com])
    email.extra_headers['X-Mailgun-Variables'] = {'my-id': 'email_id', 'my-variable':'variable'}
    email.send()

Later, you can read this data in your Mailgun webhook handler. For example::

    def mailgun_webhook(request):
        email_id = request.data.get('my-id')
        my_variable = request.data.get('my-variable')

        # Do something with your variables

        return Response(status=status.HTTP_200_OK)

*NOTE*: Django-Mailgun does **NOT**
validate your data for compliance with Mailgun's API; it merely maps over whatever values you provide.  For example,
Mailgun's API states that no more than 3 tags are allowed per email, and each tag must be no greater than
128 characters (https://documentation.mailgun.com/user_manual.html#tagging).  If you provide 4 tags,
or a tag longer than 128 characters, Django-Mailgun will attempt to send such (potentially) invalid
data.  You must ensure what you send is appropriate.

Django Email Backend Reference
================================

* http://docs.djangoproject.com/en/dev/topics/email/#e-mail-backends
