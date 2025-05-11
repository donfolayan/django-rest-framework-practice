from django.urls import path
from .views import (
    ProductDetailAPIView,
    ProductListCreateAPIView,
    ProductListAPIView,
    product_alt_view,
)

urlpatterns = [
    path('', product_alt_view, name='product-create'),
    path('<int:pk>/', product_alt_view, name='product-detail'),
]