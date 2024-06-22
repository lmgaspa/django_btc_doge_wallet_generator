from django.urls import path
from . import views

urlpatterns = [
    path('', views.btcaddressgenerator, name='btcaddressgenerator'),
]