.PHONY: lint docs


test:
	pytest -svx --cov-report term-missing --cov-report html --cov-branch --cov rst2html5/


lint:
	ruff check --diff .
	@echo
	ruff format --diff .
	@echo
	mypy .


format:
	ruff check --silent --exit-zero --fix .
	@echo
	ruff format .


audit:
	pip-audit


docs:
	make -C docs clean
	make -C docs html
