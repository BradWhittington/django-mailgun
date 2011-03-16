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

Installing mailgun (NB, this is a required step, as the lib is not on pypi)::

    pip install -e git://github.com/mailgun/mailgun.py.git#egg=pymailgun

If you are using python version 2.6 or below, you will need to use the following::
    
    pip install -e git://github.com/bradwhittington/mailgun.py.git@py25#egg=pymailgun

Install django-mailgun::

    pip install -e git://github.com/bradwhittington/django-mailgun.git#egg=django_mailgun 

Add the following to your settings.py::

    EMAIL_BACKEND = 'django_mailgun.MailgunBackend'

    # These are optional -- if they're set as environment variables they won't
    # need to be set here as well
    MAILGUN_ACCESS_KEY = 'ACCESS-KEY'
    # This is optional entirely, mailgun will default to a server if none specified
    MAILGUN_SERVER_NAME = 'SERVER-NAME'

Now, when you use ``django.core.mail.send_mail``, Mailgun will send the messages

Django Builtin-in Error Emails
==============================

If you'd like Django's `Builtin Email Error Reporting`_ to function properly
(actually send working emails), you'll have to explicitly set the
``SERVER_EMAIL`` setting to one of your SES-verified addresses. Otherwise, your
error emails will all fail and you'll be blissfully unaware of a problem.


.. _Builtin Email Error Reporting: http://docs.djangoproject.com/en/1.2/howto/error-reporting/
.. _Django: http://djangoproject.com
.. _Mailgun: http://mailgun.net
