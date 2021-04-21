.PHONY: lint docs


test: lint
	pytest -svx --cov-report term-missing --cov-report html --cov-branch --cov src/


lint:
	isort --diff -c .
	flake8 .
	blue --check --diff .
	mypy .


format:
	isort .
	blue .


docs:
	make -C docs clean
	make -C docs html
