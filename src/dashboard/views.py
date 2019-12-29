from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from routes.services import metrics
import urllib
from django.shortcuts import redirect


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

    user_id = request.GET.get('user_id')

    if not user_id:
        params = {
            'user_id': request.user
        }
        return redirect_params('/tracks', params)

    context = {'user_id': user_id}
    return render(request, template_name, context)
