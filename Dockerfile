FROM python:3.9

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY . .

RUN python3 -m pip install -r requirements.txt
