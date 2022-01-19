FROM nginx:1.20

RUN mkdir /app
RUN mkdir /sock
ADD ./config/nginx/uwsgi_params /etc/nginx/
ADD ./config/nginx/app.conf /etc/nginx/conf.d/default.conf