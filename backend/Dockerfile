FROM python:3.8

RUN mkdir /workspace

WORKDIR /workspace

COPY ./ /workspace

RUN pip install -r requirements.txt

RUN python manage.py migrate