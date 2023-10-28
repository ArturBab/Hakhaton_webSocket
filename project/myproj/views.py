from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import time

def index(request):
    return render(request, 'index.html')

depth = 0
oxygen = 100
fuel = 100


def submarine(move):
    global depth
    global oxygen  # в %
    global fuel  # в %
    while oxygen & fuel:
        if move:
            depth = depth - move
        if depth != 0:
            oxygen = oxygen - 5
        else:
            oxygen = 100
        fuel = fuel - 1
        yield ({'depth': depth, 'oxygen': oxygen, 'fuel': fuel})
        time.sleep(2)


@api_view(['GET'])
def get_data(request):
    return Response(next(submarine(5)))

# Create your views here.
