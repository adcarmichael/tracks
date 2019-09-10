from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

from routes.models import Profile
import routes.services.dal as Dal
from routes.forms import SignUpForm, GymCreateForm
from routes.tokens import account_activation_token
from routes.services.conf import GymKey
from .forms import AddRouteSetForm_Eden
import routes.services.utils as util
from routes.services.conf import GradeSub, Grade
from routes.services import conf as conf
dal = Dal.get_dal(GymKey.eden_rock_edinburgh)


def home_page(request):
    return render(request, 'home_page.html')


def add_route_set(request, details):
    pass


def gyms_page(request):
    gym_data = dal.get_gym_all()
    gym = zip(gym_data.get_id(),
              gym_data.get_name(),
              gym_data.get_city(),
              gym_data.get_email())

    return render(request, 'gyms_page.html', {'gym': gym})


def gyms_add(request):
    # Adding gyms is restricted to
    if request.user.is_superuser:
        if request.method == 'POST':
            form = GymCreateForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['Name']
                email = form.cleaned_data['Email']
                city = form.cleaned_data['City']
                dal.create_gym(name, email, city)
                return HttpResponseRedirect('/')

        else:
            form = GymCreateForm()
        return render(request, 'gym_add_page.html', {'form': form})
    else:
        return HttpResponseForbidden()


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


def get_route_date_for_routes_page(gym_id):

    data_black = dal.get_route_set_of_grade('black', gym_id=gym_id)
    black = zip(data_black.get_number(),
                data_black.get_grade())
    data = {
        'purple': dal.get_route_set_of_grade('purple'),
        'orange': dal.get_route_set_of_grade('orange'),
        'green': dal.get_route_set_of_grade('green'),
        'yellow': dal.get_route_set_of_grade('yellow'),
        'blue': dal.get_route_set_of_grade('blue'),
        'white': dal.get_route_set_of_grade('white'),
        'red': dal.get_route_set_of_grade('red'),
        'black': black}
    return data


def routes_page(request, gym_id):
    data = get_route_date_for_routes_page()
    return render(request, 'routes.html', data)


def test_page(request):
    CHOICES_grade_sub = [(e.value, e.name) for e in GradeSub]
    CHOICES_grade = [(e.value, e.name) for e in Grade]
    grade_data = zip(CHOICES_grade, CHOICES_grade_sub)
    data = {'grade_data': grade_data}
    if request.method == 'POST':
        pass

    else:
        pass
    return render(request, 'test_page.html', data)


def route_set_add_page(request, gym_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AddRouteSetForm_Eden(request.POST)

            if form.is_valid():
                grade = int(form.cleaned_data['grade'])
                up_date = form.cleaned_data['up_date']
                down_date = form.cleaned_data['down_date']
                grade_sub = []
                number = []

                for ind, field in enumerate(form.fields):
                    if 'grade_sub' in field:
                        grade_sub_temp = int(form.cleaned_data[field])
                        if grade_sub_temp != 0:
                            grade_sub.append(grade_sub_temp)
                            number.append(ind)

                dal._create_route_set_for_list_of_grade_sub(
                    gym_id, grade, grade_sub, up_date, down_date=down_date)
                return HttpResponseRedirect('/')
        else:
            form = AddRouteSetForm_Eden()
        return render(request, 'route_set_add_page.html', {'form': form})
    else:
        return HttpResponseForbidden()


def routes_user_page(request, user_id, gym_id):
    route_data_all = dal.get_route_set_of_grade('purple', gym_id=gym_id)
    route_record = dal.get_route_record_for_user(
        user_id, route_data_all.get_route_id())

    grade = route_data_all.get_grade()
    sub_grade = route_data_all.get_grade_sub()
    route_id = route_data_all.get_route_id()
    grade_names = conf.get_grade_names()
    grade_sub_names = get_grade_sub_names_clean()
    active_grade = get_active_grade_for_filter(user_id, gym_id)

    route_data = zip(route_id,
                     route_data_all.get_number(),
                     grade,
                     sub_grade,
                     get_grade_hex_colour(grade),
                     get_sub_grade_icon_class(sub_grade),
                     route_record['is_climbed'],
                     route_record['date'])

    # data = get_route_date_for_routes_page(gym_id)
    data = {'route_data': route_data,
            'user_id': user_id,
            'gym_id': gym_id,
            'active_grade': active_grade,
            'grade_names': grade_names,
            'grade_sub_names': grade_sub_names}

    return render_with_user_restriction(request, 'routes_user.html', data, user_id)


def get_active_grade_for_filter(user_id, gym_id):
    dal.get_grade_of_last_recorded_climb(user_id, gym_id)
    return 'purple'


def get_grade_sub_names_clean():
    grade_sub_names = conf.get_grade_sub_names()
    if 'null' in grade_sub_names:
        grade_sub_names.remove('null')
    return grade_sub_names


def record_route(request, user_id, gym_id, route_id):
    dal.set_route_record_for_user(
        user_id, route_id, conf.ClimbStatus.climbed.value, True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def get_grade_hex_colour(grade_list):
    class_text = []
    # Colours came from https://htmlcolorcodes.com/
    for grade in grade_list:

        if grade == 'purple':
            class_text.append('#A569BD')
        elif grade == 'orange':
            class_text.append('#E67E22')
        elif grade == 'green':
            class_text.append('#58D68D')
        elif grade == 'yellow':
            class_text.append('#F1C40F')
        elif grade == 'blue':
            class_text.append('#3498DB')
        elif grade == 'white':
            class_text.append('#D0D3D4')
        elif grade == 'black':
            class_text.append('#34495E')
        elif grade == 'red':
            class_text.append('#E74C3C')
        else:
            class_text.append('#784212')
    return class_text


def get_sub_grade_icon_class(sub_grade_list):
    class_text = []

    for sub_grade in sub_grade_list:
        class_text.append(conf.GradeSubIcon.get_value_from_name(sub_grade))

    return class_text


def is_username_match_user_id(username, user_id):
    prof = Profile.objects.get(id=user_id)
    return str(username) == str(prof.user.username)


def render_with_user_restriction(request, html, data, user_id):
    if not is_username_match_user_id(request.user, user_id):
        response = HttpResponseForbidden()
        return response
    else:
        return render(request, 'routes_user.html', data)
