FROM python:3.9

ENV APP_DIR=/app

RUN mkdir $APP_DIR
RUN mkdir /sock
RUN chmod -R 666 /sock
WORKDIR $APP_DIR
COPY ./config/pip/requirements.txt /tmp/
COPY ./config/uwsgi/uwsgi.ini /etc/
COPY ./app .
RUN pip install -r /tmp/requirements.txt

CMD ["python3"]