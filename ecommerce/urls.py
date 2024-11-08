from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, list_products, register_user, login_view, product_detail, search_products

app_name = 'ecommerce'

urlpatterns = [
    path('', home, name='home'),
    path('products/', list_products, name='list_products'),
    path('products/<int:id>/', product_detail, name='product-detail'),
    path('registration/', register_user, name='register'),
    path('login/', login_view, name='login'),
    path('search/', search_products, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
