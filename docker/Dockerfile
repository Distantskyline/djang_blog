FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /config
ADD requirements.txt /config/
RUN pip install -r /config/requirements.txt
RUN yum install libxml*
RUN pip3 install uwsgi --no-cache-dir

RUN mkdir -p /code/djang_blog
WORKDIR /code/blog
EXPOSE 80
