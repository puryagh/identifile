FROM python:3.9-slim AS builder

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

RUN mkdir /data
RUN groupadd -r identifile && useradd -r -g identifile identifile
RUN chown -R identifile:identifile /app
RUN chown -R identifile:identifile /data

USER identifile

EXPOSE 8079

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8079"]