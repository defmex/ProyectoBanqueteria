from django.urls import path
from .views import ClienteListCreate, ClienteRetrieveUpdateDestroy, TrabajadorListCreate, TrabajadorRetrieveUpdateDestroy, ClienteLogin, TrabajadorLogin

urlpatterns = [
    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'), # Url para llamar a los clientes general 
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-detail'),  # Url para llamar a los clientes especifico 
    path('clientes/login/', ClienteLogin.as_view(), name='cliente-login'),
    path('trabajador/', TrabajadorListCreate.as_view(), name='trabajador-list-create'), #  Url para llamar a los trabajadores general 
    path('trabajador/<int:pk>/', TrabajadorRetrieveUpdateDestroy.as_view(), name='trabajador-detail'), # Url para llamar a los trabajadores especifico 
    path('trabajador/login/', TrabajadorLogin.as_view(), name='trabajador-login'),
]
