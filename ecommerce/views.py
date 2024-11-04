from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import  JsonResponse
from .models import Product
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


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


def list_products(request): # LISTAGEM DE PRODUTOS
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

@csrf_exempt
def register_user(request):

    if request.method == 'POST':
        data = json.loads(request.body) # Carrega dados enviados pelo front.
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Este email já está sendo usado por outro usuário.'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Este nome de usuário já está sendo usado.'}, status=400)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'success': 'Usuário cadastrado com sucesso'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


# Login de usuário
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username
        })
    return Response({'error': 'Dados Inválidos'}, status=400)