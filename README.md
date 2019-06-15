# tracks

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
