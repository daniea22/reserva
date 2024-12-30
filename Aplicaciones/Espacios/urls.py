from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio), 

    path('crear_espacio/', views.crear_espacio),
    path('guardar_espacio/', views.guardar_espacio, name='guardar_espacio'),
    path('editar_espacio/<int:id>/', views.editar_espacio, name='editar_espacio'),
    path('eliminar_espacio/<int:id>/', views.eliminar_espacio, name='eliminar_espacio'),
    path('lista_espacios/', views.lista_espacios, name='lista_espacios'),

    #######################################################################################3
    #cliente
    path('crear_cliente/', views.crear_cliente),
    path('lista_clientes/', views.lista_clientes, name='lista_cliente'),
    path('guardar_cliente/', views.guardar_cliente, name='guardar_cliente'),
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),

    ####################################################################################################
    path('crear_reserva/', views.crear_reserva),
    path('guardar_reserva/', views.guardar_reserva, name='guardar_reserva'),
    path('lista_reservas/', views.lista_reservas, name='lista_reserva'),
    path('eliminar_reserva/<int:id>/', views.eliminar_reserva, name='eliminar_reserva'),
    path('editar_reserva/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
    ###########################################################

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
