import datetime
from django.db.models.functions import Cast, Coalesce
from django.db.models import DateField
from datetime import datetime
from routes.models import RouteSet, Route, RouteRecord, Profile, Gym, Gym2, RouteSet2
from django.db.models import Model, CASCADE
import django
import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'tracks.settings'
django.setup()

gym = Gym(name='eden', email='asdf@esd.com', gym_key='asd')
gym.save()

# g = Gym.objects.all()[1]

up_date = '03/06/2019'
up_date = datetime.strptime(up_date, "%d/%m/%Y").date()
up_date = Cast(up_date, DateField)
up_date = datetime.date.today()
rs = RouteSet(up_date=up_date)
rs.gym = gym

# from django.db.models import Model, CASCADE
# from django.db.models import IntegerField, EmailField, ForeignKey, DateField, BooleanField, CharField

# class Gym2(Model):
#     key = CharField(max_length=10)


# class RouteSet2(Model):
#     gym = ForeignKey(Gym, on_delete=CASCADE)
#     up_date = DateField(null=False, verbose_name='This it was available')

d = datetime.date.today()
g = Gym2(key='asd', email='why@me.com', name='123')
g.save()
rs = RouteSet2(gym=g, date=d)
rs.save()
