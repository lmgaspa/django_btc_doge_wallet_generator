from django.urls import path
from . import views

urlpatterns = [
    path('noid/', views.noid, name='noid'),
]