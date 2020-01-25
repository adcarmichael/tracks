from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from routes.services import metrics, records
from routes.views import get_sub_grade_icon_class, get_grade_hex_colour
import urllib
from django.shortcuts import redirect
from django.contrib.auth.models import User

from routes.services import security


def redirect_params(url, params=None):
    response = redirect(url)
    if params:
        query_string = urllib.parse.urlencode(params)
        response['Location'] += '?' + query_string
    return response


def your_view(request):
    your_params = {
        'item': 4
    }
    return redirect_params('search_view', your_params)


def user_dashboard_page(request):
    template_name = 'dashboard/dashboard.html'

    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    user = request.GET.get('user')

    if not user:
        params = {
            'user': request.user,
        }
        return redirect_params('user_dashboard', params)

    user_id = security.get_user_id_from_username(user)
    if not user_id:
        return HttpResponseForbidden()

    rec = records.record(is_reversed=True, max_return=20)
    rec_data = rec.get_for_user(user_id)
    rec_data = update_data_colour(rec_data)
    rec_data = update_data_icon(rec_data)

    context = {'username': user,
               'user_id': user_id,
               'records': rec_data}

    return render(request, template_name, context)


def update_data_icon(data):
    for item in data:

        item.update(
            {"icon": get_sub_grade_icon_class(item['grade_sub'])[0]})
    return data


def update_data_colour(data):
    for item in data:

        item.update(
            {"colour": get_grade_hex_colour(item['grade'])[0]})
    return data
