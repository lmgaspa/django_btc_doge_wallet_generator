from django.urls import path
from . import views

urlpatterns = [
    path('create_wallets_btc/', views.create_wallets_btc, name='create_wallets_btc'),
    path('create_wallets_doge/', views.create_wallets_doge, name='create_wallets_doge'),
]