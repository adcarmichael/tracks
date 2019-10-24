# tracks
[![Build Status](https://travis-ci.org/adcarmichael/tracks.svg?branch=master)](https://travis-ci.org/adcarmichael/tracks)
## Accessing Django ORM outwith Django Framework
https://stackoverflow.com/questions/34300513/using-django-model-outside-of-the-django-framework

import django
import sys
import os

sys.path.append(os.path.abspath("/home/pi/garageMonitor/django/garageMonitor"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'tracks.settings'
django.setup()
import models
    config = models.SystemConfiguration.objects.filter(idSystemConfiguration=1)
    config = config[0]
    for x in config.__dict__:
      print x

## Env Variables
Secrets are injected into the docker containers through docker-compose. docker-compose.yaml expects a file called .env to be at the root of the repo:

  DEBUG=1
  SECRET_KEY=foo
  DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

  SQL_ENGINE=django.db.backends.postgresql
  SQL_DATABASE=tracks
  SQL_USER=admin
  SQL_PASSWORD=password
  SQL_HOST=db
  SQL_PORT=5432

  POSTGRES_USER=admin
  POSTGRES_PASSWORD=password
  POSTGRES_DB=tracks

  EMAIL_USE_TLS=true
  EMAIL_HOST=smtp.mailtrap.io
  EMAIL_HOST_USER=userrname
  EMAIL_HOST_PASSWORD=password
  EMAIL_PORT=587
  EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend

Note that the above POSTGRES_* variables are interpreted by the postgres container on build and are used to create the user.

## Email Signup
Taken from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

## For authentication (login lohout etc)
https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/


## Nuke Docker
Use sparingly... 

  docker system prune --volumes
  docker image prune -a  
  docker volume prune 
  docker container prune 
[Resource](https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/)

## Test User
username = test_user
password = test_password

## SSL Certification
from https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx
Then execlent guide from https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04 allowed me to set up nginx config to have chalktracks domain

Had issues with nginx not starting found solution from (https://www.digitalocean.com/community/questions/can-t-start-nginx-job-for-nginx-service-failed)

  Try to run the following two commands:
  sudo fuser -k 80/tcp
  sudo fuser -k 443/tcp
  Then execute
  sudo service nginx restart
  https://stackoverflow.com/questions/35868976/nginx-not-started-and-cant-start/51684856#51684856