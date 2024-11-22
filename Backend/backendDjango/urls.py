from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuario.urls')),
    path('eventos/', include('eventos.urls')),
    path('pagos/', include('pagos.urls')),
    path('informes/', include('informes.urls')),
    path('reservas/', include('reservas.urls'))
]
