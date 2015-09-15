==========
Django-Mailgun
==========
:Info: A Django email backend for use with Mailgun
:Author: Bradley Whittington (http://github.com/bradwhittington, http://twitter.com/darb)

This README is derived from https://github.com/hmarr/django-ses/blob/master/README.rst

Overview
=================
Django-Mailgun is a drop-in mail backend for Django_, 
per http://docs.djangoproject.com/en/dev/topics/email/#e-mail-backends

Getting going
=============

Install django-mailgun::

    pip install django-mailgun

Add the following to your settings.py::

    EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
    MAILGUN_ACCESS_KEY = 'ACCESS-KEY'
    MAILGUN_SERVER_NAME = 'SERVER-NAME'

Now, when you use ``django.core.mail.send_mail``, Mailgun will send the messages.

.. _Builtin Email Error Reporting: http://docs.djangoproject.com/en/1.2/howto/error-reporting/
.. _Django: http://djangoproject.com
.. _Mailgun: http://mailgun.net

Mailgun also includes the ability to send emails to a group of recipients via a single
API call (https://documentation.mailgun.com/user_manual.html#batch-sending).  To make use of this,
you need to pass Recipient Variables along with your API call.  To do so with Django-Mailgun,
add a valid json string to the `extra_headers` attribute of EmailMessage and Django-Mailgun will
remove the string from the headers and send it appropriately.  For example::

    email = EmailMessage('Hi!', 'Cool message for %recipient.first_name%', 'admin@example.com', [joe@example.com, jane@example.com])
    email.extra_headers['recipient_variables'] = '{"joe@example.com":{"first_name":"Joe"}, "jane@example.com":{"first_name":"Jane"}}'
    email.send()

When Jane receives her email, its body should read 'Cool message for Jane', and Joe will see
'Cool messagae for Joe'.