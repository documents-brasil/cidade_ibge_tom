NAME    := cidade_ibge_tom

.PHONY: lint
lint:
	poetry run flake8 ./cidade_ibge_tom/

.PHONY: mypy
mypy:
	poetry run mypy .

.PHONY: test
test:
	poetry run pytest tests/

.PHONY: coverage
cov:
	poetry run pytest -vv --cov=. tests/
