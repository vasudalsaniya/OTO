from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
    path('driver/',include('driver.urls')),
    path('repair/',include('repair.urls')),
    path('vehicle/',include('vehicle.urls')),
    path('home/',include('home.urls')),
]
