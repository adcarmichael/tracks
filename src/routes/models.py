from django.db import models
from django.db.models import IntegerField, EmailField, ForeignKey, DateField, BooleanField, CharField
from django.db.models import Model, CASCADE
from django.db.models import OneToOneField
from django.db.models import ImageField, TextField
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Gym(Model):
    email = EmailField(null=False)
    name = CharField(max_length=300)
    city = CharField(max_length=300)
    website = CharField(max_length=300, default='')
    # image = ImageField()
    description = TextField(max_length=300, default='')

    def __str__(self):
        return f'{self.name} in {self.city}'


class RouteSet(Model):
    gym = ForeignKey(Gym, on_delete=CASCADE)
    up_date = DateField(null=False)
    down_date = DateField(null=True)
    zone = CharField(max_length=200, default='')

    def __str__(self):
        return f'{self.gym.name} set on {self.up_date} and down on {self.down_date}. The zone is {self.zone}'


class Route(Model):
    number = IntegerField(
        verbose_name='The number of the route if given e.g. route 6 or 11.', null=True)
    grade = IntegerField(verbose_name='Grade of climbing route')
    grade_sub = IntegerField(
        verbose_name='Optional sub grade of climbing route', null=True, default=0)
    route_set = ForeignKey(RouteSet, on_delete=CASCADE, related_name='routes')

    def __str__(self):
        return f"Number {self.number} of Route Set {self.route_set.id} ({self.route_set}) with grade {self.grade} and sub grade {self.grade_sub}"


class UserProfile(Model):
    user_id = IntegerField()
    level = IntegerField(verbose_name='Climbing level')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

    def __str__(self):
        return "ID:{}, Name:{}".format(self.user.id, self.user.username)


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
    record_type = IntegerField(
        verbose_name='E.g. mastered, climbed, attempted, todo')
    # date_last_failed_attempt = DateField(
    # null=False, auto_now=True, verbose_name='Date of last attempted climb')

    # is_on_sight = models.BooleanField(default=False)

    # climb_count = IntegerField(default=0,
    #    verbose_name='Number of completed climbs')
    # climb_count_failed_attempt = IntegerField(default=0,
    #   verbose_name='Number of attempted climbs (incomplete)')

    class meta:
        unique_together = ('route', 'user',)

    def __str__(self):
        return "Route:{}, User:{}, Record Type:{}".format(self.route, self.user, self.record_type)


class Zone(Model):
    name = CharField(max_length=200)
    gym = ForeignKey(Gym, on_delete=CASCADE)

    def __str__(self):
        return f'"{self.name}" at {self.gym.name}'
