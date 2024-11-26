from django.urls import path
from .views import PagoListCreate, PagoRetrieveUpdateDestroy

urlpatterns = [
    path('pago/', PagoListCreate.as_view(), name='pago-list-create'),  
    path('pago/<int:pk>/', PagoRetrieveUpdateDestroy.as_view(), name='pago-detail')
]
