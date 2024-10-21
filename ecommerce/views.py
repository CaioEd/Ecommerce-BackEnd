from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

from .serializers import UserSerializer

# Create your views here.

# ROTAS GET

def home(request):
    return HttpResponse('test')


def login(request):
    return HttpResponse('')


def registration_page(request):
    return HttpResponse('')


def cart(request):
    return HttpResponse('')


# ROTAS POST

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)