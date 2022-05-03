from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Calculate
from .serializers import CalculateSerializer
from .models import Calculate


# Create your views here.

@api_view(['POST'])
def addnum(request):
    if request.method == 'POST':
        item = CalculateSerializer(data=request.data)
        if item.is_valid():
            item.save()
            data1 = request.data
            sumo = int(data1['num1']) + int(data1['num2'])
            a = Calculate.objects.latest('id')
            a.output = sumo
            a.save()
            return Response(a.output)

@api_view(['POST'])
def subnum(request):
    if request.method == 'POST':
        item = CalculateSerializer(data=request.data)
        if item.is_valid():
            item.save()
            data1 = request.data
            subo = int(data1['num1']) - int(data1['num2'])
            a = Calculate.objects.latest('id')
            a.output = subo
            a.save()
            return Response(a.output)