from django.urls import path
from .views import ClienteListCreate, ClienteRetrieveUpdateDestroy, TrabajadorListCreate, TrabajadorRetrieveUpdateDestroy

urlpatterns = [
    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-detail'),
    path('trabajador/', TrabajadorListCreate.as_view(), name='trabajador-list-create'),
    path('trabajador/<int:pk>/', TrabajadorRetrieveUpdateDestroy.as_view(), name='trabajador-detail'),
]
