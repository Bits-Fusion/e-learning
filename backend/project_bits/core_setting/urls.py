from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_root/', include('auth_api_root.urls')),
    path('auth/', include('rest_framework.urls'))
]