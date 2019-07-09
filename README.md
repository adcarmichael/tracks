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

## Email Signup
Taken from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

## For authentication (login lohout etc)
https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/