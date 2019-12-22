from django.urls import path, include
from dashboard.views import user_tracks_page

urlpatterns=[
   path('',user_tracks_page),
]