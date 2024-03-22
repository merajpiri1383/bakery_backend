from django.urls import path 
from product import views 
urlpatterns = [
    path("category/",views.CategoryListCreateAPIView.as_view()),
    path("category/<pk>/",views.CategoryAPIView.as_view()),
    path("category/<category_id>/subcategory/",views.SubcategoryListCreateAPIView.as_view()),
    path("subcategory/",views.ListSubcategoryAPIView.as_view()),
    path("subcategory/<subcategory_id>/",views.SubCategoryAPIView.as_view()),
    path("products/",views.ProductListCreateAPIView.as_view()),
    path("products/<pk>/",views.ProductAPIView.as_view()),
]