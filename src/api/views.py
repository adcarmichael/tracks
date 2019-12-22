from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Create your views here.

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):




        data = {'sales':10,'customers':100}
        return Response(data)

