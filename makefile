run:
	docker-compose up -d

stop:
	docker-compose stop

build:
	docker-compose build

restart:
	docker-compose restart

migrate:
	docker-compose run --rm web python manage.py migrate

makemi:
	docker-compose run --rm web python manage.py makemigrations

collect:
	docker-compose run --rm web python manage.py collectstatic --noinput -l

#pip:
#	docker-compose run --rm web pip install -r /tmp/requirements.txt
