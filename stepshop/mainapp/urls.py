from django.urls import path

from .views import products, product

urlpatterns = [
    path('', products),
    path('product/', product),
]
