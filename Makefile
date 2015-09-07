test:
	py.test --cov=django_mailgun --cov-report html
	open htmlcov/index.html
