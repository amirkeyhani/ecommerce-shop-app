from django.urls import path, include
from .views import *

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products', ProductCreate.as_view(), name='product-create'),
    path('products/<int:pk>/detail', ProductDetail.as_view(), name='product-detail'),
    path('products/<int:pk>', ProductUpdate.as_view(), name='product-update'),
    path('products/<int:pk>', ProductDelete.as_view(), name='product-delete'),
    
    path('categories', CategoryList.as_view(), name='category-list'),
    path('categories', CategoryCreate.as_view(), name='category-create'),
    path('categories/<int:pk>/detail', CategoryDetail.as_view(), name='category-detail'),
    path('categories/<int:pk>', CategoryUpdate.as_view(), name='category-update'),
    path('categories/<int:pk>', CategoryDelete.as_view(), name='category-delete'),
    
    path('customers', CustomerList.as_view(), name='customer-list'),
    path('customers', CustomerCreate.as_view(), name='customer-create'),
    path('customers/<int:pk>/detail', CustomerDetail.as_view(), name='customer-detail'),
    path('customers/<int:pk>', CustomerUpdate.as_view(), name='customer-update'),
    path('customers/<int:pk>', CustomerDelete.as_view(), name='customer-delete'),
    
    path('orders', OrderList.as_view(), name='order-list'),
    path('orders', OrderCreate.as_view(), name='order-create'),
    path('orders/<int:pk>/detail', OrderDetail.as_view(), name='order-detail'),
    path('orders/<int:pk>', OrderUpdate.as_view(), name='order-update'),
    path('orders/<int:pk>', OrderDelete.as_view(), name='order-delete'),
    
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
