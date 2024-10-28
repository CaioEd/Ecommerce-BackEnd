from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from .models import Product
from .serializers import UserSerializer

import json

User = get_user_model()

# Create your views here.

# === ROTAS GET ===

def home(request):
    data = {
        'message': 'Welcome to the Home Page!',
        'status': 'sucess'
    }

    return JsonResponse(data)


# LISTAGEM DE PRODUTOS

def list_products(request):
    products = Product.objects.all() # Consulta todos produtos
    products_list = list(products.values())
    return JsonResponse(products_list, safe=False)


# ROTAS POST

# Usuários django admin
@api_view(['POST'])
def register_user_admin(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Usuários app

@api_view(['POST'])
def register_user(request):

    if request.method == 'POST':
        data = json.loads(request.body) # Carrega dados enviados pelo front.
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already registered.'}, status=400)
    
        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'success': 'User registered successfully'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)