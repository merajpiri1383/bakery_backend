from django.contrib import admin
from django.urls import path,include,re_path 
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("bakery/",include("product.urls")),
    path("auth/",include("user.urls")),
    path("cart/",include("cart.urls")),
    re_path("^media/(?P<path>.*)$",serve,{"document_root":settings.MEDIA_ROOT}),
]
