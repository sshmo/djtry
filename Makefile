test:
	pytest -svv --log-cli-level=INFO --cov=djtry/ tests/ --hypothesis-show-statistics

dev:
	pre-commit run -a
	mypy . --check-untyped-defs
	pytype .
	radon cc -a -nb .
	pytest -svv --log-cli-level=INFO --cov=djtry/ tests/ --hypothesis-show-statistics
