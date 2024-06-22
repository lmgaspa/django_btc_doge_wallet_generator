# urls.py

from django.urls import path, include
from . import viewsnoid, views

urlpatterns = [
    path('viewsnoid/', viewsnoid.viewsnoid, name='viewsnoid'),
    path('btcaddressgenerator/', views.btcaddressgenerator, name='btcaddressgenerator'),
]

"""
 path('', viewsnoid.viewsnoid, name='index'),
 """