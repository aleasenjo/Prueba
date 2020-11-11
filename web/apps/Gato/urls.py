from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import GatoList, GatoCreate, GatoUpdate , GatoDelete,GatoList2,GatoList3

urlpatterns = [
    path('listar/', GatoList.as_view(), name="gatos_list"),
    path('contenido/', GatoList2.as_view(), name="gatos_list2"),
    path('cuidados/', GatoList3.as_view(), name="gatos_list3"),

    path('crear/', GatoCreate.as_view(), name="gatos_form"),
    path('editar/<int:pk>', GatoUpdate.as_view(), name="gatos_update"),
    path('borrar/<int:pk>', GatoDelete.as_view(), name="gatos_borrar"),
    
]
