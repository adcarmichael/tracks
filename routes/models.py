from django.db import models
from django.db.models import IntegerField, ForeignKey, DateField, BooleanField, CharField
from django.db.models import Model, CASCADE
from django.db.models import OneToOneField
from datetime import date
from django.utils import timezone

# Create your models here.
class RouteSet(Model):
    up_date = DateField(null=False, default=timezone.now(),
                        verbose_name='This is the date that the route set was available')
    down_date = DateField(null=True, verbose_name='This is the date that the route set was taken down')
    is_active = BooleanField(default=False, verbose_name='Is the set active.', null=False)

    def __str__(self):
        return "{} {} {}".format(self.up_date, self.down_date, self.is_active)


class Route(Model):
    grade = IntegerField(verbose_name='Grade of climbing route')
    grade_sub = IntegerField(verbose_name='Optional sub grade of climbing route', null=True, default=0)
    route_set = ForeignKey(RouteSet, on_delete=CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.grade, self.grade_sub, self.route_set)

""" 
The Profile class which OnetoOnes with django user model and reciever decoraters were taken from 
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
"""
class Profile(Model):
    user_id = IntegerField()
    level = IntegerField(verbose_name='Climbing level')


class RouteRecord(Model):
    route_id = ForeignKey(Route, on_delete=CASCADE)
    user = ForeignKey(Profile, on_delete=CASCADE)
    status = IntegerField(verbose_name='E.g. mastered, climbed, attempted, todo')
