from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from routes.models import Profile, RouteSet,Gym
from django.shortcuts import render, redirect

def check_user_credentials(request,user_id):
    return request.user.is_authenticated and is_username_match_user_id(request.user, user_id)

def is_username_match_user_id(username, user_id):
    prof = Profile.objects.get(id=user_id)
    return str(username) == str(prof.user.username)


def render_with_user_restriction(request, html, data, user_id):
    if not is_username_match_user_id(request.user, user_id):
        response = HttpResponseForbidden()
        return response
    else:
        return render(request, html, data)

class Validate:
    
    def gym(self,gym_id):
        return self._check_query(Gym.objects.get(id = gym_id))
        
    def _check_query(self,query):
        if query:
            return True
        else:
            return False