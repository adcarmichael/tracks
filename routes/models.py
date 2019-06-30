from django.db import models
from django.db.models import IntegerField, ForeignKey, DateField, BooleanField, CharField
from django.db.models import Model, CASCADE
from django.db.models import OneToOneField
from datetime import date
from django.utils import timezone


class RouteSet(Model):
    up_date = DateField(null=False,
                        verbose_name='This is the date that the route set was available')
    down_date = DateField(
        null=True, verbose_name='This is the date that the route set was taken down', default=date(2000, 1, 1))

    def __str__(self):
        return "{} {}".format(self.up_date, self.down_date)


class Route(Model):
    number = IntegerField(
        verbose_name='The number of the route if given e.g. route 6 or 11.', null=True)
    grade = IntegerField(verbose_name='Grade of climbing route')
    grade_sub = IntegerField(
        verbose_name='Optional sub grade of climbing route', null=True, default=0)
    route_set = ForeignKey(RouteSet, on_delete=CASCADE, related_name='routes')

    def __str__(self):
        return "{} {} {}".format(self.grade, self.grade_sub, self.route_set)


class Profile(Model):
    user_id = IntegerField()
    level = IntegerField(verbose_name='Climbing level')


class RouteRecord(Model):
    route = ForeignKey(Route, on_delete=CASCADE)
    user = ForeignKey(Profile, on_delete=CASCADE)
    status = IntegerField(
        verbose_name='E.g. mastered, climbed, attempted, todo')
