from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

from routes.models import Profile
from routes import services
from routes.forms import SignUpForm
from routes.tokens import account_activation_token


dal = services.get_dal()


def home_page(request):
    return render(request, 'home_page.html')


def add_route_set(request, details):
    pass


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def get_route_date_for_routes_page():

    data_black = dal.get_route_set_of_colour('black')
    black = zip(data_black.get_number(),
                data_black.get_colour())
    data = {
        'purple': dal.get_route_set_of_colour('purple'),
        'orange': dal.get_route_set_of_colour('orange'),
        'green': dal.get_route_set_of_colour('green'),
        'yellow': dal.get_route_set_of_colour('yellow'),
        'blue': dal.get_route_set_of_colour('blue'),
        'white': dal.get_route_set_of_colour('white'),
        'red': dal.get_route_set_of_colour('red'),
        'black': black}
    return data


def routes_page(request):
    data = get_route_date_for_routes_page()
    return render(request, 'routes.html', data)


def routes_user_page(request, user_id):
    data = get_route_date_for_routes_page()
    return render_with_user_restriction(request, 'routes_user.html', data, user_id)


def does_username_match_user_id(username, user_id):
    prof = Profile.objects.get(id=user_id)
    return str(username) == str(prof.user.username)


def render_with_user_restriction(request, html, data, user_id):
    if not does_username_match_user_id(request.user, user_id):
        response = HttpResponseForbidden()
        return response
    else:
        return render(request, 'routes_user.html', data)
