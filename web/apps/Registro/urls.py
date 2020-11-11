from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [

    # listar los mensajes de la bd
    path('listarMensajes', views.listar_mensajes, name="listar_mensajes"),
    path('add_mensaje', views.MensajeCreate.as_view(), name="add_mensaje"),
    # path('list_mensajes/', views.MensajeList.as_view(), name='list_mensajes'),
    path('list_mensajes/', views.mantenedor , name="list_mensajes"), 


    path('edit_mensaje/<int:pk>', views.MensajeUpdate.as_view(), name='edit_mensaje'),

    path('del_mensaje/<int:pk>', views.MensajeDelete.as_view(), name='del_mensaje'),
]
