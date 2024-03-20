from django.urls import path 
from product import views 
urlpatterns = [
    path("category/",views.CategoryListCreateAPIView.as_view()),
    path("category/<pk>/",views.CategoryAPIView.as_view()),
    path("products/",views.ProductListCreateAPIView.as_view()),
    path("products/<pk>/",views.ProductAPIView.as_view()),
]