FROM python:3

RUN useradd -ms /bin/bahs django

USER django

ENV PYTHONUNBUFFERED 1

WORKDIR /home/django/app

ENV PATH $PATH:/home/django/.local/bin

COPY requirements.txt /home/django/app

RUN pip install -r requirements.txt

COPY . /home/django/app

