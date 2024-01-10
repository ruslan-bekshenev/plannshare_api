FROM python:3.9

RUN mkdir /plannshare_api

WORKDIR /plannshare_api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh