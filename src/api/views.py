from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Create your views here.


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, format=None):

        # metrics.get_percentage_complete_for_active_grade(
        #     gym_id, user_id, grade)

        data = {'sales': 10, 'customers': 100}
        return Response(data)


"""
def chart_data(request):
    dataset = Passenger.objects \
        .values('embarked') \
        .exclude(embarked='') \
        .annotate(total=Count('embarked')) \
        .order_by('embarked')

    port_display_name = dict()
    for port_tuple in Passenger.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)

"""
