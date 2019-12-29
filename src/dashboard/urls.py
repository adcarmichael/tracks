from django.urls import path, include
from dashboard.views import user_dashboard_page

urlpatterns = [
    path('', user_dashboard_page, name='user_dashboard'),
]
