from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect



def user_tracks_page(request):
    context={}
    return render(request,'dashboard/dashboard.html',context)



