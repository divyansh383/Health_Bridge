from django.shortcuts import render
from django.http import HttpResponse

#rest_framework
from rest_framework.response import Response 
from rest_framework.decorators import api_view 

# Create your views here.
def index(request):
    return HttpResponse("django backend")

api_view(['GET'])
def api(request):
    data={'message':'hello world'}
    return Response(data)

api_view(['POST'])
def setSymptoms(request):
    symptops=request.data['symptoms']
    pass