run:
	docker-compose up -d

stop:
	docker-compose stop

restart:
	docker-compose restart

migrate:
	docker-compose run --rm app python manage.py migrate

makemi:
	docker-compose run --rm app python manage.py makemigrations

collect:
	docker-compose run --rm app python manage.py collectstatic --noinput -l