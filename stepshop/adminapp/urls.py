from django.urls import path

import adminapp.views as adminapp
from adminapp.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, \
                           CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView


app_name = 'adminapp'

urlpatterns = [
    # path('users/create/', adminapp.user_create, name='user_create'),
    # path('users/read/', adminapp.users, name='users'),
    # path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    # path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/read/', UserListView.as_view(), name='users'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', CategoryListView.as_view(), name='categories'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminapp.products, name='products'),
    path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),
]


# Create
# Read
# Update
# Delete
