from django.urls import path
from . import views

urlpatterns = [
    path('solanaaddressgenerator/', views.solanaaddressgenerator, name='solanaaddressgenerator'),
]