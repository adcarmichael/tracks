from django.db import models
from django.db.models import IntegerField, EmailField, ForeignKey, DateField, BooleanField, CharField
from django.db.models import Model, CASCADE
from django.db.models import OneToOneField
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Gym(Model):
    email = EmailField(null=False)
    name = CharField(max_length=300)
    city = CharField(max_length=300)
    # website = CharField(max_length=300)


class RouteSet(Model):
    gym = ForeignKey(Gym, on_delete=CASCADE)
    up_date = DateField(null=False)
    down_date = DateField(null=True)

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


class UserProfile(Model):
    user_id = IntegerField()
    level = IntegerField(verbose_name='Climbing level')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class RouteRecord(Model):
    route = ForeignKey(Route, on_delete=CASCADE)
    user = ForeignKey(Profile, on_delete=CASCADE)
    date = DateField(null=False, auto_now=True,
                     verbose_name='Date of completed climb')
    # date_last_failed_attempt = DateField(
    # null=False, auto_now=True, verbose_name='Date of last attempted climb')

    status = IntegerField(
        verbose_name='E.g. mastered, climbed, attempted, todo')
    is_climbed = models.BooleanField(default=False)
    # is_on_sight = models.BooleanField(default=False)

    # climb_count = IntegerField(default=0,
    #    verbose_name='Number of completed climbs')
    # climb_count_failed_attempt = IntegerField(default=0,
    #   verbose_name='Number of attempted climbs (incomplete)')

    class meta:
        unique_together = ('route', 'user',)