# Development setup
pip-upgrade:
	pip install --upgrade pip

pip-install:
	pip install -r requirements.txt

pip-install-dev: pip-install
	pip install -e .

# Development server
dev:
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8080

# Docker commands
docker-build:
	docker build --tag identifile:latest .

docker-start:
	docker run -d --name identifile -p 8079:8079 identifile:latest

docker-stop:
	docker stop identifile
	docker rm identifile

# Testing and code quality
test:
	pytest

test-cov:
	pytest --cov=src --cov-report=term --cov-report=html

lint:
	flake8 src tests

format:
	black src tests
	isort src tests

type-check:
	mypy src tests

check: lint type-check test

# Clean up
clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov .mypy_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

.PHONY: pip-upgrade pip-install pip-install-dev dev docker-build docker-start docker-stop test test-cov lint format type-check check clean