from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import list_products, register_user, login_view

app_name = 'ecommerce'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.list_products, name='list_products'),
    path('registration/', register_user, name='register'),
    path('login/', login_view, name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
