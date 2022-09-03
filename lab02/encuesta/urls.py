

from django.urls import path
from . import views

app_name = 'encuesta'

urlpatterns = [
    #1path('', views.index,name='index'),
    #1path('enviar', views.enviar,name='enviar'),
    
    #2path('', views.indexmatematico,name='indexmatematico'),
    #2path('enviar2', views.enviar2,name='enviar2'),
    
    path('', views.indexcilindro,name='indexcilindro'),
    path('calcular', views.calcular,name='calcular'),
   
]
