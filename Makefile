pip-upgrade:
	pip install --upgrade pip

pip-install:
	pip install -r requirements.txt

dev:
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8080

docker-build:
	docker build --tag identifile:latest .

docker-start:
	docker run -d --name identifile -p 8079:8079 identifile:latest

.PHONY: upgrade-pip pip-install dev docker-build docker-start