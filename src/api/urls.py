from django.urls import path, include
from api.views import ChartData

urlpatterns=[
   path('chart/data',ChartData.as_view()),
]