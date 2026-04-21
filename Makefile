.PHONY: dev start test lint format

dev:
	poetry run fastapi dev src/main.py

start:
	poetry run fastapi run src/main.py

test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run ruff format .
