FROM postgres:14

COPY ./config/db/db_config.sh /docker-entrypoint-initdb.d/db_config.sh
RUN chmod 755 /docker-entrypoint-initdb.d/db_config.sh