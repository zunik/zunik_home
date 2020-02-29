FROM python:3.6.6

MAINTAINER Zunik <chazunik@gmail.com>

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && apt-get install -y npm

COPY ./app /zunik_home/app

WORKDIR /zunik_home/app

ARG SECRET_KEY
ARG DEBUG
ARG DB_HOST
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
ARG SITE_DOMAIN
ARG ALLOWED_HOSTS
ARG DISQUS_WEBSITE_SHORTNAME

ENV SECRET_KEY=${SECRET_KEY} \
    DEBUG=${DEBUG} \
    DB_HOST=${DB_HOST} \
    DB_NAME=${DB_NAME} \
    DB_USER=${DB_USER} \
    DB_PASSWORD=${DB_PASSWORD} \
    SITE_DOMAIN=${SITE_DOMAIN} \
    ALLOWED_HOSTS=${ALLOWED_HOSTS} \
    DISQUS_WEBSITE_SHORTNAME=${DISQUS_WEBSITE_SHORTNAME}

ENV TZ Asia/Seoul

RUN pip install -r requirements.txt
RUN npm install -g bower && npm install
RUN python manage.py bower_install --allow-root

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "zunik_home.wsgi:application"]