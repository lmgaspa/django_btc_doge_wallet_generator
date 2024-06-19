from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('btcaddressgenerator.urls')),
    path('btcaddressgenerator/', include('btcaddressgenerator.urls')
]
