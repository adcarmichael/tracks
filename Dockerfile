FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /src
RUN mkdir /static
WORKDIR /src
ADD ./src /src

# install psycopg2
RUN apk update \
    && apk add gcc python3-dev musl-dev \
    && apk add postgresql-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python manage.py collectstatic --no-input;python manage.py migrate; gunicorn tracks.wsgi -b 0.0.0.0:8000
