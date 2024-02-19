from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/' , include("drf_social_oauth2.urls", namespace='drf')),
    path('api_root/auth/', include('auth_api_root.urls')),
    path('api_root/couser/', include('video_api_root.urls')),
]