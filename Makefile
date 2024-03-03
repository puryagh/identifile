pip-upgrade:
	pip install --upgrade pip

pip-install:
	pip install -r requirements.txt

dev:
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8080

docker-build:
	docker build --tag identifile-pro:latest .

run:
	docker run -d --name identifile-pro -p 8079:8079 identifile-pro:latest

.PHONY: start upgrade-pip