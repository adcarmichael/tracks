from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import JsonResponse

from routes.services import metrics, conf, utils

from django.contrib.auth.models import User

# Create your views here.


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, format=None):
        user = self.request.GET.get('user')

        if not user:
            return Response({})

        user_id = User.objects.get(username=user).pk

        gym_id = 1

        labels = []
        data_current = []
        data_previous = []
        for grade in range(3, 9):
            perc_current = metrics.get_percentage_complete_for_active_grade(
                gym_id, user_id, grade)

            perc_prev = metrics.get_percentage_complete_for_previously_active_grade(
                gym_id, user_id, grade)

            labels.append(utils.get_grade_name_from_value(grade))
            data_current.append(round(perc_current, 1))
            data_previous.append(round(perc_prev, 1))

        context = {
            'type': 'radar',
            'data': {
                'labels': labels,
                'datasets': [{
                    'label': 'Current (%)',
                    'data': data_current,
                    'backgroundColor': [
                        'rgba(54, 162, 235, 0.2)',
                    ],
                    'borderColor': [
                        'rgba(54, 162, 235, 1)',
                    ],
                    'borderWidth': 1
                },
                    {
                    'label': 'Previous (%)',
                    'data': data_previous,
                    'backgroundColor': [
                        'rgba(255, 206, 86, 0.1 )',
                    ],
                    'borderColor': [
                        'rgba(255, 206, 86, 0.5)',
                    ],
                    'borderWidth': 1
                }]
            },
            'options': {
                'scale': {
                    'ticks': {
                        'suggestedMin': 0,
                        'suggestedMax': 100,
                        'stepSize': 25
                    }

                }
            }
        }

        return Response(context)
