FROM python:3.9

RUN mkdir /tz_lexicom

WORKDIR /tz_lexicom

COPY ./requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . .
