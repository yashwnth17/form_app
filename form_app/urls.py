from django.urls import path
from .views import create_product , product_list,search_product

urlpatterns = [
    path('create/', create_product, name='create_product'),
    path('product-list/', product_list, name='product_list'),
    path('search/', search_product, name='search_product'),
]