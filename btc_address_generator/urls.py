from django.urls import path
from . import views

urlpatterns = [
    path('', views.btc_address_generator, name='btc_address_generator'),
]