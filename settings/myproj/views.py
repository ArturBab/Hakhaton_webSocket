from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


def lobby(request):
    return render(request, 'lobby.html')


@api_view(['GET'])
def get_data(request):
    response = requests.get('http://127.0.0.1:8000/')
    return Response(response)
# Create your views here.
