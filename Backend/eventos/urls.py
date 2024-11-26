from django.urls import path
from .views import EventoListCreate, EventoRetrieveUpdateDestroy, BanqueteriaListCreate, BanqueteriaRetrieveUpdateDestroy, ComponenteListCreate, ComponenteRetrieveUpdateDestroy, LocalListCreate, LocalRetrieveUpdateDestroy, EventoComponenteListCreate, EventoComponenteRetrieveUpdateDestroy

urlpatterns = [
    path('evento/', EventoListCreate.as_view(), name='evento-list-create'),  
    path('evento/<int:pk>/', EventoRetrieveUpdateDestroy.as_view(), name='evento-detail'),   
    path('banqueteria/', BanqueteriaListCreate.as_view(), name='banqueteria-list-create'),  
    path('banqueteria/<int:pk>/', BanqueteriaRetrieveUpdateDestroy.as_view(), name='banqueteria-detail'),
    path('componente/', ComponenteListCreate.as_view(), name='componente-list-create'),  
    path('componente/<int:pk>/', ComponenteRetrieveUpdateDestroy.as_view(), name='componente-detail'),
    path('local/', LocalListCreate.as_view(), name='local-list-create'),  
    path('local/<int:pk>/', LocalRetrieveUpdateDestroy.as_view(), name='local-detail'),
    path('evento-componente/', EventoComponenteListCreate.as_view(), name='evento-componente-list-create'),  
    path('evento-componente/<int:pk>/', EventoComponenteRetrieveUpdateDestroy.as_view(), name='evento-componente-detail'),
]
