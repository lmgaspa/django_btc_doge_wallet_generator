from django.urls import path
from . import views
from . import viewsnoid  # Importa viewsnoid do arquivo viewsnoid.py

urlpatterns = [
    
    path('viewsnoid/', viewsnoid.viewsnoid, name='viewsnoid'),  # Usa viewsnoid.viewsnoid para acessar a função de view
]


"""
 path('', viewsnoid.viewsnoid, name='index'),
 """