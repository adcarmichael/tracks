from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from routes.models import Profile, RouteSet, Gym
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def check_user_credentials(request, user_id):
    return request.user.is_authenticated and is_username_match_user_id(request.user, user_id)


def get_user_id_from_username(username):
    query = User.objects.get(username=username)
    if query:
        user_id = query.pk
    else:
        user_id = []
    return user_id


def is_username_match_user_id(username, user_id):
    prof = Profile.objects.get(id=user_id)

    if prof:
        is_user = str(username) == str(prof.user.username)
    else:
        is_user = False

    return is_user


def render_with_user_restriction(request, html, data, user_id):
    if not is_username_match_user_id(request.user, user_id):
        response = HttpResponseForbidden()
        return response
    else:
        return render(request, html, data)


class Validate:

    def gym(self, gym_id):
        return Gym.objects.filter(id=gym_id).exists()

    def username(self, user_id):
        return self._check_query(User.objects.get(id=user_id))

    def _check_query(self, query):
        if query:
            return True
        else:
            return False
