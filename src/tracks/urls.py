"""tracks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from routes.views import home_page
from routes.views import routes_page
from routes.views import signup
from routes.views import account_activation_sent
from routes.views import activate
import routes.views as rv
import routes.views as rv
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('test', rv.test_page),
    path('gyms', rv.gyms_page),
    path('gyms/add/', rv.gyms_add, name='add_new_gym'),
    path('gyms/<int:gym_id>/routes', routes_page, name='routes'),
    path('gyms/<int:gym_id>/routes/set/add/', rv.route_set_add_page,
         name='add_route_set_page'),
    path('gyms/<str:gym_id>/routes/<int:route_id>',
         routes_page, name='route_ind'),
    path('users/<int:user_id>/<int:gym_id>/routes',
         rv.routes_user_page, name='routes_for_user'),
    path('users/<int:user_id>/<int:gym_id>/routes/<int:route_id>/record/',
         rv.record_route, name='routes_record_for_user'),
    url(r'^account_activation_sent/$', account_activation_sent,
        name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]