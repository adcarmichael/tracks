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

from routes.models import Profile, RouteSet
import routes.services.dal as Dal
from routes.forms import SignUpForm, GymCreateForm
from routes.tokens import account_activation_token
from routes.services.conf import GymKey
import routes.services.records as rec
from routes import services
from routes.services import metrics

from .forms import AddRouteSetForm_Eden, RouteSetForm
import routes.services.utils as util
from routes.services.conf import GradeSub, Grade
from routes.services import conf as conf
from datetime import datetime

from routes.services import security

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


def get_route_data_for_routes_page(gym_id):

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
    data = get_route_data_for_routes_page()
    
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


def route_set_page(request, gym_id):

    gym_query = dal.get_gym(gym_id)
    if gym_query and request.user.is_superuser:

        data_dict = dal.get_route_set_data(gym_id)

        is_active = list(map(check_if_active_dates,
                             data_dict['up_date'],
                             data_dict['down_date']))

        data = zip(data_dict['id'], data_dict['up_date'],
                   data_dict['down_date'], data_dict['num_routes'], is_active)

        context = {'route_set_data': data,
                   'gym_id': gym_id, 'gym_name': gym_query.name}

        return render(request, 'route_set.html', context)
    else:
        return HttpResponseForbidden()


def check_if_active_dates(up_date, down_date):
    is_active = up_date < datetime.now().date() < down_date
    return is_active


def route_set_add_page(request, gym_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AddRouteSetForm_Eden(request.POST)

            if form.is_valid():
                process_route_set_form(form, gym_id)
                return HttpResponseRedirect('/')
        else:
            form = AddRouteSetForm_Eden()
        return render(request, 'route_set_add_page.html', {'form': form})
    else:
        return HttpResponseForbidden()


def route_set_update_page(request, gym_id, route_set_id):
    rs = RouteSet.objects.get(pk=route_set_id)
    if rs and request.user.is_superuser:
        if request.method == 'POST':
            form = RouteSetForm(request.POST)

            if form.is_valid():
                up_date = form.cleaned_data['up_date']
                down_date = form.cleaned_data['down_date']
                rs = RouteSet.objects.get(pk=route_set_id)
                if rs:
                    rs.up_date = up_date
                    rs.down_date = down_date
                    rs.save()

                return HttpResponseRedirect(f'/gyms/{gym_id}/routes/set')
        else:

            init_form = {'up_date': rs.up_date, 'down_date': rs.down_date}

            form = RouteSetForm(initial=init_form)
        return render(request, 'route_set_update.html', {'form': form, 'route_set_id': route_set_id})
    else:
        return HttpResponseForbidden()


def get_init_route_set_form_data(route_set_id):
    query = RouteSet.objects.get(pk=route_set_id)
    query_routes = query.routes.order_by('number').all()

    data = {'up_date': query.up_date, 'down_date': query.down_date}
    for ind in range(len(query_routes)):
        field_name = f'grade_sub_{ind}'
        data[field_name] = query_routes[ind].grade_sub
    return data


def process_route_set_form(form, gym_id):

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


def routes_user_page(request, user_id, gym_id):

    is_users_page = security.check_user_credentials(request, user_id)

    grade_name = request.GET.get('grade',conf.default_grade_eden)
    grade = conf.Grade.get_value_from_name(grade_name)

    record_data = dal.get_records_for_active_routes(gym_id, user_id,grade=grade)
    grade_names = conf.get_grade_names()
    grade_sub_names = get_grade_sub_names_clean()
    grade_names_all = [conf.Grade(val).name for val in record_data['grade']]
    grade_sub_names_all = [conf.GradeSub(val).name for val in record_data['grade_sub']]
    
    n_total_climbs = metrics.get_total_climbs_for_route(record_data['id'])

    route_data = zip(record_data['id'],
                     record_data['number'],
                     grade_names_all,
                     grade_sub_names_all,
                     get_grade_hex_colour(record_data['grade']),
                     get_sub_grade_icon_class(record_data['grade_sub']),
                     record_data['is_climbed'],
                     record_data['date_climbed'],
                     record_data['num_climbed'],
                     record_data['is_onsight'],
                     record_data['is_attempted'],
                     record_data['num_attempted'],
                     n_total_climbs)
    
    data = {'route_data': route_data,
            'user_id': user_id,
            'is_users_page':is_users_page,
            'gym_id': gym_id,
            'active_grade': grade,
            'grade_names': grade_names,
            'grade_sub_names': grade_sub_names,
            'climb_status_climbed': conf.ClimbStatus.climbed.value,
            'climb_status_attempt': conf.ClimbStatus.attempted.value,
            'climb_status_onsight': conf.ClimbStatus.onsight.value,
            'n_climbed': sum(record_data['is_climbed']),
            'n_routes': len(record_data['id'])}
            
    return render(request, 'routes_user.html', data, user_id)

def route_record_delete(request, user_id, gym_id,route_id):
        
    if security.check_user_credentials(request, user_id):
        services.records.delete_route_record_for_user(user_id,route_id)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseForbidden()

def route_record_delete_last_entry(request, user_id, gym_id,route_id):
        
    if security.check_user_credentials(request, user_id):
        services.records.delete_last_route_record_entry_for_user(user_id,route_id)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseForbidden()

def route_page(request,gym_id,route_id):
    r = rec.record()   
    records = r.get_for_route(route_id,max_return=20,is_reversed=True)
    data = {'records':records,'gym_id':gym_id,'route_id':route_id,'user_id': request.user.id,'http_referer':request.META.get('HTTP_REFERER')}
    return render(request, 'route_page.html', data)




def record_route(request, user_id, gym_id, route_id,record_type):
    is_auth = security.check_user_credentials(request, user_id)
    is_valid = security.Validate().gym(gym_id)
    if is_auth and is_valid:
        dal.set_route_record_for_user(
            user_id, route_id, record_type)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseForbidden()



def get_active_grade_for_filter(user_id, gym_id):
    return dal.get_grade_name_of_last_recorded_climb(user_id, gym_id)

def get_grade_sub_names_clean():
    grade_sub_names = conf.get_grade_sub_names()
    if 'null' in grade_sub_names:
        grade_sub_names.remove('null')
    return grade_sub_names


def get_grade_hex_colour(grade_list):
    class_text = []
    # Colours came from https://htmlcolorcodes.com/
    for grade in grade_list:

        if grade == conf.Grade.purple.value:
            class_text.append('#A569BD')
        elif grade == conf.Grade.orange.value:
            class_text.append('#E67E22')
        elif grade == conf.Grade.green.value:
            class_text.append('#58D68D')
        elif grade == conf.Grade.yellow.value:
            class_text.append('#F1C40F')
        elif grade == conf.Grade.blue.value:
            class_text.append('#3498DB')
        elif grade == conf.Grade.white.value:
            class_text.append('#D0D3D4')
        elif grade == conf.Grade.black.value:
            class_text.append('#34495E')
        elif grade == conf.Grade.red.value:
            class_text.append('#E74C3C')
        else:
            class_text.append('#784212')
    return class_text


def get_sub_grade_icon_class(sub_grade_list):
    class_text = []
    for sub_grade in sub_grade_list:
        sub_grade_name = conf.GradeSub(sub_grade).name
        class_text.append(
            conf.GradeSubIcon.get_value_from_name(sub_grade_name))

    return class_text



