from django.urls import path
from .views import InformeListCreate, InformeRetrieveUpdateDestroy, InformeReserva

urlpatterns = [
    path('informe/', InformeListCreate.as_view(), name='informe-list-create'),  
    path('informe/<int:pk>/', InformeRetrieveUpdateDestroy.as_view(), name='informe-detail'),
    path('informe-reserva/', InformeReserva.as_view(), name='informe-reserva')
]
