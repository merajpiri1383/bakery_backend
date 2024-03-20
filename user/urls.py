from django.urls import path 
from rest_framework_simplejwt.views import TokenRefreshView
from user import views 
urlpatterns = [
    path("register/",views.register_user_api_view),
    path("login/",views.login_user_api_view),
    path("activate/",views.activate_email_api_view),
]