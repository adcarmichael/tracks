from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from routes import services


dal = services.get_dal()


def home_page(request):
    return render(request, 'home_page.html')


def add_route_set(request, details):
    pass


def routes_page(request):
    data_black = dal.get_route_set_of_colour('black')
    black = zip(data_black.get_number(),
                data_black.get_colour())
    print(black)
    data = {
        'purple': dal.get_route_set_of_colour('purple'),
        'orange': dal.get_route_set_of_colour('orange'),
        'green': dal.get_route_set_of_colour('green'),
        'yellow': dal.get_route_set_of_colour('yellow'),
        'blue': dal.get_route_set_of_colour('blue'),
        'white': dal.get_route_set_of_colour('white'),
        'red': dal.get_route_set_of_colour('red'),
        'black': black}

    return render(request, 'routes.html', data)
