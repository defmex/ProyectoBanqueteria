from django.urls import path
from .views import ReservaListCreate, ReservaRetrieveUpdateDestroy

urlpatterns = [
    path('reserva/', ReservaListCreate.as_view(), name='reserva-list-create'),  
    path('reserva/<int:pk>/', ReservaRetrieveUpdateDestroy.as_view(), name='reserva-detail')
]
