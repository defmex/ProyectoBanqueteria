from django.urls import path
from .views import EventoListCreate, EventoRetrieveUpdateDestroy, BanqueteriaListCreate, BanqueteriaRetrieveUpdateDestroy, ComponenteBanqueteriaListCreate, ComponenteBanqueteriaRetrieveUpdateDestroy, LocalListCreate, LocalRetrieveUpdateDestroy

urlpatterns = [
    path('evento/', EventoListCreate.as_view(), name='evento-list-create'),  
    path('evento/<int:pk>/', EventoRetrieveUpdateDestroy.as_view(), name='evento-detail'),   
    path('banqueteria/', BanqueteriaListCreate.as_view(), name='banqueteria-list-create'),  
    path('banqueteria/<int:pk>/', BanqueteriaRetrieveUpdateDestroy.as_view(), name='banqueteria-detail'),
    path('componente/', ComponenteBanqueteriaListCreate.as_view(), name='componente-banqueteria-list-create'),  
    path('componente/<int:pk>/', ComponenteBanqueteriaRetrieveUpdateDestroy.as_view(), name='componente-banqueteria-detail'),
    path('local/', LocalListCreate.as_view(), name='local-list-create'),  
    path('local/<int:pk>/', LocalRetrieveUpdateDestroy.as_view(), name='local-detail'),
]
