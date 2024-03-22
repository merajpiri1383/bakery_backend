from django.contrib import admin
from django.urls import path,include,re_path 
from django.views.static import serve
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("bakery/",include("product.urls")),
    path("auth/",include("user.urls")),
    path("cart/",include("cart.urls")),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    re_path("^media/(?P<path>.*)$",serve,{"document_root":settings.MEDIA_ROOT}),
]
