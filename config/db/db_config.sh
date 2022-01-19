psql --username "$POSTGRES_USER" -c "CREATE DATABASE $DB_NAME"
psql --username "$POSTGRES_USER" -c "CREATE USER $DB_USER WITH password '$DB_USER_PASSWORD'"
psql --username "$POSTGRES_USER" -d "$DB_NAME" -c "create schema authorization $DB_SCHEMA"