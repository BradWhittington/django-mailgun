test:
	py.test test_django_mailgun.py --cov=django_mailgun --cov-report html
	open htmlcov/index.html
