build:
	docker-compose build

up:
	docker-compose up -d --build

up-non-daemon:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

down:
	docker-compose down -v

restart:
	docker-compose stop && docker-compose start

django-tests:
	docker-compose run --rm web python manage.py test .

django-createsuperuser:
	docker-compose run --rm web python manage.py createsuperuser

django-migrate:
	docker-compose run --rm web python manage.py migrate

shell-nginx:
	docker exec -ti nginx_container /bin/sh

shell-web:
	docker exec -ti web_container /bin/sh

shell-db:
	docker exec -ti postgres_container /bin/sh

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

log-db:
	docker-compose logs db

collectstatic:
	docker exec dz01 /bin/sh -c "python manage.py collectstatic --noinput"  