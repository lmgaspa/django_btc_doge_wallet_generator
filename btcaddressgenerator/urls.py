from django.urls import path
from . import views

urlpatterns = [
    path('btcaddressgenerator/', views.btcaddressgenerator, name='btcaddressgenerator'),
]