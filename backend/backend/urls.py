from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # api
    path('api/users/', include('users.urls')),
    path('api/vehicles/', include('vehicle_management.urls')),
]
