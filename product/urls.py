from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/categories/', views.category_list_api_view, name = 'category-list'),
    path('api/v1/categories/<int:id>/', views.category_detail_api_view, name = 'category-detail'),
    path('api/v1/products/', views.product_list_api_view, name = 'product-list'),
    path('api/v1/products/<int:id>/', views.product_detail_api_view, name = 'product-detail'),
    path('api/v1/reviews/', views.review_list_api_view, name = 'review-list'),
    path('api/v1/reviews/<int:id>/', views.review_detail_api_view, name = 'review-detail'),
]