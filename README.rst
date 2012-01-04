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

Now, when you use ``django.core.mail.send_mail``, Mailgun will send the messages

.. _Builtin Email Error Reporting: http://docs.djangoproject.com/en/1.2/howto/error-reporting/
.. _Django: http://djangoproject.com
.. _Mailgun: http://mailgun.net
