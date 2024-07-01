from django.urls import path
from . import views

urlpatterns = [
    path('', views.doge_address_generator, name='doge_address_generator'),
]