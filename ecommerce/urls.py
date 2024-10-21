from django.urls import path
from . import views
from .views import register_user, login, registration_page, cart 

app_name = 'ecommerce'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login, name='login'),
    path('registration', registration_page, name='registration'),
    path('cart/', cart, name='cart'),
    path('registration/', register_user, name='registration'),
]