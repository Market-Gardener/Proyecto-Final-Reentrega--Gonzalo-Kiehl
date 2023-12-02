from django.urls import path, include
from Isaac import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('items/', views.seccionItems, name="Item"),
    path('formItems/', views.itemFormulario, name="FormItem"),
    path('itemBusqueda/', views.itemBusqueda, name="ItemBusqueda"),
    path('buscarItem/', views.buscarItem, name="BucarItem"),
    path('contacto/', views.contacto, name="Contacto"),
    path('logout/', views.salir, name="Salir"),
    path('nope/', views.nada, name="Nada"),
]