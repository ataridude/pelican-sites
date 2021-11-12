FROM python:3 AS builder
WORKDIR /usr/src/app

ARG SITE

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN apt update && apt -y install python3-lxml
RUN apt install git && \
    git clone https://github.com/getpelican/pelican-plugins.git pelican-plugins && \
    git clone https://github.com/ataridude/pelican_theme.git theme && \
    mkdir -p /usr/local/pelican-plugins && \
    git clone https://github.com/ataridude/pelican_tipue_search.git /usr/local/pelican-plugins/tipue_search

ADD sites/$SITE/content ./content
COPY sites/$SITE/pelicanconf.py ./
RUN pelican /usr/src/app/content/ -s pelicanconf.py

FROM nginx:latest
COPY --from=0 /usr/src/app/output /usr/share/nginx/html
