from django.urls import path
from . import views
from .views import btcaddressgenerator

urlpatterns = [
    path('btcaddressgenerator/', views.btcaddressgenerator, name='btcaddressgenerator'),
]