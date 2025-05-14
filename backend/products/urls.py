from django.urls import path
from .views import (
    ProductDetailAPIView,
    ProductListCreateAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    ProductListAPIView,
    product_alt_view,
)

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='product-create'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]