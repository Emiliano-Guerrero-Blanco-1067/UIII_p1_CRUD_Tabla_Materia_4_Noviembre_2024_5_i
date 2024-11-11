from django.urls import path
from . import views
urlpatterns = [
    path('',views.inicio_vistas,name='gestionarMateria.html'),
    path('registrarMateria/',views.registrarMateria,  name='registrarMateria'),
    path("seleccionarMateria/<codigo>" ,views.seleccionarMateria ,name="seleccionarMateria"),
    path("editarMateria/", views.editarMateria),
    path("borrarMateria/<codigo>", views.borrarMateria, name="borrarMateria")
]