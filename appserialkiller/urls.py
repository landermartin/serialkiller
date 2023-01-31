from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registro',views.registro_killer,name='registro'),
    path('visualizar',views.mostrar_killers,name='visualizar'),
    path('killer/<int:killer_id>',views.mostrar_killer,name='singlekiller')
]