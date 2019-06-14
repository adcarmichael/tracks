from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView


def home_page(request):
    return render(request, 'home_page.html')
