from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def welcome(request):
    return Response("Welcome to API")

@api_view(['Post'])
def Postmethod(request):
    return Response("This is post method")

@api_view(['GET','Post'])
def getrespond(request):
    return Response("which")