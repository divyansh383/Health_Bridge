from django.shortcuts import render
from django.http import HttpResponse
from .models import Report,User,DoctorProfile
from .serializers import reportSerializer
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

from rest_framework.exceptions import ParseError

@api_view(['POST'])
def setSymptoms(request):
    try:
        user=User.objects.get(pk=request.data['id'])
        symptoms=request.data['symptoms']
        address=request.data['address']
    except KeyError:
        raise ParseError('Invalid input data')

    try:
        pat=Report.objects.create(patient=user,symptoms=symptoms,address=address)
        pat.save()
    except Exception as e:
        return Response({'error': str(e)}, status=500)

    return Response('Report Added')

@api_view(['GET'])
def getReports(request):
    reports = Report.objects.all()
    serializer = reportSerializer(reports, many=True)
    return Response(serializer.data)

