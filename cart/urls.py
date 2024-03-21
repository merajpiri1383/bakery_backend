from django.urls import path
from cart import views
urlpatterns = [
    path("",views.CartListAPIView.as_view()),
    path("<cart_id>/",views.CartAPIView.as_view()),
    path("product/<product_id>/",views.CartProductAPIView.as_view()),
]